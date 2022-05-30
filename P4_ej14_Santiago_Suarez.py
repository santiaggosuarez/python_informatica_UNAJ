#Ejercicio 14: Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio aeróbico;
#la fórmula que se aplica cuando la persona no está entrenada: (220-edad)/10; si la persona está entrenada: (210-edad)/10.

def entrenada(respuesta):
  return respuesta == si or "si" or "SI" or "sí" or "Sí"

def numero_de_pulsaciones(edad,entrenada):

  if entrenada:
    resultado = (210 - edad)/10
  
  else:
    resultado = (220 - edad)/10
  
  return resultado

respuesta = input("usted está entrenado/a?: ")
edad = int(input("ingrese su edad: "))

print("cada 10 segundos debe tener ",numero_de_pulsaciones(edad,entrenada)," pulsaciones.")
