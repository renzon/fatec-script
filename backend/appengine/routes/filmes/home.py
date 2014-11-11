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
    cmd = facade.list_filmes_cmd()
    filmes = cmd()
    public_form = facade.filme_public_form()
    filme_public_dcts = [public_form.fill_with_model(filme) for filme in filmes]
    context = {'filmes': filme_public_dcts,'admin_path':router.to_path(admin),
               'salvar_path':router.to_path(rest.save)}
    return TemplateResponse(context)

