from pilasengine.actores.actor import Actor
from actor.golpe import Golpe

class Jugador(Actor):
    def iniciar(self, ejeX=0, ejeY=0):
        self.animacion = self.pilas.imagenes.cargar_animacion("imagenes/actor/jugadorGrilla.png", 20)
        self.imagen = self.animacion
        self.x = ejeX
        self.y = ejeY
        self.direccion = 1
        self.velocidad = 10
        self.escala = 1
        self.figura = self.pilas.fisica.Circulo(self.x, self.y, 30, friccion=0, restitucion=0)
        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 30, 5, sensor=True, dinamica=False)
        self.figura_de_colision.escala = 1.8
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 3.5
        self.powerUp = None
        self.enfriamiento = None
        self.puedoPegar = True
        self.animacion.definir_animacion('parado', [0, 1, 2 , 3], 6)
        self.animacion.definir_animacion('caminar', [4 ,5, 6, 7, 8, 9], 15)
        self.animacion.definir_animacion('saltando', [5], 1)
        self.animacion.definir_animacion('golpeando',[11,12,13,14,10], 10)
        self.alturaSalto = 60


    def actualizar(self):
        self.imagen.avanzar()
        self.x = self.figura.x
        self.y = self.figura.y
        self.pilas.camara.x = self.x
        self.pilas.camara.y = self.y

        if self.pilas.control.derecha and not(self.pilas.control.boton):
             self.moverALaDerecha()
        elif self.pilas.control.izquierda and not(self.pilas.control.boton):
             self.moverALaIzquierda()
        elif self.pilas.control.boton:
            if self.puedoPegar:
                self.puedoPegar = False
                self.golpe = Golpe(self.pilas,self.x +(self.direccion * 30) , self.y)
                self.enfriamiento = self.pilas.tareas.agregar(0.1, self.terminarCoolddown,self.golpe)
                self.figura.velocidad_x = 0
                self.imagen.cargar_animacion('golpeando')


        else:
            self.figura.velocidad_x = 0
            self.imagen.cargar_animacion('parado')

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, self.alturaSalto)


        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 35


    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

    def moverALaDerecha(self):
        self.imagen.cargar_animacion('caminar')
        self.figura.velocidad_x = self.velocidad
        self.espejado = True
        self.mirandoALaDerecha = True
        self.direccion = 1

    def moverALaIzquierda(self):
        self.imagen.cargar_animacion('caminar')
        self.figura.velocidad_x = -(self.velocidad)
        self.espejado = False
        self.mirandoALaDerecha = False
        self.direccion = -1

    def potenciar(self):
        if self.powerUp is not None:
            self.powerUp.terminar()
            self.powerUp = None
        self.velocidad = 20
        self.alturaSalto = 100
        self.powerUp = self.pilas.tareas.agregar(10, self.normalizar)

    def normalizar(self):
        self.velocidad = 10
        self.alturaSalto = 60
        self.powerUp.terminar()
        self.powerUp = None

    def terminarCoolddown(self,golpe):
        golpe.eliminar()
        self.puedoPegar = True
        #self.enfriamiento = None






