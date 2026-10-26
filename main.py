
from clases.artistas import Artista, Cantante, DJ, Banda


def iniciar_festival(lista_artistas):
    print("BIENVENIDOS AL FESTIVAL")
    print("=" * 40)

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación")
        print("=" * 40)


def main():
    artistas = []

    while True:
        try:
            cantidad = int(input("¿Cuántos artistas se presentarán? "))
            if cantidad > 0:
                break
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Introduce un número entero válido.")

    for i in range(cantidad):
        print(f"\nArtista {i + 1}")

        while True:
            tipo = input("Tipo (Cantante, DJ o Banda): ").strip().lower()
            if tipo in ["cantante", "dj", "banda"]:
                break
            print("Tipo de artista no válido.")

        nombre = input("Nombre: ").strip()

        while not nombre:
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre: ").strip()

        while True:
            genero = input("Género (Pop, Rock, Electrónica, Reguetón o Jazz): ").strip()
            if Artista.validar_genero(genero):
                break
            print("Género no válido.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if Artista.validar_popularidad(popularidad):
                    break
                print("La popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Introduce un número entero.")

        try:
            if tipo == "cantante":
                cancion = input("Canción más popular: ").strip()
                artista = Cantante(nombre, genero, popularidad, cancion)

            elif tipo == "dj":
                estilo = input("Estilo musical: ").strip()
                artista = DJ(nombre, genero, popularidad, estilo)

            else:
                while True:
                    try:
                        integrantes = int(input("Número de integrantes: "))
                        if integrantes > 0:
                            break
                        print("Debe ser un número entero positivo.")
                    except ValueError:
                        print("Introduce un número entero.")

                artista = Banda(nombre, genero, popularidad, integrantes)

            artistas.append(artista)

        except ValueError as error:
            print(f"Error: {error}")
            print("Vuelve a ejecutar el programa para registrar al artista.")

    iniciar_festival(artistas)


if __name__ == "__main__":
    main()
