# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from categoria_app.commands import ListCategoriaCommand, SaveCategoriaCommand, UpdateCategoriaCommand, \
    CategoriaPublicForm, CategoriaDetailForm, CategoriaShortForm


def save_categoria_cmd(**categoria_properties):
    """
    Command to save Categoria entity
    :param categoria_properties: a dict of properties to save on model
    :return: a Command that save Categoria, validating and localizing properties received as strings
    """
    return SaveCategoriaCommand(**categoria_properties)


def update_categoria_cmd(categoria_id, **categoria_properties):
    """
    Command to update Categoria entity with id equals 'categoria_id'
    :param categoria_properties: a dict of properties to update model
    :return: a Command that update Categoria, validating and localizing properties received as strings
    """
    return UpdateCategoriaCommand(categoria_id, **categoria_properties)


def list_categorias_cmd():
    """
    Command to list Categoria entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCategoriaCommand()


def categoria_detail_form(**kwargs):
    """
    Function to get Categoria's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CategoriaDetailForm(**kwargs)


def categoria_short_form(**kwargs):
    """
    Function to get Categoria's short form. just a subset of categoria's properties
    :param kwargs: form properties
    :return: Form
    """
    return CategoriaShortForm(**kwargs)

def categoria_public_form(**kwargs):
    """
    Function to get Categoria'spublic form. just a subset of categoria's properties
    :param kwargs: form properties
    :return: Form
    """
    return CategoriaPublicForm(**kwargs)


def get_categoria_cmd(categoria_id):
    """
    Find categoria by her id
    :param categoria_id: the categoria id
    :return: Command
    """
    return NodeSearch(categoria_id)


def delete_categoria_cmd(categoria_id):
    """
    Construct a command to delete a Categoria
    :param categoria_id: categoria's id
    :return: Command
    """
    return DeleteNode(categoria_id)

