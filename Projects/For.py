def tabla(numero):
    print('Esta es la tabla del ' + str(numero))
    for i in range(0,13):
        print(i*numero) 


def run():
    menu = """
Esta es una tabla de multiplicar, selecciona una opción

    a. Tabla del 1
    b. Tabla del 2
    c. Tabla del 3
    d. Tabla del 4
    e. Tabla del 5
    f. Tabla del 6
    g. Tabla del 7
    h. Tabla del 8
    i. Tabla del 9
    j. Tabla del 10
    k. Tabla del 11
    l. Tabla del 12
    
        """
        
    opción = str(input(menu))

    if opción == 'a':
        tabla(2)
    elif opción == 'b':
        tabla(3)       
    elif opción == 'c':
        tabla(4)
    elif opción == 'd':
        tabla(5)
    elif opción == 'e':
        tabla(6)
    elif opción == 'f':
        tabla(7)
    elif opción == 'g':
        tabla(8)
    elif opción == 'h':
        tabla(9)
    elif opción == 'i':
        tabla(10)
    elif opción == 'j':
        tabla(11)
    elif opción == 'k':
        tabla(12)
    elif opción == 'l':
        tabla(13)

    else:
        print:('Porfavor selecciona una opción correcta')

if __name__ == '__name__':
    run()