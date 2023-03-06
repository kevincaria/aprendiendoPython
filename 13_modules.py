#Modulos

'''
los módulos en Python son simplemente archivos Python que contienen definiciones de funciones, 
variables y/o clases que se pueden utilizar en otros archivos Python. Para crear un módulo, 
simplemente creamos un archivo Python y definimos las funciones, variables y/o clases que deseamos exportar. 
Luego, podemos importar el módulo en otro archivo Python y utilizar las funciones, variables y/o clases 
definidas en él. Los módulos son una herramienta útil para organizar 
y reutilizar código en aplicaciones más grandes.
'''
#para importar modulos/clases enteras, la nomenclatura de los modulos no puede empezar con numero
import module 
#Llamado de funciones para importaciones de modulos enteros
module.sumValue(1,2,3) #Ademas de importar se llama, primero al modulo y despues a la funcion que queramos
module.printValue('Llamado de una funcion perteneciente a un modulo importado')

#para importar funciones/operaciones concretas de un modulo
from module import sumValue 
from module import printValue
#Llamado de funciones para importaciones de funciones concretas de un modulo, notar que no es necesario aclarar de que modulo salen
sumValue(1,2,1)
printValue('Llamado de funcion concreta importada')

#Importando modulos fuera de nuestro fichero y renombrar lo importado
from math import pi as PI

print(PI)
