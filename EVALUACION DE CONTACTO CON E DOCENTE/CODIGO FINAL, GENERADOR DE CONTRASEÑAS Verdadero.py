import random

letras = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%&*()_+-=´´<>?,./'

print("Bienvenido al generador de contraseñas")

nm_letras = int(input("¿Cuantas letras quieres en tu clave?"))
nm_numeros = int(input("¿Cuantos numeros quieres en tu clave?"))
nm_simbolos = int(input("¿Cuantos simbolos quieres en tu clave?"))

lista_letras = [random.choice(letras) for _ in range(nm_letras)]
lista_numeros =[random.choice(numeros) for _ in range(nm_numeros)]
lista_simbolos = [random.choice(simbolos) for _ in range(nm_simbolos)]

lista_contraseña = lista_letras + lista_numeros + lista_simbolos
random.shuffle(lista_contraseña)
print("Tu contraseña es: ", ''.join(lista_contraseña), "Quieres que esta sea tu contraseña?")
respuesta = input("Si o No:")
if respuesta.lower() == "si":
    print("Tu contraseña ha sido guardada")
    print("Tienes 5 intentos para introducir tu contraseña")
    contador = 1
    correcta = ''.join(lista_contraseña)
    while contador <= 5:
        contraseña_usuario = input("Introduce tu contraseña: ")
        if contraseña_usuario == correcta:
            print("Contraseña correcta, bienvenido")
            break
        else:
            print("Contraseña incorrecta")
            contador += 1
    else:
        print("Has agotado tus intentos, mala suerte")
elif respuesta.lower() == "no":
    print("De acuerdo, generemos otra contraseña. Por favor, salga y vuelva a ejecutar el programa")
else:
    print("Respuesta no reconocida. Ejecute el programa de nuevo y responda 'Si' o 'No'.")