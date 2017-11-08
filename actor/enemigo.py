import random

from pilasengine.actores.actor import Actor

from actor.powerUp import PowerUp


class Enemigo(Actor):
    def iniciar(self, ejeX=0, ejeY=0):
        self.x = ejeX
        self.y = ejeY
        self.velocidad_x = 0.1
        self.imagen = "imagenes/actor/enemigo.png"
        self.escala = 1
        self.figura = self.pilas.fisica.Circulo(self.x, self.y, 17, friccion=0, restitucion=0)
        self.figura_de_colision.escala = 3.5
        self.velocidad = 8
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 3.5
        self.actualizacion = self.pilas.tareas.siempre(1.5, self.cambiarDireccion)
        self.direccionDerecha = True
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
        var = self.items [random.randint(0,1)]
        if var is not None:
            var(self.pilas,ejeX=self.x, ejeY=self.y)

    def morir(self):
        self.actualizacion.terminar()
        self.figura.eliminar()
        self.eliminar()
        self.soltarItem()



