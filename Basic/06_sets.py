# Sets
#Un set no es una estructura ordenada como una lista, utiliza un hash para agregar elementos al set
#Gracias al hash, no deja ingresar elementos repetidos

#Constructores para sets
my_set = set()
my_other_set = {}  #Inicialmente es un diccionario con este constructor, pero con el tipado dinamico no influye mucho

# Creamos un set con algunos elementos
my_set = {1, 2, 3, 4, 5}

# Podemos acceder a los elementos de un set usando un bucle for
for x in my_set:
    print(x)

#Podemos realizar busquedas en los sets de la siguiente forma, la cual nos devuelve un booleano
print(10 in my_set)

# Agregar elementos a un set usando el método add()
my_set.add(6)
print(my_set)

# Agregar múltiples elementos a un set usando el método update()
my_set.update([7, 8, 9])
print(my_set)

# Remover elementos de un set usando el método remove()
my_set.remove(8)
print(my_set)

# Podemos utilizar el método discard() para eliminar un elemento, pero no nos dará un error si el elemento no existe en el set
my_set.discard(10)
print(my_set)

# Podemos utilizar el método pop() para eliminar un elemento arbitrario de un set y obtener su valor
x = my_set.pop()
print(x, my_set)

# Podemos utilizar el método clear() para vaciar el set
my_set.clear()
print(my_set)

# Podemos utilizar el método union() para unir dos sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

# Podemos utilizar el método intersection() para obtener la intersección de dos sets
set4 = {1, 2, 3}
set5 = {3, 4, 5}
set6 = set4.intersection(set5)
print(set6)

# Podemos utilizar el método difference() para obtener la diferencia entre dos sets
set7 = {1, 2, 3}
set8 = {3, 4, 5}
set9 = set7.difference(set8)
print(set9)

# Podemos utilizar el método symmetric_difference() para obtener los elementos que están en ambos sets, pero no en ambos al mismo tiempo
set10 = {1, 2, 3}
set11 = {3, 4, 5}
set12 = set10.symmetric_difference(set11)
print(set12)

# Podemos utilizar el método issubset() para verificar si un set es un subconjunto de otro set
set13 = {1, 2}
set14 = {1, 2, 3, 4, 5}
print(set13.issubset(set14))  # True

# Podemos utilizar el método issuperset() para verificar si un set es un superconjunto de otro set
set15 = {1, 2, 3, 4, 5}
set16 = {1, 2}
print(set15.issuperset(set16))  # True

# Podemos utilizar el método isdisjoint() para verificar si dos sets no tienen elementos en común
set17 = {1, 2, 3}
set18 = {4, 5, 6}
print(set17.isdisjoint(set18))  # True
