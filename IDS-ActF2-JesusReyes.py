class Personaje:
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} ha sido eliminado")
        else:
            print(f"{self.nombre} ahora tiene {self.vida} puntos de vida")
        
    def accion(self, objetivo):
        pass
    
class PlantaAtaque(Personaje):
    def atacar(self, zombi):
        print(f"{self.nombre} ha atacado a {zombi.nombre} y ha causado {self.poder} puntos de daño")
        zombi.recibir_daño(self.poder)

class Zombi(Personaje):
    def atacar(self, planta):
        print(f"{self.nombre} ha atacado a {planta.nombre} y ha causado {self.poder} puntos de daño")
        planta.recibir_daño(self.poder)
        
class PlantaCurativa(Personaje):
    def accion(self, objetivo):
        print(f"{self.nombre} cura a {objetivo.nombre} restaurando {self.poder} puntos de vida")
        objetivo.vida += self.poder
        print(f"{objetivo.nombre} ahora tiene {objetivo.vida} puntos de vida")
    
lanzaguizantes = PlantaAtaque("Lanzaguizantes", 100, 10)
zombi = Zombi("Zombi", 100, 10)
girasol = PlantaCurativa("Girasol", 100, 5)

lanzaguizantes.accion(zombi)    
lanzaguizantes.atacar(zombi)

zombi.accion(lanzaguizantes)
zombi.atacar(lanzaguizantes)
zombi.atacar(girasol)


girasol.accion(lanzaguizantes)