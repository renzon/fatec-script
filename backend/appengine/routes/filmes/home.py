# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from filme_app import facade
from routes.filmes import admin, rest


@login_not_required
@no_csrf
def index():
    context = {
        'salvar_path': router.to_path(rest.save),
        'deletar_path': router.to_path(rest.delete),
        'editar_path': router.to_path(rest.update),
        'listar_path': router.to_path(rest.index)}
    return TemplateResponse(context)

