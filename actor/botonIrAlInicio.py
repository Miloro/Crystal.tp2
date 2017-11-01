from pilasengine.actores.actor import Actor
from escena.pantallaDeJuego import PantallaJuego


class VolverAJugar(Actor):

	def iniciar(self, x = 0, y = 0):
		self.x = x
		self.y = y
		self.imagen = "invisible.png"
		self.boton = self.pilas.actores.Boton()
		self.boton.x = self.x
		self.boton.y = self.y
		self.presionado = self.boton.conectar_presionado(self.cuando_pulsan_el_boton)
		self.sobre = self.boton.conectar_sobre(self.cuando_pasa_sobre_el_boton)
		self.normal = self.boton.conectar_normal(self.cuando_deja_de_pulsar)

	def cuando_pulsan_el_boton(self):
		self.pilas.escenas.vincular(PantallaJuego)
		self.pilas.escenas.PantallaJuego(pilas=self.pilas)
		self.pilas.avisar("")

	def cuando_pasa_sobre_el_boton(self):
		self.pilas.avisar("")

	def cuando_deja_de_pulsar(self):
		self.pilas.avisar("")