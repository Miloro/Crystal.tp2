import pilasengine


class CDE():

	def __init__(self, pilas):
		self.pilas = pilas 


	def iniciar(self):
		self.imagen = "invisible.png"


	def irAlInicio(self):
		self.pilas.escenas.Inicio(pilas=self.pilas)

	def irALaPantallaDelJuego(self):
		self.pilas.escenas.PantallaJuego(pilas=self.pilas)

	def irALaPantallaPerder(self,puntos):
		self.pilas.escenas.PantallaJuegoTerminado(pilas=self.pilas, p = puntos)