from pilasengine.actores.actor import Actor


class PlataformaCM(Actor):

    def iniciar(self, d = 1):
      self.dificultad = d
      self.x = self.pilas.azar(-250, 250)
      self.imagen = "imagenes/actor/plataforma.png"
      self.escala = 1 - (self.dificultad * 0.01)
      self.figura = self.pilas.fisica.Rectangulo(self.x,30,30,30,False,self.x,self.y,30,30,True,False,True)
      self.figura.escala = 1 - (self.dificultad * 0.01)
 


    def actualizar(self):
        self.figura.y = self.y
        self.y = self.y - (1.3 + (self.dificultad * 0.01))
        if self.y < -400:
          self.eliminar()