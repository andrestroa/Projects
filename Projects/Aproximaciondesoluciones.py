def run():
    objetivo = int(input("Escribe un número :" ))
    epsilon = 0.1
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta, paso)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro raiz cuadrada')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if  __name__ == "__main__":
    run()