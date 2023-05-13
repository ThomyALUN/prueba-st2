from funciones import *
from tablaHash import HashTable

archivo = "ArchNombres1.txt"

with open(archivo, "r", encoding="utf-8") as archivo:
    datos=archivo.readlines()

print(datos)

while True:
    try:
        tamanio=input("Ingrese el tamaño de la tabla: ")
        tamanio=int(tamanio)
    except ValueError:
        print("El valor debe ser un número")
    else:
        if tamanio<len(datos):
            print("El tamaño no puede ser menor que la cantidad de datos")
        else:
            break

tabla=HashTable(tamanio, 0)
for i in range(len(datos)):
    tabla.ingresarDatos(int(datos[i][0]))
print("")
print(tabla)
print("")
print(tabla.getTabla())