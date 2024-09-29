# Ejercicio 4: Definir una función recursiva que imprime los números sucesivos desde n hasta 10. Por
#              ejemplo funcion_sucesivo (6) Imprimirá: 6,7,8,9,10

def funcion_sucesivo(numero):
    sucesion = numero
    if numero > 10:
        print("ERROR, el número ingresado es mayor a 10")
    while sucesion <= 10:
        print(sucesion)
        sucesion += 1


numero = int(input("Ingrese un número, no mayor a diez: "))
funcion_sucesivo(numero)
