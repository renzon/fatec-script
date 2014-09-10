# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from filme_app import facade


def index():
    cmd = facade.list_filmes_cmd()
    filme_list = cmd()
    short_form=facade.filme_short_form()
    filme_short = [short_form.fill_with_model(m) for m in filme_list]
    return JsonResponse(filme_short)


def save(**filme_properties):
    cmd = facade.save_filme_cmd(**filme_properties)
    return _save_or_update_json_response(cmd)


def update(filme_id, **filme_properties):
    cmd = facade.update_filme_cmd(filme_id, **filme_properties)
    return _save_or_update_json_response(cmd)


def delete(filme_id):
    facade.delete_filme_cmd(filme_id)()


def _save_or_update_json_response(cmd):
    try:
        filme = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.filme_short_form()
    return JsonResponse(short_form.fill_with_model(filme))

