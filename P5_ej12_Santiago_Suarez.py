#Ejercicio 12: Dada la siguiente lista [1, 14, 56, 43, 23, 46, 58, 123, 67 ]
#escribir un programa que muestre el número más alto.

lista = [1, 14, 56, 43, 23, 46, 58, 123, 67 ]

#igualo maximo al primer elemento de la lista para que funcione con listas que contengan numeros negativos
max = lista[0]

#recorro la lista comparando cada numero con el maximo para saber cual es el mayor
for num in lista:
  if num > max:
    max = num

print(max)
