# Ejercicio 2: Implementar una función que me permita ver si un número es capicúa o no.

def verifica_capicua (numero):
    str_num = str(numero)
    if len (str_num) == 1:
        print("el número es capicua")
    
    elif str_num[0] == str_num[-1]:
        return verifica_capicua(str_num[1:-1])
    
    else:
        print("El número no es capicua")
    
numero = int(input("Ingrese un número por favor: "))
verifica_capicua(numero)