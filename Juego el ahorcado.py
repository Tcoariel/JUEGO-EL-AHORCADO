import random

def elegir_palabra():
    palabras = ["manzana", "banana", "pera", "uva"]
    return random.choice(palabras)

def jugar():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    juego_terminado = False

    while intentos > 0 and not juego_terminado==True:
        palabra_oculta = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += "_"
        print(palabra_oculta)

        if "_" not in palabra_oculta:
            print("¡Felicidades! Has adivinado la palabra:", palabra)
            juego_terminado = True
            continue

        letra = input("Introduce una letra: ").lower()

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Correcto!")
        else:
            intentos -= 1
            print("¡Incorrecto! Te quedan", intentos, "intentos.")

    if "_" in palabra_oculta:
        print("¡Has perdido! La palabra era:", palabra)

jugar()