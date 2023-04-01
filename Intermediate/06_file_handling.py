# File Handling

# .txt file 
txt_file = open("Intermediate/my_file.txt", "r+")

print(txt_file.read())  # Leer todo el archivo
print(txt_file.read(5))  # Leer los primeros 5 caracteres del archivo
print(txt_file.readline())  # Leer la primera línea del archivo
print(txt_file.readlines())  # Leer todas las líneas del archivo como una lista

for line in txt_file.readlines():  # Iterar sobre todas las líneas del archivo
    print(line)

txt_file.write("\nAlgo mas ")  # Escribir en el archivo
txt_file.close()  # Cerrar el archivo

txt_file = open("Intermediate/my_file.txt", "r+")
print(txt_file.read())  # Leer todo el archivo nuevamente

# .json file
import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Kevin",
    "surname": "Caria",
    "age": 29,
    "languages": ["Python", "Java"]
}  # Esto es un diccionario

json.dump(json_test, json_file, indent=2)  # Se guarda como json
json_file.close()  # Cerrar el archivo

# Abrir y mostrar por consola el archivo json
with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Parsear el archivo json a un diccionario
json_dict = json.load(open('Intermediate/my_file.json'))

# .csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language"])
csv_writer.writerow(["Kevin", "Caria", 29, "Python"])

csv_file.close()

# Leer el archivo csv
with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xml file
import xml.etree.ElementTree as ET

# Crear un archivo xml
root = ET.Element("person")
name = ET.SubElement(root, "name")
name.text = "Kevin"
surname = ET.SubElement(root, "surname")
surname.text = "Caria"
age = ET.SubElement(root, "age")
age.text = "29"

tree = ET.ElementTree(root)
tree.write("Intermediate/my_file.xml")

# Leer el archivo xml
tree = ET.parse("Intermediate/my_file.xml")
root = tree.getroot()
print(root.tag)
print(root[0].tag)
print(root[0].text)
print(root[1].tag)
print(root[1].text)
print(root[2].tag)
print(root[2].text)

