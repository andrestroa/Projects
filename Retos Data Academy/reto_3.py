KM = 0.621371 #Km a Milla
MILLA = 1.609344 #Milla a Km


def conversor(usuario):
    if usuario == 1:
        unidad = float(input('Ingrese la distancia que quiere convertir '))
        resultado = unidad * KM
        print(f'{unidad} Milla(s) a Km(s) son {resultado} Milla(s)')        
    elif usuario == 2:
        unidad = float(input('Ingrese la distancia que quiere convertir '))
        resultado = unidad * MILLA
        print(f'{unidad} Km(s) a Milla(s) son {resultado} Km(s)')

    else:
        print('Ingrese una opción correcta')



def run():
    usuario = int((input(""" 

Bienvenido, que tipo de medida quieres cambiar:

1.Millas a kilómetros
2.Kilómetros a Millas

""")))
    conversor(usuario)

if __name__ == "__main__":
    run()