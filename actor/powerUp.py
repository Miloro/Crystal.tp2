from pilasengine.actores.actor import Actor


class PowerUp(Actor):
    def iniciar(self, ejeX=0, ejeY=0):
        self.x = ejeX
        self.y = ejeY
        self.imagen = "imagenes/actor/powerUp.png"



