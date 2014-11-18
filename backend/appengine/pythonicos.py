# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from random import shuffle


class Carta():
    def __init__(self, numero, naipe):
        self.numero = numero
        self.naipe = naipe

    def __repr__(self):
        return '%s de %s' % (self.numero, self.naipe)


class Baralho():
    def __init__(self):
        self._cartas = [Carta(numero, naipe) for numero in 'As 1 2 3 4 5 6 7 8 9 10 Q J K'.split()
                        for naipe in 'Ouros Espadas Copas Paus'.split()]

    def __getitem__(self, index):
        return self._cartas[index]

    def __setitem__(self, key, value):
        self._cartas[key] = value

    def __len__(self):
        return len(self._cartas)


print Carta('As', 'Paus')
baralho = Baralho()
baralho[55] = Carta('As', 'Paus')
shuffle(baralho)
for carta in baralho:
    print carta

print baralho[0]


class Vetor():
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y


vetor1 = Vetor(1, 1)
vetor2 = Vetor(1, 1)

print vetor1 + vetor2
print vetor1 == vetor2