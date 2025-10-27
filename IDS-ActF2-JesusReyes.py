import random

#Clase principal (Padre), representa cualquier personaje.
class Personaje:
    #Constructor
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder  #Poder de ataque o curación (depende del personaje)
        self.vida_maxima = vida
        
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
        if zombi.vida <= 0:
            print(f"{zombi.nombre} ya ha sido eliminado y no se puede atacar")
        else:
            print(f"{self.nombre} ha atacado a {zombi.nombre} y ha causado {self.poder} puntos de daño")
            zombi.recibir_daño(self.poder)  #Llama al método recibir_daño del zombi, aplicando el poder de la planta como daño

#Clase hija que representa un zombie que puede atacar    
class Zombi(Personaje):
    def accion(self, planta):
        if planta.vida <= 0:
            print(f"{planta.nombre} ya ha sido eliminado y no se puede atacar")
        else:
            print(f"{self.nombre} ha atacado a {planta.nombre} y ha causado {self.poder} puntos de daño")
            planta.recibir_daño(self.poder)
        
class ZombiFuerte(Zombi):
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)
        if random.randint(0, 1) % 2 == 0:
            self.poder += 5
        else:
            self.poder *= 2
            self.daño_critico = True
    
    def accion(self, planta):
        if getattr(self, "daño_critico", False): # "getattr" Busca self.daño_critico, si no existe devuelve False y no da error
            print("Daño critico!")
        super().accion(planta)
        
class ZombiRegenerativo(Zombi):
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)
        self.regeneracion = 5
    
    def accion(self, planta):
        super().accion(planta)
        self.vida += self.regeneracion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
            print(f"{self.nombre} ha intetado curarse, pero ya tiene la vida maxima")
        else:
            print(f"{self.nombre} ha regenerado vida con el ataque y ahora tiene {self.vida} puntos de vida")
        


#Clase hija que representa una planta curativa      
class PlantaCurativa(Personaje):
    def accion(self, objetivo):
        if objetivo.vida > 0:
            objetivo.vida += self.poder #Aumenta la vida del objetivo usando el valor de poder
            if objetivo.vida > objetivo.vida_maxima: 
                objetivo.vida = objetivo.vida_maxima
                print(f"{self.nombre} ha intetado curar a {objetivo.nombre}, pero ya tiene la vida maxima y no puede ser curado")
            else:
                print(f"{self.nombre} cura a {objetivo.nombre} restaurando {self.poder} puntos de vida")
                print(f"{objetivo.nombre} ahora tiene {objetivo.vida} puntos de vida")
    
lanzaguizantes = PlantaAtaque("Lanzaguizantes", 100, 100)
zombi = Zombi("Zombi", 100, 10)
zombifuerte = ZombiFuerte("Zombi Fuerte", 100, 10)
zombiregenerativo = ZombiRegenerativo("Zombi Regenerativo", 100, 5)
girasol = PlantaCurativa("Girasol", 100, 5)



lanzaguizantes.accion(zombi)    
lanzaguizantes.accion(zombi)
zombi.accion(lanzaguizantes)
zombi.accion(girasol)
zombifuerte.accion(girasol)
zombiregenerativo.accion(girasol)
girasol.accion(lanzaguizantes)