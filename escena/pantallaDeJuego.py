import pilasengine
from actor.jugador import Jugador
from actor.plataforma import Plataforma
from actor.puntaje import Puntaje
from actor.plataformaConMovimiento import PlataformaCM
from logica.cde import CDE

class PantallaJuego(pilasengine.escenas.Escena):

    def iniciar(self, pilas):
        #self.grilla = pilas.imagenes.cargar_grilla("imagenes/esenario/plataformas_10_10.png",100,100)
        #self.mapa = pilas.actores.Mapa(grilla=self.grilla)
        self.mapa = pilas.actores.MapaTiled('archivo.tmx')
        self.cde = CDE(self.pilas)
        self.jugador = Jugador(pilas)

    #def crearPlataformas(self):
    #	plataformaCM = PlataformaCM(self.pilas,  self.puntaje.puntos )
    #    plataformaCM.y = 300

    #def perder(self):
    #    if(self.jugador.y <= -220):
    #        print("perdiste guchin")
    #        self.cde.irALaPantallaPerder(self.puntaje.puntos)
