# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from categoria_app import facade


def index():
    cmd = facade.list_categorias_cmd()
    categoria_list = cmd()
    short_form=facade.categoria_short_form()
    categoria_short = [short_form.fill_with_model(m) for m in categoria_list]
    return JsonResponse(categoria_short)


def save(**categoria_properties):
    cmd = facade.save_categoria_cmd(**categoria_properties)
    return _save_or_update_json_response(cmd)


def update(categoria_id, **categoria_properties):
    cmd = facade.update_categoria_cmd(categoria_id, **categoria_properties)
    return _save_or_update_json_response(cmd)


def delete(categoria_id):
    facade.delete_categoria_cmd(categoria_id)()


def _save_or_update_json_response(cmd):
    try:
        categoria = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.categoria_short_form()
    return JsonResponse(short_form.fill_with_model(categoria))

