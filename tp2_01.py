# Ejercicio 1: Definir una función que calcule la suma de todos los números enteros comprendidos
#              entre cero y un número entero positivo dado.


def suma_de_numeros(numero):
    suma = 0
    contador = 0
    while contador <= numero:
        suma += contador
        contador += 1
    return suma
    
    
numero = int(input("Ingrese un número: "))
resultado = suma_de_numeros(numero)
print(f"La suma de los números del 0 al {numero} es: {resultado}")

suma_de_numeros(numero)