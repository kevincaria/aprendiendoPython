# Clases

# Definir una clase de persona, las clases en python se definen con CamelCase
class Person:
    """Clase que define a una persona con nombre y edad."""

    # Constructor de la clase Persona
    def __init__(self, name, age):
        """Constructor de la clase que inicializa el nombre y la edad."""
        self.name = name #atributo publico
        self.age = age #atributo publico
        self.__full_name = f'{name} {age}' #atributo privado se designa con el doble guion bajo
    
    #Como armar un 'get' en python para acceder a los atributos sin poder modificarlos
    def get_name(self):
        return self.__full_name
    
#Funcion de la clase Person
    def walk(self):
        print(f'{self.name} de {self.age} esta caminando')

# Crear una instancia de la clase Persona
my_person = Person("Juan", 25)

#Llamando a la funcion walk de Person
my_person.walk

# Imprimir el nombre y la edad de la persona, no necesita gets como en java
print(my_person.name)
print(my_person.age)

#Si hacemos que los atributos sean 'privados' con gets armados, asi solo podemos leerlos pero no modificarlos
print(my_person.get_name())

#Para cambiarle el valor a algun atributo del objeto, no necesito sets como en java
my_person.name = 'Kevin'
print(my_person.name)
# En Python, la sintaxis para definir una clase es la siguiente:
# class NombreDeLaClase:
#     def __init__(self, parametro1, parametro2, ...):
#         self.atributo1 = parametro1
#         self.atributo2 = parametro2
#         ...

# La línea de código 'class Persona:' define una clase llamada 'Persona'. El código indentado debajo de la línea 'class' es el cuerpo de la clase. En este caso, la clase tiene un constructor que toma dos parámetros 'nombre' y 'edad', y dos métodos que devuelven el nombre y la edad de la persona.

# El constructor es un método especial que se llama automáticamente cuando se crea una nueva instancia de la clase. El constructor utiliza la palabra clave 'self' para hacer referencia a la instancia de la clase que se está creando, y utiliza la sintaxis 'self.atributo = valor' para asignar valores a los atributos de la instancia.

# Para crear una nueva instancia de la clase Persona, simplemente llamamos a la clase y proporcionamos los argumentos necesarios. En este caso, se crea una instancia llamada 'my_person' con el nombre 'Juan' y la edad '25'.
