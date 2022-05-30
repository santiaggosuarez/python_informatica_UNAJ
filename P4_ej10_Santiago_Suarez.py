#Ejercicio 10: Dadas 3 longitudes, decir mediante un mensaje si se forma o no un triángulo
#(cada lado tiene que ser menor que la suma de los otros dos).
#Escriba una función que recibe 3 parámetros para resolver el problema. Invoque la función en un programa.

def es_triangulo(long1,long2,long3):

  if long1 + long2 > long3 and long1 + long3 > long2 and long2 + long3 > long1:
    resultado = "es triangulo"
  
  else:
    resultado = "NO es triangulo"
  
  return resultado

long1 = float(input("ingrese una primera longitud: "))
long2 = float(input("ingrese una segunda longitud: "))
long3 = float(input("ingrese una tercera longitud: "))

print(es_triangulo(long1,long2,long3))
