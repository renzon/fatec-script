# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from categoria_app.model import Categoria

class CategoriaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Categoria
    _include = [Categoria.nome]


class CategoriaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Categoria
    _include = [Categoria.nome]


class CategoriaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Categoria
    _include = [Categoria.creation, 
                Categoria.nome]


class CategoriaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Categoria
    _include = [Categoria.creation, 
                Categoria.nome]


class SaveCategoriaCommand(SaveCommand):
    _model_form_class = CategoriaForm


class UpdateCategoriaCommand(UpdateNode):
    _model_form_class = CategoriaForm


class ListCategoriaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCategoriaCommand, self).__init__(Categoria.query_by_creation())

