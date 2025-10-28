import random

# CLASE BASE: Personaje
class Personaje:
    """
    Clase base que representa un persoanje del juego.
    Puede ser una planta o un zombi.
    
    Atributos:
        nombre (str): nombre del personaje
        vida (int): vida del personaje
        poder (int): poder de ataque o curación
        vida_maxima (int): vida maxima del personaje
    """
    def __init__(self, nombre, vida, poder):
        """
        Inicializa un personaje con nombre, vida y poder
        """
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        self.vida_maxima = vida
        
      
    def recibir_daño(self, daño):
        """
        Reduce la vida del personaje según el daño recibido
        Imprime el estado del personaje despues de ataque
        
        Args:
            daño (int): puntos de daño que recibirá el personaje
        """
        self.vida -= daño
        if self.vida <= 0:
            print(f"{self.nombre} ha sido eliminado")
        else:
            print(f"{self.nombre} ahora tiene {self.vida} puntos de vida")
        
    def accion(self, objetivo):
        """
        Método génerico de acción que será redefinido por las subclases
        """
        pass
    
    def estado_vivo(self):
        """
        Verifica si el personaje está vivo.

        Returns:
            bool: True si la vida es mayor a 0, de lo contrario muestra un mensaje y retorna False.
        """
        if self.vida > 0:
            return True
        else:
            print(f"{self.nombre} ha sido eliminado y no puede realizar ninguna acción")
            return False
             
                

# CLASE HIJA: PlantaAtaque
class PlantaAtaque(Personaje):
    """
    Representa una planta que puede atacar a los zombis
    """
    def accion(self, zombi):
        """
        Ataca a un zombi si esta vivo

        Args:
            zombi (Zombi): objeto Zombi que será atacado
        """
        if zombi.vida <= 0:
            print(f"{zombi.nombre} ya ha sido eliminado y no se puede atacar")
        else:
            print(f"{self.nombre} ha atacado a {zombi.nombre} y ha causado {self.poder} puntos de daño")
            zombi.recibir_daño(self.poder)  #Llama al método recibir_daño del zombi, aplicando el poder de la planta como daño

# CLASE HIJA: Zombi   
class Zombi(Personaje):
    """
    Representa un zombi que puede atacar a las plantas.
    """
    def accion(self, planta):
        """
        Ataca a una planta si está viva.

        Args:
            planta (PlantaAtaque o PlantaCurativa): planta objetivo del ataque
        """
        if planta.vida <= 0:
            print(f"{planta.nombre} ya ha sido eliminado y no se puede atacar")
        else:
            print(f"{self.nombre} ha atacado a {planta.nombre} y ha causado {self.poder} puntos de daño")
            planta.recibir_daño(self.poder)

# CLASE HIJA: ZombiFuerte        
class ZombiFuerte(Zombi):
    """
    Zombi que causa daño extra.
    Puede causar daño crítico (daño doble).
    """
    def __init__(self, nombre, vida, poder):
        """
        Inicializa un zombi fuerte y determina si su ataque será crítico.

        Args:
            nombre (str): nombre del zombi
            vida (int): vida del zombi
            poder (int): poder de ataque base
        """
        super().__init__(nombre, vida, poder)
        if random.randint(0, 1) % 2 == 0:
            self.poder += 5
        else:
            self.poder *= 2
            self.daño_critico = True
    
    def accion(self, planta):
        """
        Realiza ataque al objetivo e imprime mensaje de daño crítico si aplica.

        Args:
            planta (PlantaAtaque o PlantaCurativa): objetivo del ataque
        """
        if getattr(self, "daño_critico", False): # "getattr" Busca self.daño_critico, si no existe devuelve False y no da error
            print("Daño critico!")
        super().accion(planta)

# CLASE HIJA: ZombiRegenerativo        
class ZombiRegenerativo(Zombi):
    """
    Zombi que se regenera después de atacar.
    """
    def __init__(self, nombre, vida, poder):
        """
        Inicializa un zombi regenerativo con poder de regeneración.

        Args:
            nombre (str): nombre del zombi
            vida (int): vida del zombi
            poder (int): poder de ataque
        """
        super().__init__(nombre, vida, poder)
        self.regeneracion = 5
    
    def accion(self, planta):
        """
        Realiza un ataque y se regenera después, sin superar la vida máxima.

        Args:
            planta (PlantaAtaque o PlantaCurativa): objetivo del ataque
        """
        super().accion(planta)
        self.vida += self.regeneracion
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima
            print(f"{self.nombre} ha intetado curarse, pero ya tiene la vida maxima")
        else:
            print(f"{self.nombre} ha regenerado vida con el ataque y ahora tiene {self.vida} puntos de vida")
        


# CLASE HIJA: PlantaCurativa   
class PlantaCurativa(Personaje):
    """
    Planta que cura otras plantas.
    """
    def accion(self, objetivo):
        """
        Cura al objetivo si está vivo y no supera su vida máxima.

        Args:
            objetivo (PlantaAtaque o PlantaCurativa): planta objetivo de la curación
        """
        if objetivo.vida > 0:
            objetivo.vida += self.poder #Aumenta la vida del objetivo usando el valor de poder
            if objetivo.vida > objetivo.vida_maxima: 
                objetivo.vida = objetivo.vida_maxima
                print(f"{self.nombre} ha intetado curar a {objetivo.nombre}, pero ya tiene la vida maxima y no puede ser curado")
            else:
                print(f"{self.nombre} cura a {objetivo.nombre} restaurando {self.poder} puntos de vida")
                print(f"{objetivo.nombre} ahora tiene {objetivo.vida} puntos de vida")
   
# CREACIÓN DE PERSONAJES    
lanzaguizantes = PlantaAtaque("Lanzaguizantes", 100, 100)
zombi = Zombi("Zombi", 100, 10)
zombifuerte = ZombiFuerte("Zombi Fuerte", 100, 10)
zombiregenerativo = ZombiRegenerativo("Zombi Regenerativo", 100, 5)
girasol = PlantaCurativa("Girasol", 100, 5)


# SIMULACIÓN DE ACCIONES
lanzaguizantes.accion(zombi)    
lanzaguizantes.accion(zombi)
zombi.accion(lanzaguizantes)
zombi.accion(girasol)
zombifuerte.accion(girasol)
zombiregenerativo.accion(girasol)
girasol.accion(lanzaguizantes)
