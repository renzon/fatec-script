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
    short_form = facade.filme_short_form()
    filme_short = [short_form.fill_with_model(m) for m in filme_list]
    return JsonResponse(filme_short)


@login_not_required
@no_csrf
def save(_resp, **filme_properties):
    cmd = facade.save_filme_cmd(**filme_properties)
    return _save_or_update_json_response(_resp, cmd)


@login_not_required
@no_csrf
def update(_resp, id, **filme_properties):
    cmd = facade.update_filme_cmd(id, **filme_properties)
    return _save_or_update_json_response(_resp, cmd)


@login_not_required
@no_csrf
def delete(id):
    facade.delete_filme_cmd(id)()


def _save_or_update_json_response(_resp, cmd):
    try:
        filme = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse(cmd.errors)
    short_form = facade.filme_short_form()
    return JsonResponse(short_form.fill_with_model(filme))

