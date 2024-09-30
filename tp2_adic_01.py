"""
Ejercicio 1
    a) Realice una función que procesa la información de alumnos de la UNAB. De cada alumno se
    conoce legajo, nombre, apellido, contraseña. El procesamiento termina cuando se ingresa el
    número de legajo 0. La función deberá retornar una lista con la información procesada.
    
    b) Realice una función llamada imprimir_alumno que recibe como parámetro una lista con los datos
    de un alumno (Legajo, nombre, apellido, contraseña), los datos del alumno serán mostrados por
    pantalla con la forma:
    Legajo:XXXX
    Nombre:XXXX
    Apellido:XXXX
    Contraseña:XXXXX
    
    c) Realice un función llamada legajo_menor que recibe como parámetro una lista de alumnos, de
    cada alumno se conoce la información (legajo, nombre, apellido, contraseña), la función debe
    buscar cuál es el alumno con el menor legajo dentro de la lista y retornarlo.
    
    d) Realice un función llamada nombre_mas_largo que recibe como parámetro una lista de alumnos.
    La función debe buscar cuál es el alumno con el nombre más largo dentro de la lista y retornarlo.
    
    e) Realice un función llamada controlar_clave que recibe como parámetro un alumno,(legajo,
    nombre, apellido, contraseña). La función debe controlar si la contraseña es mayor a 6 caracteres y
    termina con un número, deberá imprimir un mensaje especificando el error cometido en caso de no
    cumplir las condiciones o bien imprimir los datos del alumno si la clave cumple con todas las
    condiciones.
    
    f) Realice una función llamada verificar_claves que recibe como parámetro una lista de alumnos, la
    función deberá controlar por cada alumno si la contraseña que usa cumple con: ser mayor a 6
    caracteres y terminar con un número.
    Construir un menú, el menú deberá permitir ingresar 5 opciones, La opción 0 permite salir del menú,
    el resto de las opciones permiten:
    imprimir los datos de todos los alumnos con el formato pedido en el punto a)
    imprimir los datos del alumno que tiene el legajo más chico.
    imprimir los datos del alumno que tiene el nombre más largo.
    Imprimir si las contraseñas de cada alumno cumplen con un tamaño mayor a 6 caracteres y
    terminan con un número.
"""

class Alumno(object):
    def __init__(self, legajo, nombre, apellido, contraseña):
        self.nombre = nombre
        self.legajo = legajo
        self.apellido = apellido
        self.contraseña = contraseña
    

def ingresar_alumno():
    alumnos = []
    legajo = int(input("Ingrese un número de legajo: (0 para salir del programa) "))
    while legajo != 0:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        contraseña = input("Ingrese la contraseña: ")
        
        alumno = Alumno(legajo, nombre, apellido, contraseña)
        alumnos.append(alumno)
        
        legajo = int(input("Ingrese un número de legajo: (0 para salir del programa)"))
    
    print("Programa FINALIZADO.")
    return alumnos



def imprimir_alumnos():
    for alumno in lista_alumnos:
        print(f"Legajo: {alumno.legajo}, Nombre: {alumno.nombre}, Apellido: {alumno.apellido}, Contraseña: {alumno.contraseña}")
        
        
lista_alumnos = ingresar_alumno()
imprimir_alumnos()
    