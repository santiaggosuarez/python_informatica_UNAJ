#Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número introducido por teclado por el usuario.

def tabla_de_multiplicar(num):
  mult = 1
  
  while mult < 11:
    print(num, " x ", mult, " = ", num*mult)
    mult +=1

n = int(input("ingrese un número para saber su tabla de multiplicar: "))
tabla_de_multiplicar(n)
