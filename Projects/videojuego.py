import random


def run():
    numero_ramdom = random.randint(1, 100)
    numero_de_usuario = int(input("ingresa un número del 1 al 100 : "))
    while numero_de_usuario != numero_ramdom:
        if numero_de_usuario < numero_ramdom:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_de_usuario = int(input("Elige otro número "))        
    print("¡GANASTE!")


if __name__ == "__main__":
    run()