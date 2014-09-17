# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from categoria_app import facade
from routes.categorias import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'categorias/admin/form.html')


def save(_handler, categoria_id=None, **categoria_properties):
    cmd = facade.save_categoria_cmd(**categoria_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'categoria': cmd.form}

        return TemplateResponse(context, 'categorias/admin/form.html')
    _handler.redirect(router.to_path(admin))

