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

def menu():
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 0:
        print("FIN DEL PROGRAMA")
    elif opcion == 1:
        imprimir_alumnos()
    elif opcion == 2:
        alumno_menor = legajo_menor(lista_alumnos)
        print(f"El legajo más chico es: {alumno_menor.legajo}, Nombre: {alumno_menor.nombre}, Apellido: {alumno_menor.apellido}")    
    elif opcion == 3:
        alumno_nombre_largo = nombre_largo(lista_alumnos)
        print(f"El nombre más largo es del alumno: {alumno_nombre_largo.legajo}, Nombre: {alumno_nombre_largo.nombre}, Apellido: {alumno_nombre_largo.apellido}")
    elif opcion == 4:
        verifica_contraseña(lista_alumnos)
    else:
        print("FIN DEL PROGRAMA")
        

def ingresar_alumno():
    alumnos = []
    legajo = int(input("Ingrese un número de legajo: (0 para salir del programa)  "))
    while legajo != 0:
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        contraseña = input("Ingrese la contraseña: ")
        
        alumno = Alumno(legajo, nombre, apellido, contraseña)
        alumnos.append(alumno)
        
        legajo = int(input("Ingrese un número de legajo: (0 para salir del programa)"))
    
    print("Programa para ingresar alumnos FINALIZADO.")
    print("")
    return alumnos



def imprimir_alumnos():
    for alumno in lista_alumnos:
        print(f"Legajo: {alumno.legajo}, Nombre: {alumno.nombre}, Apellido: {alumno.apellido}, Contraseña: {alumno.contraseña}")
        
        
def legajo_menor(lista_alumnos):
    legajo_menor = lista_alumnos[0]
    for alumno in lista_alumnos[1:]:
        if alumno.legajo < legajo_menor.legajo:
            legajo_menor = alumno
    return legajo_menor


def nombre_largo(lista_alumnos):
    nombre_largo = lista_alumnos[0]
    for alumno in lista_alumnos[1:]:
        if len(alumno.nombre) > len(nombre_largo.nombre):
            nombre_largo = alumno
    return nombre_largo

def controlar_clave(alumno):
    contraseña = alumno.contraseña
    if len(contraseña) < 6:
        print("ERROR, contraseña demasiado corta")
    elif not contraseña[-1].isdigit():
        print("ERROR, la contraseña debe tener un digito al final")
    else:
        print("Contraseña correcta")  


def verifica_contraseña(lista_alumnos):       
    for alumno in lista_alumnos:  
        contraseña = alumno.contraseña
        if len(contraseña) < 6:
            print(f"ERROR, contraseña de {alumno.nombre}, {alumno.apellido} demasiado corta")
        elif not contraseña[-1].isdigit():
            print("ERROR, la contraseña debe tener un digito al final")
        else:
            print(f"Contraseña de {alumno.nombre}, {alumno.apellido} es correcta")    

print("Bienvenido, primero ingresemos los datos de los alumnos: ")


lista_alumnos = ingresar_alumno()
print("")

print("Ingrese 1 para imprimir los datos de los alumnos: ")
print("Ingrese 2 para imprimir los datos del alumno con legajo más chico: ")
print("Ingrese 3 para imprimir los datos del alumno con el nombre más largo: ")
print("Ingrese 4 para verificar si todas las contraseñas de los alumnos es corecta: ")
print("Ingrese 0 para salir del programa")
print("")

menu()


"""
imprimir_alumnos()

alumno_menor_legajo = legajo_menor(lista_alumnos)
print(f"El legajo más chico es: {alumno_menor_legajo.legajo}, Nombre: {alumno_menor_legajo.nombre}, Apellido: {alumno_menor_legajo.apellido}")
print("")

alumno_nombre_largo = nombre_largo(lista_alumnos)
print(f"El nombre más largo es: {alumno_nombre_largo.nombre}")    
print("")

controlar_clave(lista_alumnos[0])
print("")

verifica_contraseña(lista_alumnos)
print("")
"""