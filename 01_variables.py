#Variables

#Asignacion de primeras variables y types principales
myStringVariable = 'My string variable'
print(myStringVariable)

myIntVariable = 10
print(myIntVariable)

myBoolVariable = False
print(myBoolVariable)

#Concatenación de variables en un print
print(myStringVariable, myIntVariable, myBoolVariable)

#Algunas funciones de python
#Transformando un int a string
intToStringVariable = str(myIntVariable)
print(intToStringVariable)

#Cantidad de caracteres
print('Este es el largo de myStringVariable:',len(myStringVariable))

'''
Tambien se pueden crear variables en una sola linea, 
aunque no sea buena practica, interesante caracteristica de la sintaxis del lenguaje
'''
name, surname, age = 'Kevin', 'Caria', 29
print('My name is:', name, 'My surname is:', surname, 'My age is:', age)

#Cambiamos el tipo de las variables, notando lo debilmente tipado que es python
name = 29
age = 'Kevin'

print(name, age)

#Se puede especificar el tipado de las variables pero simplemente para ayudarnos a nosotros,
#Igualmente puede modificarse el tipo de la variable
address: str = 'My direccion'
address = name
print(address)