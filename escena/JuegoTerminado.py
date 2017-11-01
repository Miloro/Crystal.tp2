import pilasengine
from actor.plataformaConMovimiento import PlataformaCM
from actor.volverAJugar import VolverAJugar
from actor.irAlInicio import IrAlInicio

class PantallaJuegoTerminado(pilasengine.escenas.Escena):


    def iniciar(self, pilas, p):
        texto_codigo = self.pilas.actores.Texto("Juego Terminado", magnitud=40)
        texto_codigo2 = self.pilas.actores.Texto("puntaje: " + str(p) , magnitud=40)
        texto_codigo2.y = 100
        self.volverAJugar = VolverAJugar(pilas, -123 ,-123)
        self.irAlInicio = IrAlInicio(pilas, 123 , - 123)

