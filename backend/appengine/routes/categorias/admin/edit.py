# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from categoria_app import facade
from routes.categorias import admin


@no_csrf
def index(categoria_id):
    categoria = facade.get_categoria_cmd(categoria_id)()
    detail_form = facade.categoria_detail_form()
    context = {'save_path': router.to_path(save, categoria_id), 'categoria': detail_form.fill_with_model(categoria)}
    return TemplateResponse(context, 'categorias/admin/form.html')


def save(_handler, categoria_id, **categoria_properties):
    cmd = facade.update_categoria_cmd(categoria_id, **categoria_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'categoria': cmd.form}

        return TemplateResponse(context, 'categorias/admin/form.html')
    _handler.redirect(router.to_path(admin))

