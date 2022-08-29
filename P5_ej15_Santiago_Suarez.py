#Implemente un programa que pida el ingreso de 10 numeros y luego imprima aquellos numeros ingresados mayores al promedio

suma = 0
lista_num = []
lista_may = []

for i in range(10):
  num = int(input("ingrese un numero: "))
  lista_num.append(num)
  suma += num

promedio = suma/10

for i in lista_num:
  if i > promedio:
    lista_may.append(i)

print(lista_num)
print(promedio)
print(lista_may)
