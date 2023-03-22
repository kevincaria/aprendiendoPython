# Lambdas en Python
'''
las lambdas son funciones anónimas que pueden ser utilizadas en lugar de definir 
una función completa. Son útiles en situaciones donde se necesita una función simple
para ser utilizada como argumento en otra función o para crear funciones más complejas 
de manera dinámica.
'''
# Sintaxis básica:
# lambda argumentos: expresión

# Ejemplo 1: función que suma dos valores utilizando una lambda
sum_two_values = lambda first_value, second_value: first_value + second_value

# Llamada a la función
print(sum_two_values(8, 10)) # Output: 18

# Ejemplo 2: función que multiplica dos valores utilizando una lambda
multiply_values = lambda first_value, second_value: first_value * second_value

# Llamada a la función
print(multiply_values(2, 10)) # Output: 20

# Ejemplo 3: lambda sin argumentos
greeting = lambda: "Hola, mundo!"

# Llamada a la función
print(greeting()) # Output: Hola, mundo!

# Ejemplo 4: lambda con un número variable de argumentos
sum_all_values = lambda *values: sum(values)

# Llamada a la función con diferentes números de argumentos
print(sum_all_values(1, 2, 3, 4)) # Output: 10
print(sum_all_values(1, 2)) # Output: 3
print(sum_all_values(1)) # Output: 1
print(sum_all_values()) # Output: 0

# Ejemplo 5: lambda que devuelve otra lambda
def power_function(power):
    return lambda x: x ** power

# Llamada a la función para crear una nueva lambda
square = power_function(2)

# Llamada a la nueva lambda
print(square(5)) # Output: 25

# Ejemplo 6: uso de lambdas con funciones integradas en Python
# sorted() utiliza una lambda para ordenar una lista de diccionarios por el valor de una clave
fruits = [
    {"name": "apple", "price": 0.5},
    {"name": "banana", "price": 0.25},
    {"name": "orange", "price": 0.75}
]

sorted_fruits = sorted(fruits, key=lambda x: x["price"])

# Imprime la lista ordenada
print(sorted_fruits)
# Output: [{'name': 'banana', 'price': 0.25}, {'name': 'apple', 'price': 0.5}, {'name': 'orange', 'price': 0.75}]

