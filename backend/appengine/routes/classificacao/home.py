# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria_app.model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index():
    query = Categoria.query().order(Categoria.nome)
    categorias = query.fetch()
    for cat in categorias:
        cat.exibir_path = router.to_path(exibir, cat.key.id())
    contexto = {'categorias': categorias}
    return TemplateResponse(contexto)


@login_not_required
@no_csrf
def exibir(categoria_id):
    categoria = Categoria.get_by_id(int(categoria_id))
    query=Piloto.query(Piloto.categoria==categoria.key).order(-Piloto.pontuacao)
    lista_de_pilotos=query.fetch()
    contexto = {'lista_de_pilotos':lista_de_pilotos,
                'categoria': categoria,
                'salvar_path':router.to_path(salvar_piloto)}
    return TemplateResponse(contexto, 'classificacao/exibir.html')


@login_not_required
def salvar_piloto(categoria_id, nome, pontuacao):
    categoria_chave = ndb.Key(Categoria, int(categoria_id))
    piloto = Piloto(nome=nome, pontuacao=int(pontuacao),
                    categoria=categoria_chave)
    piloto.put()
    return RedirectResponse(router.to_path(exibir, categoria_id))


# Modelo e formulário

class Piloto(ndb.Model):
    nome = ndb.StringProperty(required=True)
    pontuacao = ndb.IntegerProperty(required=True)
    categoria = ndb.KeyProperty(Categoria, required=True)
