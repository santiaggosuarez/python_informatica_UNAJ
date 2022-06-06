#Ejercicio 1: Escribir un programa que muestre la tabla de multiplicar de un número introducido por teclado por el usuario.

num = int(input("ingrese un número para saber su tabla de multiplicar: "))
mult = 1

while mult < 11:
  print(num, " x ", mult, " = ", num*mult)
  mult +=1
