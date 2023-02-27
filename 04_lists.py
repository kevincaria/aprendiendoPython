# Lists

#Formas de inicializar una lista, en python listas o arrays son similares, el concepto de array por si solo no existe, se agrupa en listas
my_list = list()
my_other_list = []

#Se pueden definir listas con elementos de varios tipos
my_list = [35, 1.77, 'hola']

#se puede asignar el contenido de las listas a variables
age, height, string = my_list

# Definimos una lista de números
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Accedemos a los elementos de la lista utilizando índices
print(numbers[0])  # 1
print(numbers[-1])  # 5

# Utilizamos el método len() para obtener la longitud de la lista
print(len(numbers))  # 5

# Utilizamos el método append() para añadir un elemento a la lista
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Utilizamos el método extend() para añadir varios elementos a la lista
numbers.extend([7, 8, 9])
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Utilizamos el operador + para concatenar dos listas
more_numbers = [10, 11, 12]
all_numbers = numbers + more_numbers
print(all_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Utilizamos el método insert() para insertar un elemento en una posición específica de la lista
all_numbers.insert(0, 0)
print(all_numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Utilizamos el operador * para repetir una lista varias veces
repeated_numbers = [0] * 3
print(repeated_numbers)  # [0, 0, 0]

# Utilizamos el operador in para comprobar si un elemento está en la lista
print(5 in all_numbers)  # True
print(13 in all_numbers)  # False

# Utilizamos el método remove() para eliminar un elemento de la lista
all_numbers.remove(0)
print(all_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Utilizamos el método pop() para eliminar el último elemento de la lista y devolverlo
last_number = all_numbers.pop()
print(last_number)  # 12
print(all_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Utilizamos el método index() para obtener el índice de la primera aparición de un elemento en la lista
index = all_numbers.index(5)
print(index)  # 4

# Utilizamos el método count() para contar cuántas veces aparece un elemento en la lista
count = all_numbers.count(5)
print(count)  # 1

# Utilizamos el método sort() para ordenar la lista
all_numbers.sort()
print(all_numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Utilizamos el método reverse() para invertir el orden de los elementos en la lista
all_numbers.reverse()
print(all_numbers)
