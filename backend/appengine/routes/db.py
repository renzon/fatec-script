# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.ndb.form import ModelForm
from tekton import router


@no_csrf
def index():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)


class Escravo(ndb.Model):
    birth = ndb.DateProperty(auto_now=True)
    creation = ndb.DateTimeProperty()
    age = ndb.IntegerProperty()
    name = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()


class EscravoForm(ModelForm):
    _model_class = Escravo
    _include = [Escravo.name,Escravo.age]

def salvar(_resp, **kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        _resp.write(erros)
    else:
        campos = escravo_form.normalize()
        escravo = Escravo(**campos)
        escravo.put()
        _resp.write(campos)
