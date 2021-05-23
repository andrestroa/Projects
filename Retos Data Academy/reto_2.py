import random
import os


opciones = {1:"Piedra",2:"Papel",3:"Tijeras"}

def verificacion_de_ganador(decision_usuario,opcion_de_pc,resultado):
    datos = {"usuario":decision_usuario,"pc":opcion_de_pc}
    if resultado == 4 or resultado == 3:
        ganador = min(datos, key=lambda key: datos[key])
    elif resultado == 5:
        ganador = max(datos, key=lambda key: datos[key])
    
    return ganador


    

def decision_pc():
    return random.randint(1,3)

def juego():
    puntos_pc = 0
    puntos_usuario = 0
    ganador = False

    

    while ganador == False:
        if puntos_pc == 2 or puntos_usuario == 2:
            ganador = True
        else:
            decision_usuario = int(input('Ingrese una opción '))
            opcion_de_pc = decision_pc()
            if decision_usuario == opcion_de_pc:
                print('Empate, nadie gana puntos')         
            elif (decision_usuario + opcion_de_pc) == 4:
                resultado = 4
                winner = verificacion_de_ganador(decision_usuario,opcion_de_pc,resultado)
                if winner == "pc":
                    puntos_pc += 1
                    print(f'Punto para la PC, {opciones[opcion_de_pc]} gana a {opciones[decision_usuario]}')               
                else:
                    puntos_usuario += 1
                    print(f'Punto para el usuario, {opciones[decision_usuario]} gana a {opciones[opcion_de_pc]}')               
            elif (decision_usuario + opcion_de_pc) == 3:
                resultado = 3
                winner = verificacion_de_ganador(decision_usuario,opcion_de_pc,resultado)
                if winner == "pc":
                    puntos_pc += 1
                    print(f'Punto para la PC, {opciones[opcion_de_pc]} gana a {opciones[decision_usuario]}')               
                else:
                    puntos_usuario += 1
                    print(f'Punto para el usuario, {opciones[decision_usuario]} gana a {opciones[opcion_de_pc]}')                      
                
            elif (decision_usuario + opcion_de_pc) == 5:
                resultado = 5
                winner = verificacion_de_ganador(decision_usuario,opcion_de_pc,resultado)
                if winner == "pc":
                    puntos_pc += 1
                    print(f'Punto para la PC, {opciones[opcion_de_pc]} gana a {opciones[decision_usuario]}')               
                else:
                    puntos_usuario += 1
                    print(f'Punto para el usuario, {opciones[decision_usuario]} gana a {opciones[opcion_de_pc]}')                           
                
    if puntos_pc == 2:
        print(f'El ganador es la PC, usuario = {puntos_usuario} PC = {puntos_pc}')
    else:
        print(f'El ganador es el usuario,usuario = {puntos_usuario} PC = {puntos_pc} ')


    if puntos_pc == 2:
        print('La pc gano')
    else:
        print('Felicidades ganaste')
    

def run():
    os.system("cls")
    print("""
Bienvenido al juego de Piedra, Papel y Tijera,las reglas son simples, compites contra la PC, debes seleccionar una de las siguientes opciones:
1.Piedra
2.Papel
3:Tijera
Son 3 rondas, gana el que acumule 2 puntos""")
    juego()

if __name__ == '__main__':
    run()