# Strings

# Definimos una cadena de texto
string = "Hola, mundo!"
other_string = 'Mi otro string'

#Concatenando strings 
print(string + other_string)

#Salto de linea en un string con \n
line_string = 'Este es un String \ncon salto de linea'

#Tabulación en un string con \t
tab_string = '\tEste es un String con tab'
#Si a \t o a \n le agregamos doble barra \\ no realiza el salto o el tab \\t

# Accedemos a los caracteres de la cadena utilizando índices
print(string[0])  # H
print(string[-1])  # !

#Para acceder a una porcion del string utilizando indices
print(string[2:7])  # la, m

#Reverse
print(string[::-1])

# Utilizamos el método len() para obtener la longitud de la cadena
print(len(string))  # 12

# Utilizamos el método split() para dividir la cadena en una lista de palabras
words = string.split()
print(words)  # ['Hola,', 'mundo!']

# Utilizamos el método lower() para convertir la cadena a minúsculas
lowercase_string = string.lower()
print(lowercase_string)  # hola, mundo!

# Utilizamos el método upper() para convertir la cadena a mayúsculas
uppercase_string = string.upper()
print(uppercase_string)  # HOLA, MUNDO!

# Utilizamos el método replace() para reemplazar una parte de la cadena por otra
new_string = string.replace("mundo", "Python")
print(new_string)  # Hola, Python!

# Utilizamos el método find() para buscar la posición de una subcadena dentro de la cadena
position = string.find("mundo")
print(position)  # 6

# Utilizamos el método count() para contar cuántas veces aparece una subcadena dentro de la cadena
count = string.count("o")
print(count)  # 2

#Formateo
name, surname, age = 'Kevin', 'Caria', 29
#1ra forma dando los datos tal cual para el print
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
#2da forma formatiando los datos a string
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
#3ra forma
print(f'Mi nombre es {name} {surname} y mi edad es {age}')

#Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language #Se guarda un caracter en cada variable
print(a)     # P
print(e)     # o

#Funciones booleanas
print(language.isnumeric())
print(language.isupper())
print(language.startswith('Py')) #Diferencia mayúsculas y minusculas