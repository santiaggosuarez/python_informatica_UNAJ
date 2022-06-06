#Ejercicio 14: Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio aeróbico;
#la fórmula que se aplica cuando la persona no está entrenada: (220-edad)/10; si la persona está entrenada: (210-edad)/10.

def numero_de_pulsaciones(edad,entrenado):

  if entrenado.lower() == "si":
    resultado = (210 - edad)/10
  
  elif entrenado.lower() == "no":
    resultado = (220 - edad)/10
  
  return resultado
  
print("cada 10 segundos debe tener ",numero_de_pulsaciones(edad,entrenado)," pulsaciones.")
