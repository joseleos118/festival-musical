
class Artista:
    GENEROS_PERMITIDOS = ["Pop", "Rock", "Electrónica", "Reguetón", "Jazz"]

    def __init__(self, nombre, genero, popularidad):
        if not self.validar_genero(genero):
            raise ValueError("Género musical no válido")

        if not self.validar_popularidad(popularidad):
            raise ValueError("La popularidad debe estar entre 1 y 100")

        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
        print(f"Bienvenido al festival, {self.nombre}")

    @property
    def popularidad(self):
        return self._popularidad

    @popularidad.setter
    def popularidad(self, valor):
        if not self.validar_popularidad(valor):
            raise ValueError("La popularidad debe estar entre 1 y 100")
        self._popularidad = valor

    @staticmethod
    def validar_genero(genero):
        return genero.lower() in [
            g.lower() for g in Artista.GENEROS_PERMITIDOS
        ]

    @staticmethod
    def validar_popularidad(popularidad):
        return isinstance(popularidad, int) and 1 <= popularidad <= 100

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y mi género es {self.genero}")

    def actuar(self):
        raise NotImplementedError

    def despedirse(self):
        print(f"Gracias por acompañarnos. Soy {self.nombre}")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Género: {self.genero}")
        print(f"Popularidad: {self.popularidad}")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def presentarse(self):
        super().presentarse()
        print("Prepárense para cantar")

    def actuar(self):
        print(
            f"{self.nombre} canta su éxito "
            f"{self.cancion_mas_popular} con gran energía."
        )


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def presentarse(self):
        super().presentarse()
        print("Que empiece la fiesta")

    def actuar(self):
        print(
            f"El DJ {self.nombre} mezcla temas de estilo "
            f"{self.estilo}, haciendo vibrar al público."
        )


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        if not isinstance(integrantes, int) or integrantes <= 0:
            raise ValueError("Los integrantes deben ser un entero positivo")

        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def presentarse(self):
        super().presentarse()
        print("Somos una banda en vivo")

    def actuar(self):
        print(
            f"La banda {self.nombre} con {self.integrantes} integrantes "
            "toca un poderoso solo de guitarra."
        )
