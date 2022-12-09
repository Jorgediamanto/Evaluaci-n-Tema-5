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


class Gestor:

    def añadir():
        pass

    def borrar():
        pass

    def mostrar():
        pass