import random

class Personaje:

    def __init__(self,nombre ,vida, ataque, defensa, alcance):
        self.nombre = nombre

        if vida<1:
            raise ValueError("vida debe ser mayor que 0")
        self.vida = vida

        if ataque<1:
            raise ValueError("ataque debe ser mayor que 0")
        self.ataque = ataque

        if defensa<1:
            raise ValueError("defensa debe ser mayor que 0")
        self.defensa = defensa

        if alcance<1:
            raise ValueError("alcance debe ser mayor que 0")
        self.alcance = alcance

    def __str__(self):
        return "nombre: "+self.nombre+" vida: "+str(self.vida)+" ataque: "+str(self.ataque)+" defensa: "+str(self.defensa)+" alcance: "+str(self.alcance)

    def __delete__(self):
        del self.value


class Gestor:

    def añadir():
        nombre = input("Introducir nombre: ")
        b = random.randint(1,10)
        c = random.randint(1,10)
        d = random.randint(1,10)
        e = random.randint(1,10)
        a = Personaje(nombre,b,c,d,e)

    

    def borrar(self):
        del self

    def mostrar(self):
        print(self)

a = Personaje("Caballero",4,2,4,2)
b = Personaje("Guerrero",2,4,2,4)
c = Personaje("Arquero",2,4,1,8)



a.mostrar()
b.mostrar()
c.mostrar()

c.borrar()


a.mostrar()
b.mostrar()


