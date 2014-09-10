# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.base import EmailField
from gaeforms.ndb.form import ModelForm
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def listar():
    query = Escravo.query().order(-Escravo.name)
    escravos = query.fetch()
    form_short = EscravoFormShort()
    escravos = [form_short.fill_with_model(e) for e in escravos]
    for e in escravos:
        e['edit_path']=router.to_path(edit_form,e['id'])
        e['delete_path']=router.to_path(deletar,e['id'])
    contexto = {'escravos': escravos}
    return TemplateResponse(contexto)

def deletar(escravo_id):
    key=ndb.Key(Escravo,int(escravo_id))
    key.delete()
    return RedirectResponse(router.to_path(listar))


@no_csrf
def edit_form(escravo_id):
    escravo=Escravo.get_by_id(int(escravo_id))
    escravo_form=EscravoForm()
    escravo_form.fill_with_model(escravo)
    contexto = {'salvar_path': router.to_path(editar,escravo_id),
                'escravo': escravo_form}
    return TemplateResponse(contexto, 'db/home.html')

def editar(escravo_id,**kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(editar,escravo_id),
                    'erros': erros,
                    'escravo': kwargs}
        return TemplateResponse(contexto, 'db/home.html')
    else:
        escravo=Escravo.get_by_id(int(escravo_id))
        escravo_form.fill_model(escravo)
        escravo.put()
        return RedirectResponse(router.to_path(listar))


@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Escravo(ndb.Model):
    birth = ndb.DateProperty()
    creation = ndb.DateTimeProperty(auto_now=True)
    age = ndb.IntegerProperty()
    name = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()


class EscravoForm(ModelForm):
    _model_class = Escravo
    # email=EmailField(required=True)
    _include = [Escravo.name, Escravo.age, Escravo.price, Escravo.birth]


class EscravoFormShort(ModelForm):
    _model_class = Escravo
    _include = [Escravo.name, Escravo.price, Escravo.birth, Escravo.creation]


def salvar(**kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'erros': erros,
                    'escravo': kwargs}
        return TemplateResponse(contexto, 'db/home.html')
    else:
        escravo = escravo_form.fill_model()
        escravo.put()
        return RedirectResponse(router.to_path(listar))