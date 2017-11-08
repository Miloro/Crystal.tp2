import pilasengine
from escena.JuegoTerminado import PantallaJuegoTerminado
from escena.pantallaDeJuego import PantallaJuego
from actor.jugador import Jugador
from actor.enemigo import Enemigo
from actor.powerUp import PowerUp
from actor.golpe import Golpe
from actor.pinche import Pinche




pilas = pilasengine.iniciar(titulo='Crystal - alpha', habilitar_mensajes_log=False)

pilas.escenas.vincular(PantallaJuegoTerminado)
pilas.escenas.vincular(PantallaJuego)
pilas.actores.vincular(Jugador)
pilas.actores.vincular(Enemigo)
pilas.actores.vincular(PowerUp)
pilas.actores.vincular(Pinche)
pilas.actores.vincular(Golpe)

pilas.escenas.PantallaJuego(pilas=pilas)
pilas.ejecutar()