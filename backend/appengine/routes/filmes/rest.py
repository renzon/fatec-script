# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from filme_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_filmes_cmd()
    filme_list = cmd()
    short_form=facade.filme_short_form()
    filme_short = [short_form.fill_with_model(m) for m in filme_list]
    return JsonUnsecureResponse(filme_short)

@login_not_required
@no_csrf
def save(**filme_properties):
    cmd = facade.save_filme_cmd(**filme_properties)
    return _save_or_update_json_response(cmd)

@login_not_required
@no_csrf
def update(filme_id, **filme_properties):
    cmd = facade.update_filme_cmd(filme_id, **filme_properties)
    return _save_or_update_json_response(cmd)

@login_not_required
@no_csrf
def delete(filme_id):
    facade.delete_filme_cmd(filme_id)()


def _save_or_update_json_response(cmd):
    try:
        filme = cmd()
    except CommandExecutionException:
        return JsonUnsecureResponse(cmd.errors)
    short_form=facade.filme_short_form()
    return JsonUnsecureResponse(short_form.fill_with_model(filme))

