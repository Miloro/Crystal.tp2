from pilasengine.actores.actor import Actor

class Fondo(Actor):

	def iniciar(self):
		self.imagen = "invisible.png"
		self.fondo = self.pilas.actores.Actor()
		self.fondo.figura_de_colision.escala = 0
		self.fondo.imagen = "imagenes/fondo/ladrillo3.jpg"
		self.fondo.z = 200
		self.fondo.imagen.repetir_horizontal = True
		self.fondo.imagen.repetir_vertical = True
		self.tarea = self.pilas.tareas.siempre(1/90.0, self.mover_fondo)

	def mover_fondo(self):
		self.fondo.y -= 1
