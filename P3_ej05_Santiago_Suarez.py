#lista de meses

meses = [["ERROR","ingrese un numero del 1 al 12"],["enero",31],["febrero",28],["marzo",31],["abril",30],["mayo",31],["junio",30],["julio",31],["agosto",31],["septiembre",30],["octubre",31],["noviembre",30],["diciembre",31]]

#funcion de cuantos dias tiene el mes (x)

def cuantos_dias(x):
  return meses[x][1]

#damos valor a la variable x

x = int(input("ingrese el número del mes para saber su cantidad de días: "))
print(cuantos_dias(x))
