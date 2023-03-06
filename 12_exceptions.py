# Excepciones

#Ejemplo con try except else finally

number_one = 1
number_two = '1'

try:
    print(number_one + number_two)
    print('No se ha producido un error')
except: #Si hay un try hay un except, si no se especifica que error capturar, toma todos
    print('Se ha producido un error') #Se ejecuta si se produce una excepcion
else: #Opcional
    print('La ejecucion continua correctamente') #Se ejecuta si no se produce una excepcion
finally: #Opcional
    print('La ejecucion continua') #Se ejecuta siempre 

#Mismo ejemplo pero trabajando los errores concretos
try:
    print(number_one + number_two)
    print('No se ha producido un error')
except ValueError: 
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')

#Otro ejemplo capturando el mensaje de error dado por python
dividendo = 10
divisor = 0

# Definimos una función para dividir dos números
def dividir(dividendo, divisor):
    try:
        # Intentamos hacer la división
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError: #Se indica que capture SOLO errores ZeroDivisionError, si hay otro error no pasa por except
        # Si ocurre un error de división por cero, lanzamos una excepción personalizada
        raise ValueError("No se puede dividir por cero.")

# Ejemplo de uso de la función
try:
    resultado = dividir(10, 0)
    print(resultado)
except ValueError as error: #error es el nombre de la variable que contiene el string con el mensaje de error
    # Si ocurre una excepción personalizada, imprimimos el mensaje de error
    print("Error:", error)

# En este ejemplo, definimos una función llamada 'dividir' que toma dos parámetros: 'dividendo' y 'divisor'.
# Dentro de la función, utilizamos la declaración 'try-except' para manejar excepciones.
# Si se intenta dividir un número por cero, se lanza una excepción 'ZeroDivisionError'.
# En este caso, capturamos la excepción utilizando la declaración 'except' y lanzamos una excepción personalizada 'ValueError'.
# Luego, en el ejemplo de uso de la función, llamamos a la función 'dividir' con los parámetros 10 y 0.
# Como se intenta dividir por cero, se lanza la excepción personalizada, que capturamos y mostramos el mensaje de error.
# De esta manera, podemos controlar el flujo de nuestro programa incluso cuando ocurren errores imprevistos.



