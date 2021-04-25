def run():
    tu_nombre = input("Cual es tú nombre? ")
    saludo = len(tu_nombre)
    print("Hola " + tu_nombre + " tú nombre tiene " + str(saludo) + " letras")


if __name__ == "__main__":
    run()