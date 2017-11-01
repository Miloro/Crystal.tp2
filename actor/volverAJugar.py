from pilasengine.actores.actor import Actor
from logica.cde import CDE

class VolverAJugar(Actor):

	def iniciar(self, x = 0, y = 0):
		self.cde = CDE(self.pilas)
		self.x = x
		self.y = y
		self.imagen = "invisible.png"
		self.boton = self.pilas.interfaz.Boton("jugar")
		self.boton.x = self.x
		self.boton.y = self.y
		self.boton.conectar(self.cuandoPulsanElBoton)


	def cuandoPulsanElBoton(self):
		self.cde.irALaPantallaDelJuego()


