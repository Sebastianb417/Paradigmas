class Jugador:
    def __init__(self, nombre, edad, posicion, goles=0):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.goles = goles
        

    def anotar(self, cantidad=1):
        self.goles += cantidad
        print(f"{self.nombre} anotó {cantidad} gol(es). Total: {self.goles}")

    def transfer(self, nuevo_equipo):
        print(f"{self.nombre} ha sido transferido al equipo {nuevo_equipo}.")




class Entrenador:
    def __init__(self, nombre, años_experiencia):
        self.nombre = nombre
        self.años_experiencia = años_experiencia

    def dar_instrucciones(self):
        print(f"{self.nombre} dice: ¡JUEGUEN  QUE NO COPEAMOS !")




jugador1 = Jugador("carlos", 20, "Delantero")
jugador1.anotar(3)
jugador1.anotar(2)
jugador1.transfer("COLOMBIA")

entrenador1 = Entrenador("Fabio", 10)
entrenador1.dar_instrucciones()