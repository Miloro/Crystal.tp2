import random

import pilasengine
from actor.volverAJugar import VolverAJugar

class PantallaJuegoTerminado(pilasengine.escenas.Escena):


    def iniciar(self, pilas):
        self.frasesDeMuerte= [
        "Para un enano morir en la guerra es glorioso, pero morir en una demo es patetico",
        " \"Trom juratron gua mortac\" en humano significa: como puede ser que una criatura de \n                             tal calibre pueda matarme de un solo golpe",
        "El glorioso imperio enano fue destruido por unos enemigos tan pateticos que ni el\n                             creador del juego le dio amor a sus sprites",
        "Mi vieja mula ya no es lo que era ya no es lo que era",
        "Oviamente fue culpa de teclado no te preocupes campeon"
        ]
        texto_codigo = self.pilas.actores.Texto("Juego Terminado")
        texto_codigo2 = self.pilas.actores.Texto(self.frasesDeMuerte [random.randint(0,4)])
        texto_codigo2.escala = 0.5
        texto_codigo.y = 100
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.activar_menu_principal)


    def activar_menu_principal(self, evento):
        self.pilas.escenas.PantallaJuego(pilas=self.pilas)




