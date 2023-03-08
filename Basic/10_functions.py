# Funciones 

# Definir una función que suma dos números
def sumar(a, b):
    """Función que suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado

# Llamar a la función y asignar el resultado a una variable
x = sumar(5, 3)

# Imprimir el resultado
print(x)


#Se puede definir un valor por defecto a un parametro de la funcion si no le pasamos alguno al momento de llamar al a funcion
def print_name(name, surname, alias = 'Sin alias'):
    print( f'{name} {surname} {alias}')

print_name ('Kevin', 'Caria') #Imprime 'Sin alias'
print_name ('Kevin','Caria','Kevin') #Imprime con el alias 'Kevin'

#Se puede definir una funcion en el que se ingresen la cantidad que queramos de parametros
def print_texts(*text):
    print(text)

print_texts('hola','como estas', 'todo bien')
print_texts('Python')
# Explicación teórica:
# Las funciones son bloques de código que se definen una vez pero pueden ser llamados y ejecutados múltiples veces en diferentes partes de un programa. Las funciones pueden aceptar uno o más parámetros y pueden devolver un valor a quien llama la función.

# La sintaxis para definir una función en Python es la siguiente:
# def nombre_de_la_funcion(parametro1, parametro2, ...):
#     cuerpo_de_la_funcion
#     return valor_de_retorno (opcional)

# La línea de código 'def sumar(a, b):' define una función llamada 'sumar' que toma dos parámetros 'a' y 'b'. El código indentado debajo de la línea 'def' es el cuerpo de la función. En este caso, la función simplemente suma los dos números proporcionados y devuelve el resultado.

# Para llamar a la función, simplemente escribimos el nombre de la función seguido de un par de paréntesis que contienen los valores de los argumentos que se pasarán a la función. En este caso, la función 'sumar' se llama con los números 5 y 3 como argumentos.

# El valor devuelto por la función se asigna a una variable 'x'. Finalmente, el valor de 'x' se imprime utilizando la función 'print'.

#Mas ejemplos

def my_function ():
    print('Esto es una funcion')

my_function()

def sum_values(number_one, number_two):
    return number_one + number_two

print(sum_values(1,2))