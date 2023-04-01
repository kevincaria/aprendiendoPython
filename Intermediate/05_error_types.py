# Error types

#Documentando algunos errores típicos en Python
 
# SyntaxError: Se produce cuando hay un error en la sintaxis del código.
# print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError: Se produce cuando se intenta usar una variable que no ha sido definida previamente.
language = "Spanish"  # Comentar para Error
print(language)

# IndexError: Se produce cuando se intenta acceder a un índice que está fuera del rango de una lista.
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError: Se produce cuando se intenta importar un módulo que no existe.
# import maths # Descomentar para Error

# AttributeError: Se produce cuando se intenta acceder a un atributo que no existe en un objeto.
# print(math.PI) # Descomentar para Error
from math import pi
import math
print(math.pi)

# KeyError: Se produce cuando se intenta acceder a una clave que no existe en un diccionario.
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError: Se produce cuando se intenta realizar una operación con objetos de tipos incompatibles.
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError: Se produce cuando se intenta importar un módulo que no puede ser encontrado o importado.
# from math import PI # Descomentar para Error
print(pi)

# ValueError: Se produce cuando se intenta convertir un valor a un tipo que no es compatible.
# my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError: Se produce cuando se intenta dividir un número por cero.
# print(4/0) # Descomentar para Error
print(4/2)
