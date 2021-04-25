def run():
    raiz = int(input("Ingresa un número : "))
    respuesta = 0
    
    while respuesta**2 < raiz:
            respuesta += 1
            print(respuesta)

    if respuesta**2 == raiz:
        print("La raiz cuadrada de " + str( raiz) + " es " + str( respuesta))
    else:
        print(str(raiz) + " no tiene una raiz cuadrada")

if  __name__ == "__main__":
    run()
