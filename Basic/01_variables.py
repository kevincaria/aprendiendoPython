#Variables

#Asignacion de primeras variables y types principales
my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 10
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

#Algunas funciones de python
#Transformando un int a string
intToStringVariable = str(my_int_variable)
print(intToStringVariable)

#Cantidad de caracteres
print('Este es el largo de myStringVariable:',len(my_string_variable))

'''
Tambien se pueden crear variables en una sola linea, 
aunque no sea buena practica, interesante caracteristica de la sintaxis del lenguaje
'''
name, surname, age = 'Kevin', 'Caria', 29
print('My name is:', name, 'My surname is:', surname, 'My age is:', age)

#Cambiamos el tipo de las variables, notando el tipado dinamico de python
name = 29
age = 'Kevin'
#No se pueden crear constantes en python por este mismo tema
print(name, age)

#Se puede especificar el tipado de las variables pero simplemente para ayudarnos a nosotros,
#Igualmente puede modificarse el tipo de la variable
address: str = 'My direccion'
address = name
print(address)