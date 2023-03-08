#Operadores

a = 5
b = 3

# Operadores aritméticos
sum = a + b # suma
difference = a - b # resta
product = a * b # multiplicación
quotient = a / b # división
intQuotient = a // b #división entera
remainder = a % b # módulo
exponentiation = a ** b # potencia

print("La suma de a y b es:", sum)
print("La diferencia de a y b es:", difference)
print("El producto de a y b es:", product)
print("El cociente de a y b es:", quotient)
print("El cociente entero de a y b es:", intQuotient)
print("El residuo de a dividido por b es:", remainder)
print("a elevado a la b es:", exponentiation)

# Operadores de comparación
equality = a == b # igualdad
inequality = a != b # desigualdad
greater_than = a > b # mayor que
less_than = a < b # menor que
greater_than_or_equal = a >= b # mayor o igual que
less_than_or_equal = a <= b # menor o igual que

print("a es igual a b:", equality)
print("a es diferente de b:", inequality)
print("a es mayor que b:", greater_than)
print("a es menor que b:", less_than)
print("a es mayor o igual que b:", greater_than_or_equal)
print("a es menor o igual que b:", less_than_or_equal)

#Si comparamos strings, se basa en el orden alfabetico ASCII, teniendo en cuenta mayúsculas y minúsculas
print('Hola' > 'Python')

# Operadores lógicos
logical_and = a > 0 and b > 0 # y lógico
logical_or = a > 0 or b > 0 # o lógico
logical_not = not a > 0 # no lógico

print("a y b son mayores que cero:", logical_and)
print("a o b son mayores que cero:", logical_or)
print("a no es mayor que cero:", logical_not)

# Concatenando variables de texto
nombre = 'Kevin'
edad = 84
mensaje = "Mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print(mensaje)

#No se puede concatenar (+) un string con un int pero si podemos multiplicar strings
variable = 'hola'
print(variable * 5)
