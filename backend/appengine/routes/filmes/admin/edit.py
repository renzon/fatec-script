# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from filme_app import facade
from routes.filmes import admin


@no_csrf
def index(filme_id):
    filme = facade.get_filme_cmd(filme_id)()
    detail_form = facade.filme_detail_form()
    context = {'save_path': router.to_path(save, filme_id), 'filme': detail_form.fill_with_model(filme)}
    return TemplateResponse(context, 'filmes/admin/form.html')


def save(_handler, filme_id, **filme_properties):
    cmd = facade.update_filme_cmd(filme_id, **filme_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'filme': cmd.form}

        return TemplateResponse(context, 'filmes/admin/form.html')
    _handler.redirect(router.to_path(admin))

