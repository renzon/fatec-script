# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from filme_app import facade
from routes.filmes.admin import new, edit


def delete(_handler, filme_id):
    facade.delete_filme_cmd(filme_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_filmes_cmd()
    filmes = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.filme_short_form()

    def short_filme_dict(filme):
        filme_dct = short_form.fill_with_model(filme)
        filme_dct['edit_path'] = router.to_path(edit_path, filme_dct['id'])
        filme_dct['delete_path'] = router.to_path(delete_path, filme_dct['id'])
        return filme_dct

    short_filmes = [short_filme_dict(filme) for filme in filmes]
    context = {'filmes': short_filmes,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

