def conversor(Tipo_peso, Valor_Dolar):
    Pesos = input("¿Cuántos pesos" + Tipo_peso + "Colombianos tiene?: ")
    Pesos = float(Pesos)
    Dolares = Pesos / Valor_Dolar
    Dolares = round(Dolares,2)
    Dolares = str(Dolares)
    print("Tienes $" + Dolares + " Dolares")

Menu = """
Bienvenido al conversor de monedas 💲

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Escoge una opción: """

opcion = input(Menu)


if opcion == "1":
    conversor("Colombianos", 3875)
elif opcion == "2":
    conversor("Argentinos", 65)
elif opcion == "3":
    conversor("Mexicanos", 24)
else: 
     print("ingresa una opción correcta")



