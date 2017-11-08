import random

from pilasengine.actores.actor import Actor

from actor.powerUp import PowerUp


class Enemigo(Actor):
    def iniciar(self, ejeX=0, ejeY=0):

        # el enemigo se ubica en las coordenadas dadas, si no se le alcanza ningun x o y este iniciara en el punto (0,0)
        self.x = ejeX
        self.y = ejeY

        # se le define una imagen al enemigo
        self.imagen = "imagenes/actor/enemigo.png"

        #se le define una velocidad al enemigo
        self.velocidad = 8

        #se le define una escala al enemigo
        self.escala = 1

        #se crean figuras de colision y se ajustan 
        self.figura = self.pilas.fisica.Circulo(self.x, self.y, 17, friccion=0, restitucion=0)
        self.figura_de_colision.escala = 3.5
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 3.5

        #se crea el comportamiento de moverse de un lado a otro
        self.actualizacion = self.pilas.tareas.siempre(1.5, self.cambiarDireccion)
        self.direccionDerecha = True

        #se le da una lista de items para que suelte cuando muera
        self.items = [PowerUp,None]


    def actualizar(self):
        self.x = self.figura.x
        self.y = self.figura.y
        self.moverse()


    def moverALaDerecha(self):
        self.figura.velocidad_x = self.velocidad
        self.rotacion -= self.velocidad
        self.espejado = True

    def moverALaIzquierda(self):
        self.figura.velocidad_x = -(self.velocidad)
        self.rotacion += self.velocidad
        self.espejado = False

    def moverse(self):
        if self.direccionDerecha:
            self.moverALaDerecha()
        else:
            self.moverALaIzquierda()

    def cambiarDireccion(self):
        self.direccionDerecha = not self.direccionDerecha


    def soltarItem(self):
        var = self.items [random.randint(0,(len(self.items) - 1) )]
        if var is not None:
            var(self.pilas,ejeX=self.x, ejeY=self.y)

    def morir(self):
        self.figura.eliminar()
        self.eliminar()
        self.soltarItem()



