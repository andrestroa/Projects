import os
from math import sqrt,asin,cos,ceil
from typing import NamedTuple

def area(b,h):
    #Encuentra el area del triangulo
    A = (b * h)/ 2
    print(f'Esta es la area {A} del triangulo')

def tipo_de_triangulo(b,h):
    #Creo un triangulo rectangulo con la base y la altura para sacar un lado
    lado_derecho = ceil((sqrt(((sqrt(b))**2) + (h**2))))
    #Utilizo el arcoseno para sacar el angulo del triangulo rectangulo
    angulo_de_triangulo = asin(h/lado_derecho)
    #Con los valores anteriores se saca el lado faltante
    lado_izquierdo = ceil((sqrt(b**2 + lado_derecho**2 - 2 * b * lado_derecho * (cos(angulo_de_triangulo)))))
    #Se hace la comparación de lados para saber la clase de triangulo
    if lado_derecho == lado_izquierdo == b:
        print('Este es un triangulo equilátero ')
    elif lado_derecho == lado_izquierdo != b or lado_derecho == b != lado_izquierdo or b == lado_izquierdo != b:
        print('Este es un triangulo isóceles')
    else:
        print('Este es un triangulo escaleno')
    

def run():
    os.system("cls")
    b = round(float(input('Ingrese la base del triangulo: ')))
    h = float(input('Ingrese la altura del triangulo: '))
    area(b,h)
    tipo_de_triangulo(b,h)


if __name__ == '__main__':
    run()


    