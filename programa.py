#Generar un archivo de LOG que contenga los siguientes datos de cada ítem: a. "id" del ítem, "title" del item, "category_id" donde está
#publicado, "name" de la categoría.

import random
#Defino mis vectores.

cantidad_de_datos = 2

id = [0] * cantidad_de_datos       #Vector N1  

title = [0] * cantidad_de_datos    #Vector N2

category_id = [0] * cantidad_de_datos  #Vector N3

name = [0] * cantidad_de_datos         #Vector N4

#Procedo a cargar los vectores.

for i in range(cantidad_de_datos):
    id[i] = int(input("Ingrese su numero de ID por teclado:"))
    title[i] = str(input("Ingrese su titulo por teclado: "))
    category_id[i] = int(input("Ingrese el ID numerico de su categoria por teclado:"))
    name[i] = str(input("Ingrse el nombre de la categoria por teclado: "))


#Muestro los vectores cargados al usuario

for i in range(cantidad_de_datos):
    id[i] = print("Los datos del vector en la posicion N", i,  "son:", "ID:", id[i], "// TITULO:", title[i],"// CATEGORIA:", category_id[i], "// ID DE CATEGORIA:", name[i])

