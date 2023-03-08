#Diccionarios

# Definiendo un diccionario
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

my_other_dict = dict()

my_other_dict = {'Nombre':'Kevin', 'Apellido':'Caria', 'Edad': 29}

# Accediendo a valores mediante claves
print(my_dict['key2']) # value2

# Actualizando valores
my_dict['key1'] = 'new_value'
print(my_dict) # {'key1': 'new_value', 'key2': 'value2', 'key3': 'value3'}

# Agregando nuevos pares clave-valor
my_dict['key4'] = 'value4'
print(my_dict) # {'key1': 'new_value', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Eliminando un par clave-valor
del my_dict['key3']
print(my_dict) # {'key1': 'new_value', 'key2': 'value2', 'key4': 'value4'}

# Podemos utilizar el método items() para obtener un list con los items del dict
print(my_dict.items())

# Podemos utilizar el método keys() para obtener un list de las keys del dict
print(my_dict.keys())

# Podemos utilizar el método values() para obtener un list de todos los valores del dict
print(my_dict.values())

# Podemos utilizar el método fromkeys() para obtener un nuevo dict que reaprovecha todas las keys del dict que le pasamos
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Comprobando si una clave existe, solo se puede buscar por clave, no por valor
print('key1' in my_dict)

# Iterando a través de claves y valores
for key, value in my_dict.items():
    print(key, value)