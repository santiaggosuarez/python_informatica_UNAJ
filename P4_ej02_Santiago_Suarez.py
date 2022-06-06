#Ejercicio 2: Escribir un programa que lea dos números “n” y “m” y determine si n es divisible por m, mostrando el siguiente mensaje por pantalla:
# “El número n es/no es divisible por m”. Reemplazar n y m por los números correspondientes.

def dos_numeros(n,m):
  if (n%m) == 0:
    resultado = "el número " + str(n) + " es divisible por " + str(m)
  
  else:
    resultado =  "el número " + str(n) + " NO es divisible por " + str(m)

  return resultado

print(dos_numeros(n,m))
