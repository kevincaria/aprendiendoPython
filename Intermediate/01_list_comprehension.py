#List Comprehension

# Se define una lista con los valores del 0 al 7
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]

# Se imprime la lista definida anteriormente
print(my_original_list)

# Se define un rango de valores del 0 al 7
my_range = range(8)

# Se convierte el rango en una lista y se imprime
print(list(my_range))

# Se define una nueva lista con los valores resultantes de sumar 1 al valor de cada elemento del rango del 0 al 7
my_list = [i + 1 for i in range(8)]

# Se imprime la lista resultante
print(my_list)

# Se define una nueva lista con los valores resultantes de multiplicar por 2 cada elemento del rango del 0 al 7
my_list = [i * 2 for i in range(8)]

# Se imprime la lista resultante
print(my_list)

# Se define una nueva lista con los valores resultantes de elevar al cuadrado cada elemento del rango del 0 al 7
my_list = [i * i for i in range(8)]

# Se imprime la lista resultante
print(my_list)

# Se define una función que recibe un número y devuelve su suma más 5
def sum_five(number):
    return number + 5

# Se define una nueva lista con los valores resultantes de aplicar la función definida anteriormente a cada elemento del rango del 0 al 7
my_list = [sum_five(i) for i in range(8)]

# Se imprime la lista resultante
print(my_list)
