#Escriba un programa que lea números de documentos de identidad de
#personas hasta que se ingrese el número “999”. Debe imprimir la #cantidad de números de documentos menores que 20.000.000.

cont = 0
dni = int(input("ingrese un DNI (para finalizar ingrese 999): "))

while dni != 999:
  if dni < 20000000:
    cont += 1
    dni = int(input("ingrese un DNI (para finalizar ingrese 999): "))
  else:
    dni = int(input("ingrese un DNI (para finalizar ingrese 999): "))

print("hay " + str(cont) + " documentos menores que 20.000.000")
