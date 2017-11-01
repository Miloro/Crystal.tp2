import pilasengine
from actor.fondo import Fondo
from pilasengine.actores.actor import Actor
from actor.volverAJugar import VolverAJugar

class Inicio(pilasengine.escenas.Escena):

	def iniciar(self, pilas):


		texto_codigo = self.pilas.actores.Texto( "Crystal y sus Desventuras", magnitud=30,x=0,y=123)
		texto_codigo.color = pilas.colores.Color(0, 0, 0)
		fondo = Fondo(pilas)
 		self.volverAJugar = VolverAJugar(pilas, 0 ,-123)


