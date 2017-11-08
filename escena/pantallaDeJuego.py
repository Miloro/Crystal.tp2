import pilasengine

from actor.jugador import Jugador
from actor.enemigo import Enemigo
from actor.pinche import Pinche
from utiles.soundPool import SoundPool
from utiles.sonido import Sonido


class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):

        pilas.fisica.eliminar_paredes()
        pilas.fisica.eliminar_suelo()
        pilas.escena.fisica.eliminar_techo()
        #self.sp = SoundPool(100)
        #self.s = Sonido("audio/menu/opcion.ogg")
        self.p = pilas
        self.mapa = pilas.actores.MapaTiled('archivo.tmx')
        self.jugador = Jugador(pilas,ejeX=-700, ejeY=270)
        self.enemigo1 = Enemigo(pilas,ejeX=400, ejeY=270)
        self.enemigo4 = Enemigo(pilas,ejeX=-190, ejeY=-33)
        self.enemigo4 = Enemigo(pilas,ejeX=-190, ejeY=-481)
        self.enemigo5 = Enemigo(pilas,ejeX=-700, ejeY=-705)
        self.ponerGrupoDePinches(-500, 207)
        self.ponerGrupoDePinches(-300, 207)

        self.ponerGrupoDePinches(280, 207)
        self.ponerGrupoDePinches(0, -720)

        pilas.colisiones.agregar('Jugador', 'Enemigo', self.morir)
        pilas.colisiones.agregar('Jugador', 'Pinche', self.morir)
        pilas.colisiones.agregar('Jugador', 'PowerUp', self.potenciarJugador)
        pilas.colisiones.agregar('Enemigo', 'Golpe' , self.matarEnemigo)

    def morir(self):
        self.p.escenas.PantallaJuegoTerminado(pilas=self.p)

    def potenciarJugador(self,jugador, powerUp):
        #self.s.reproducir("opcion","menu")
        #self.s.reproducir()
        self.jugador.potenciar()
        powerUp.eliminar()

    def matarEnemigo(self,enemigo, golpe):
        enemigo.morir()

    def ponerGrupoDePinches(self, x , y):
        self.pinche1  = Pinche(self.pilas, ejeX= x    ,  ejeY=y)
        self.pinche1  = Pinche(self.pilas, ejeX= x -35, ejeY=y)
        self.pinche1  = Pinche(self.pilas, ejeX= x -70, ejeY=y)


