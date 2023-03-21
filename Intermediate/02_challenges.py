#Algunos ejercicios para practicar la logica aprendida hasta ahora con python

''' FIZZ BUZZ
Escribe un programa que muestre por consola los numeros de 1 a 100 (ambos incluidos y con un salto
de linea entre cada impresion), sustituyendo los siguientes:
- Multiplos de 3 por la palabra 'fizz'
- Multiplos de 5 por la palabra 'buzz'
- Multiplos de 2 y de 5 a la vez por la palabra 'fizzbuzz'
'''

def fizzbuzz():
    for index in range(1,101):
        if index % 2 == 0 and index % 5 == 0: 
            print('fizzbuzz')
        elif index % 5 == 0:
            print('buzz')
        elif index % 3 == 0:
            print('fizz')
        else:
            print(index)

fizzbuzz()

''' ANAGRAMA
Escribe una funcion que reciba dos palabras (string) y retorne true o false
segun sean anagramas o no
- Un anagrama consiste en formar una palabra reordenando todas las letras
de otra palabra inicial
- No hace falta comprobar que ambas palabras existan
- Dos palabras exactamente iguales no son anagramas
'''

def is_anagram(first_word, second_word):
    return not first_word.lower() == second_word.lower() and sorted(first_word.lower()) == sorted(second_word.lower())


print(is_anagram('hola', 'alho'))

''' FIBONACCI sin recursion 
Escribe un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci empezando desde 0
- La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es
la suma de los dos anteriores
'''

def fibonacci():
    prev = 0
    next = 1
    for i in range (1, 51):
        print(i,': ',prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()

''' FIBONACCI con recursion'''
'''
def fibonacci_with_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_with_recursion(n-1) + fibonacci_with_recursion(n-2)

for i in range(1, 51):
    print(i,': ', fibonacci_with_recursion(i-1))
'''

'''NUMERO PRIMO
Escribe un programa que se encargue de comprobar si un numero es o no primo.
Hecho esto, imprime los numeros primos entre 1 y 100
'''

def is_prime():

    for number in range (1,101):

        is_divisible = False

        for index in range (2, number):

            if number % index == 0 :
                is_divisible = True
                break

        if not is_divisible and number != 1:
                print(number)

is_prime()

''' INVERTIR CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del 
lenguaje que lo hagan de forma automatica. 
Si le pasamos "Hola mundo" nos retornaria "odnum aloH"
'''

def reverse(text):
    reversed_text = ''
    for index in range(len(text)-1, -1, -1):
        reversed_text += text[index]

    return reversed_text 

print(reverse('Kevin'))