from pilasengine.actores.actor import Actor


class Golpe(Actor):

    def iniciar(self,ejeX=0, ejeY=0):
        self.x = ejeX
        self.y = ejeY
        self.imagen = "invisible.png"




