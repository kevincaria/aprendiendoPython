#Tuples

#Constructores para tuplas
my_tuple = tuple() #1ra forma
my_other_tuple = () #2da forma

my_tuple = (1, 2, 3, 4, 5, 2)

# Podemos acceder a los elementos de una tupla por su índice, comenzando por 0
print(my_tuple[0])  # salida: 1
print(my_tuple[3])  # salida: 4

# Las tuplas son inmutables, lo que significa que no podemos cambiar sus elementos después de que se hayan creado
# Por lo tanto, esto provocará un error:
# my_tuple[0] = 10

# Sin embargo, podemos crear una nueva tupla a partir de una existente, agregando o eliminando elementos
# Agregar elementos a una tupla
my_new_tuple = my_tuple + (6, 7)
print(my_new_tuple)  # salida: (1, 2, 3, 4, 5, 6, 7)

# Eliminar elementos de una tupla
my_newer_tuple = my_new_tuple[:2] + my_new_tuple[3:]
print(my_newer_tuple)  # salida: (1, 2, 4, 5, 6, 7)

# Podemos desempaquetar una tupla asignándola a varias variables
a, b, c = my_tuple[:3]
print(a, b, c)  # salida: 1 2 3

# Podemos utilizar el operador * para desempaquetar el resto de los elementos en una lista
d, *e, f = my_newer_tuple
print(d, f)  # salida: 1 7
print(e)  # salida: [2, 4, 5, 6]

# Podemos utilizar la función len para obtener la longitud de una tupla
print(len(my_tuple))  # salida: 5

# Podemos utilizar el método count para contar la cantidad de veces que un elemento aparece en una tupla
print(my_tuple.count(2))  # salida: 2

# Podemos utilizar el método index para obtener el índice de la primera aparición de un elemento en una tupla
print(my_tuple.index(2))  # salida: 1

# También podemos utilizar la función tuple para convertir una lista en una tupla
my_list = [1, 2, 3]
my_new_tuple = tuple(my_list)
print(my_new_tuple)  # salida: (1, 2, 3)