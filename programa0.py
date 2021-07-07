#Recorrer todos los ítems publicados por el seller_id = 179571326 del
#site_id = "MLA"
import random
#Defino un la cantidad de items publicados.

cantidad_de_items = 25

#Defino un vector para almacenar los items
id = [0] * cantidad_de_items

#Cargo los items del vector de manera aleatoria

for i in range(cantidad_de_items):
    id[i] = random.randint(1, 50)

#Muestro los items publicados recorriendo el vector.
for i in range(cantidad_de_items):
    id[i] = print("El item en la posicion", i, "es", id[i])
