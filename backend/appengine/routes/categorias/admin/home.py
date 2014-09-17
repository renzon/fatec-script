# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from categoria_app import facade
from routes.categorias.admin import new, edit


def delete(_handler, categoria_id):
    facade.delete_categoria_cmd(categoria_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_categorias_cmd()
    categorias = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.categoria_short_form()

    def short_categoria_dict(categoria):
        categoria_dct = short_form.fill_with_model(categoria)
        categoria_dct['edit_path'] = router.to_path(edit_path, categoria_dct['id'])
        categoria_dct['delete_path'] = router.to_path(delete_path, categoria_dct['id'])
        return categoria_dct

    short_categorias = [short_categoria_dict(categoria) for categoria in categorias]
    context = {'categorias': short_categorias,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

