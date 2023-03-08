# Dates

# Importamos las clases necesarias de datetime
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

'''
datetime en Python combina tanto la fecha como la hora, con información sobre la zona horaria. 
Es útil para trabajar con fechas y horas específicas, como calcular la diferencia entre dos fechas
 y horas, o convertir una fecha y hora a un formato legible para los humanos.
'''
# Obtenemos la fecha y hora actual
now = datetime.now()

# Función para imprimir la fecha y hora dada
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# Imprimimos la fecha y hora actual
print_date(now)

# Creamos una fecha para el 1 de enero de 2023 y la imprimimos
year_2023 = datetime(2023, 1, 1)
print_date(year_2023)

'''
time en Python, como mencioné anteriormente, representa solo la hora actual en segundos o 
fracciones de segundos. Es útil para medir la duración de una operación o para crear un temporizador.
'''
# Creamos una hora y la imprimimos
current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

'''
date en Python representa solo una fecha sin información de hora o zona horaria. 
Es útil para trabajar con fechas específicas, como calcular la diferencia entre dos fechas 
o verificar si una fecha está dentro de un rango de fechas.
'''
# Obtenemos la fecha actual y la imprimimos
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Creamos una fecha y la imprimimos
current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Añadimos un mes a la fecha y obtenemos el mes
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

# Calculamos la diferencia entre dos fechas e imprimimos la diferencia
diff = year_2023 - now
print(diff)

# Calculamos la diferencia entre dos fechas diferentes e imprimimos la diferencia
diff = year_2023.date() - current_date
print(diff)

'''
timedelta es una clase de Python que representa una duración de tiempo, 
que puede ser un intervalo de días, horas, minutos, segundos y microsegundos. 
Se utiliza comúnmente para realizar operaciones matemáticas con fechas y horas, 
como calcular la diferencia entre dos fechas o agregar una cantidad de tiempo a una fecha determinada.
'''
# Creamos dos objetos timedelta y realizamos operaciones con ellos
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
