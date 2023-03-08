# Condicionales

# Definimos una variable numérica
numero = 10

# Verificamos si el número es mayor que 0
if numero > 0:
    print("El número es mayor que 0")

# Verificamos si el número es igual a 0
if numero == 0:
    print("El número es igual a 0")
    
# Verificamos si el número es par
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
# Verificamos si el número es múltiplo de 3 y 5
if numero % 3 == 0 and numero % 5 == 0:
    print("El número es múltiplo de 3 y 5")
elif numero % 3 == 0:
    print("El número es múltiplo de 3")
elif numero % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo ni de 3 ni de 5")

#Evaluando con mas de una condicion
my_condition = 5 * 5

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

# Si pasamos una variable no booleana en un if, evalua si la variable esta vacia o no 