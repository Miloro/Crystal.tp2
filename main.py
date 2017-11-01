import pilasengine
from escena.MenuPrincipal import Inicio
from escena.JuegoTerminado import PantallaJuegoTerminado
from escena.pantallaDeJuego import PantallaJuego

pilas = pilasengine.iniciar(titulo='Crystal - alpha', habilitar_mensajes_log=False)




pilas.escenas.vincular(PantallaJuegoTerminado)
pilas.escenas.vincular(PantallaJuego)
pilas.escenas.vincular(Inicio)
pilas.escenas.PantallaJuego(pilas=pilas)
pilas.ejecutar()