# Loops

# Loop while: este loop se ejecuta mientras una condición sea verdadera.
# En este caso, se imprimirá el valor de la variable `i` mientras sea menor o igual a 5.
# Cada vez que se imprime el valor de `i`, se incrementa en 1.
print("Loop while:")
i = 1
while i <= 5:
    print(i)
    i += 1

# Ejemplo de implementación de un ciclo "do while" en Python
# En este ejemplo, se le solicita al usuario que ingrese un número positivo
# y se asegura que el número sea positivo utilizando un ciclo "do while" ya que no es una estructura 
# basica de python

# Definir la variable "numero" con un valor inicial de -1
numero = -1

# Utilizar un ciclo "do while" para solicitar al usuario que ingrese un número positivo
while True:
    numero = int(input("Ingrese un número positivo: "))
    if numero > 0:
        break

# Imprimir el número ingresado por el usuario
print("El número ingresado es:", numero)

#while-else 
#en Python se puede utilizar una cláusula else junto con un ciclo while. 
# La cláusula else en un ciclo while se ejecuta después de que la condición del ciclo se vuelva falsa,
#  siempre y cuando el ciclo no se haya interrumpido con una instrucción break.
# Imprimir los números del 1 al 5 utilizando un ciclo while
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Fin del ciclo while")

# Loop for: este loop se utiliza para iterar sobre una secuencia de números.
# En este caso, se utiliza la función `range` para generar una secuencia de números del 1 al 5.
# El valor de `j` se establece en cada iteración del loop y se imprime.
print("Loop for:")
for j in range(1, 6):
    print(j)

# Loop for con lista: este loop se utiliza para iterar sobre una lista de elementos.
# En este caso, se define una lista de frutas y se utiliza un loop for para iterar sobre cada elemento de la lista e imprimirlo.
print("Loop for con lista:")
list = ["manzana", "banana", "cereza"]
for fruit in list:
    print(fruit)
# De la misma forma se puede iterar con tuplas y sets

# Loop for con tuplas
my_tuple = (29, 1.70, "Kevin", "Caria", "Kevin")
for element in my_tuple:
    print(element)


# Loop for con sets
my_set = {"Kevin", "Caria", 29}
for element in my_set:
    print(element)

# Loop for con diccionario: este loop se utiliza para iterar sobre un diccionario.
# En este caso, se define un diccionario con claves y valores, y se utiliza un loop for para iterar sobre cada clave y valor del diccionario e imprimirlo.
print("Loop for con diccionario:")
my_dict = {"nombre": "Kevin", "edad": 29, "ciudad": "Buenos Aires"}
for key, value in my_dict.items():
    print(key + ": " + str(value))

# Loop for tambien puede tener else y combinar con condiciones como el while,
#En este caso, en lugar de usar un break para frenar el loop como hicimos en el while,
#Usamos un continue para indicar que el loop continue a pesar de haber cumplido con la condicion
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")