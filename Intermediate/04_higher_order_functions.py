# Higher order functions

'''
Las funciones de orden superior son funciones que pueden tomar otras funciones 
como argumentos y/o retornar funciones como resultado. Estas funciones son muy útiles 
ya que permiten una mayor modularidad y reutilización de código.
'''
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

# se llama la función sum_two_values_and_add_one con los argumentos 8, 1 y la función sum_one
print(sum_two_values_and_add_one(8,1, sum_one))

# se llama la función sum_two_values_and_add_one con los argumentos 8, 1 y la función sum_five
print(sum_two_values_and_add_one(8,1, sum_five))

# Built-in Higher Order Functions

numbers = [2, 5, 10, 21, 3, 30]

## Map
def multiply_two(number):
    return number * 2

# se aplica la función multiply_two a cada elemento de la lista numbers utilizando la función map y se convierte el resultado a lista
print(list(map(multiply_two, numbers))) 

# se utiliza una función lambda para multiplicar cada elemento de la lista numbers por 2 utilizando la función map y se convierte el resultado a lista
print(list(map(lambda number: number * 2, numbers)))

## Filter
def filter_greater_than_ten(number):
    return number > 10

# se filtran los elementos de la lista numbers que cumplen la condición de la función filter_greater_than_ten y se convierte el resultado a lista
print(list(filter(filter_greater_than_ten, numbers)))

# se utiliza una función lambda para filtrar los elementos de la lista numbers que son mayores a 10 y se convierte el resultado a lista
print(list(filter(lambda number: number > 10, numbers)))

## Reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value

# se utiliza la función reduce para aplicar la función sum_two_values de manera acumulativa a los elementos de la lista numbers
print(reduce(sum_two_values, numbers))



# Closures
'''
los closures son funciones que capturan valores del ámbito externo a la función y 
los mantienen vivos mientras la función sigue en ejecución. 
Los closures son muy útiles para crear funciones más flexibles y personalizables
'''
def sum_ten(original_value):
    def add(value):
        return value + original_value + 10
    return add

# se crea una función sum_ten con el valor original de 1 y se asigna el resultado a la variable add_closure
add_closure = sum_ten(1)

# se llama la función add_closure con el argumento 5, que se suma con el valor original de 1 y con 10, dando un resultado de 16
print(add_closure(5))

# se llama la función sum_ten con el valor original de 5 y se le pasa como argumento el valor 1, que se suma con el valor original de 5 y con 10, dando un resultado de 16
print(sum_ten(5)(1))
