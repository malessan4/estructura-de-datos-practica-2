# Ejercicio 5: Desarrollar un algoritmo que permita calcular la siguiente serie: h(n) =
#              1+1/2+1/3+...+1/n

from fractions import Fraction

def serie(n):
    if n==2:
        return Fraction(1,2)
    else:
        return "{} {}".format(serie(n-1),Fraction(1,n))

n = int(input("Ingrese un número: "))        
print(serie(n))