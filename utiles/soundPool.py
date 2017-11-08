#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# daiyuki rts
#
# Copyright 2017 - Miguel Barraza
# licencia: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

from .sonido import Sonido

class SoundPool(object):
    """Pool que gestiona todo los sonidos del juego"""

    def __init__(self, cantidadDeSonidos=100):
        self.cantidadDeSonidos = cantidadDeSonidos
        self.sounds = dict()
        self.x = 0
        self.lista = [None]*cantidadDeSonidos

    def reproducir(self, nombre, tipo):
        """carga y reproduce un sonido"""
        self.lista[self.x] = Sonido("audio/"+tipo+"/"+nombre+".ogg")
        self.lista[self.x].reproducir()
        self.x = (self.x+1)%self.cantidadDeSonidos
