from pilasengine.actores.actor import Actor


class Jugador(Actor):
    def iniciar(self):
        self.velocidad_x = 5
        self.imagen = "imagenes/actor/player.png"
        self.escala = 1
        self.figura = self.pilas.fisica.Circulo(self.x, self.y, 17, friccion=0, restitucion=0)
        self.figura_de_colision.escala = 0

        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 3.5

        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)

    def actualizar(self):

        velocidad = 10
        salto = 20
        self.x = self.figura.x
        self.y = self.figura.y

        if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
            self.rotacion -= velocidad
            self.espejado = True
        elif self.pilas.control.izquierda:
            self.figura.velocidad_x = -velocidad
            self.rotacion += velocidad
            self.espejado = False
        else:
            self.figura.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20

        if self.esta_pisando_el_suelo():
            self.imagen = "imagenes/actor/player.png"
        else:
            self.imagen = "imagenes/actor/player.png"

        if self.x > 300:
            self.x = -300
            self.figura.x = -300

        if self.x < -300:
            self.x = +300
            self.figura.x = 300

    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0
