# Regular Expressions

import re

# match: busca si el patrón se encuentra al principio de la cadena
my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

# re.I es la flag para que la búsqueda sea case-insensitive (no distinga mayúsculas y minúsculas)
match = re.match("Esta es la lección", my_string, re.I)
print(match)

# Se utiliza la función span() para obtener los índices de la posición inicial y final de la coincidencia
start, end = match.span()
print(my_string[start:end])

# Si el patrón no coincide con la cadena, la función devuelve None
match = re.match("Esta no es la lección", my_other_string)
# Otra forma de comprobar el None es utilizando "if match is not None:"
if not match:
    print("No hubo coincidencia")

# search: busca la primera ocurrencia del patrón en la cadena
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall: busca todas las ocurrencias del patrón en la cadena y devuelve una lista
findall = re.findall("lección", my_string, re.I)
print(findall)

# split: divide la cadena en una lista de subcadenas utilizando el patrón como separador
print(re.split(":", my_string))

# sub: reemplaza todas las ocurrencias del patrón con otra cadena
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


# Los patrones son secuencias de caracteres que definen un conjunto de cadenas a buscar
# Para aprender y validar expresiones regulares: https://regex101.com

# Busca todas las ocurrencias de "lección" o "Lección" en la cadena
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

# Busca todas las ocurrencias de "lección" o "Lección" o "Expresiones" en la cadena
pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

# Busca todas las ocurrencias de dígitos en la cadena
pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

# Busca todas las ocurrencias de cualquier dígito en la cadena
pattern = r"\d"
print(re.findall(pattern, my_string))

# Busca todas las ocurrencias de cualquier carácter que no sea un dígito en la cadena
pattern = r"\D"
print(re.findall(pattern, my_string))

# Busca todas las ocurrencias de "l" seguido de cualquier cantidad de caracteres
pattern = r"[l].*"
print(re.findall(pattern, my_string))

# Verifica si la cadena cumple con el formato de una dirección de correo electrónico
email = "kevincaria@kevin.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

# Busca todas las ocurrencias de la expresión regular 'pattern' en la cadena 'email'
email = "kevincaria@kevin.com.com"
print(re.findall(pattern, email))
