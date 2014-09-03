# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def f(nome, idade):
    print nome, idade


f('Renzo', 32)

f(idade=12, nome='Joe')


def g(*args, **kwargs):
    print args[0]
    print list(args)
    print kwargs


g(0)
g(1)
g(1, 2)

argumentos = range(4)

g(argumentos)
dct = {'nome': 'Renzo', 'idade': 32}
g(1,**dct)
