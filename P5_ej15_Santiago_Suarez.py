#Implemente un programa que pida el ingreso de 10 numeros y luego imprima aquellos numeros ingresados mayores al promedio

num = int(input("ingrese un numero: "))
cant = 0
suma = 0
lista_num = []
lista_may = []

while cant < 9:
  lista_num.append(num)
  suma += num
  cant += 1
  num = int(input("ingrese un numero: "))

promedio = suma/cant

for i in lista_num:
  if i > promedio:
    lista_may.append(i)

print(lista_num)
print(promedio)
print(lista_may)
