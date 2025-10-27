#Clase principal (Padre), representa cualquier personaje.
class Personaje:
    #Constructor
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder  #Poder de ataque o curación (depende del personaje)
        
    #Metodo para recibir daño de un ataque    
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} ha sido eliminado")
        else:
            print(f"{self.nombre} ahora tiene {self.vida} puntos de vida")
        
    def accion(self, objetivo):
        pass    #Metodo que cada subclase redefine

#Clase hija que representa una planta que puede atacar    
class PlantaAtaque(Personaje):
    def accion(self, zombi):
        print(f"{self.nombre} ha atacado a {zombi.nombre} y ha causado {self.poder} puntos de daño")
        zombi.recibir_daño(self.poder)  #Llama al método recibir_daño del zombi, aplicando el poder de la planta como daño

#Clase hija que representa un zombie que puede atacar    
class Zombi(Personaje):
    def accion(self, planta):
        print(f"{self.nombre} ha atacado a {planta.nombre} y ha causado {self.poder} puntos de daño")
        planta.recibir_daño(self.poder)

#Clase hija que representa una planta curativa      
class PlantaCurativa(Personaje):
    def accion(self, objetivo):
        if objetivo.vida <= 0:
            print(f"{self.nombre} cura a {objetivo.nombre} restaurando {self.poder} puntos de vida")
            objetivo.vida += self.poder #Aumenta la vida del objetivo usando el valor de poder
            print(f"{objetivo.nombre} ahora tiene {objetivo.vida} puntos de vida")
    
lanzaguizantes = PlantaAtaque("Lanzaguizantes", 100, 10)
zombi = Zombi("Zombi", 100, 100)
girasol = PlantaCurativa("Girasol", 100, 5)

lanzaguizantes.accion(zombi)    
lanzaguizantes.accion(zombi)

zombi.accion(lanzaguizantes)
zombi.accion(girasol)

girasol.accion(lanzaguizantes)