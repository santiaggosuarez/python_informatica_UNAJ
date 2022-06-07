#Ejercicio 13: Escriba un programa que solicite nombres de localidades y códigos postales al usuario hasta que se ingresa el código postal 0. Debe generar una lista con todos los valores ingresados e imprimirla.

localidad = input("ingrese una localidad: ")
cp = int(input("ingrese su código postal ('0' para finalizar): "))
lista = []

while cp != 0:
  lista.append("localidad: " + localidad + " CP: " + str(cp))
  localidad = input("ingrese una localidad: ")
  cp = int(input("ingrese su código postal ('0' para finalizar): "))

print()
for x in lista:
    print(x)
