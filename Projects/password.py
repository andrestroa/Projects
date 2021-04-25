import random


def password_generetor():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    numeros = ["1", "2", "3", "4", "5", "6", "7"]
    caracteres = ["!", "#", "$", "%", "&", "/", "("]

    build_password = mayusculas + minusculas + numeros + caracteres

    new_password = []

    for i in range(15):
        password_ramdom = random.choice(build_password)
        new_password.append(password_ramdom)

    new_password = "".join(new_password)
    return new_password
    

def run():
    new_password = password_generetor()
    print("Tú nueva contraseña es" + new_password)

if __name__ == "__main__":
    run()