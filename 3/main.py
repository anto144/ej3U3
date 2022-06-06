from manejadorequipos import manejadorEquipos
from manejadorcontrato import manejadorContratos
from manejadorjugador import manejadorJugadores
from menu import Menu

if __name__ == '__main__':
    Equipos = manejadorEquipos()
    Jugadores = manejadorJugadores()
    Contratos = manejadorContratos()
    m = Menu(Jugadores,Contratos,Equipos)

    m.opciones()