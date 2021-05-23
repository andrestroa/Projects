PI = 3.1416

def cilindro(h,r,figura):    
    v = round(PI*(r**2)*h,2)
    print(f'El volumen de un {figura} es {v} m3')

def esfera(r):
    v = ((4) * PI * (r**3)/ 3)
    return round(v,2)

def prisma(h,r,figura):
    area = 2*(r**2)
    v = round(area * h,2)
    print(f'El volumen de un {figura} es de {v} m3')

def piramide(h,r,figura):
    area = 2*(r**2)
    v = round((area * h) / 3,2)
    print(f'El volumen de una {figura} es {v} m3')



def verificacion(tipo_de_figura,h,r):
    if tipo_de_figura == 1:
        cilindro(h,r,"Cilindro")        
    elif tipo_de_figura == 2:
        volumen = piramide(h,r,"Piramide")        
    elif tipo_de_figura == 3:
        volumen = esfera(r)
        print(f'El volumen de una Esfera es {volumen} m3')
    elif tipo_de_figura == 4:
        print(f'El volumen de un Cubo es de {h**3} m3')
    elif tipo_de_figura == 5:
        volumen = prisma(h,r,"Prima")        
    else:
        print('Ingrese una opción correcta')


def run():
    tipo_de_figura = int(input("""

Bienvenido, seleccione a que figura desea encontrar el volumen:

1.Cilindro
2.Piramide
3.Esfera
4.Cubo
5.Prisma cuadrangular

"""))

    h = float(input('Ingrese la altura de la figura '))
    r = float(input('Ingrese el radio de la figura '))

    verificacion(tipo_de_figura,h,r)

if __name__ == "__main__":
    run()