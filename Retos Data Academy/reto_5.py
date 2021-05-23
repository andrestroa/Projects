def validacion(lim_inferior, lim_superior, comparacion):
    
    while True:
        if lim_inferior > comparacion or lim_superior < comparacion:
            print(comparacion)
            comparacion = int(input('Ingrese otro número '))
            validacion(lim_inferior, lim_superior, comparacion)
        else:
            print(comparacion)
        break

def run():
    lim_inferior = int(input('Ingrese el limite inferior '))
    lim_superior = int(input('Ingrese el limite superior '))
    comparacion = int(input('Ahora ingrese un número '))

    validacion(lim_inferior, lim_superior, comparacion)


if __name__ == '__main__':
    run()