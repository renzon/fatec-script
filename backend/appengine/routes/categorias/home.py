# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from categoria_app import facade
from routes.categorias import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_categorias_cmd()
    categorias = cmd()
    public_form = facade.categoria_public_form()
    categoria_public_dcts = [public_form.fill_with_model(categoria) for categoria in categorias]
    context = {'categorias': categoria_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

