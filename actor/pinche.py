import random

from pilasengine.actores.actor import Actor

from actor.powerUp import PowerUp


class Pinche(Actor):
    def iniciar(self, ejeX=0, ejeY=0):
        self.x = ejeX
        self.y = ejeY
        self.imagen = "imagenes/actor/pinche.png"
        self.figura_de_colision.escala = 2

