#Ejercicio 6: Desarrollar un programa en el que se ingrese un año de nacimiento e indique si la persona es bebé, menor, adolescente, adulto o adulto mayor.

#defino una función para calcular su edad en base a su año de nacimiento

def edad_persona(año_nacimiento):
  edad = 2022 - año_nacimiento
  
  return edad

#función para decir en que etapa de la vida se encuentra

def etapa_persona(edad_persona):
  
  if edad_persona > -1 and edad_persona <= 2:
    resultado = "bebé"
  
  elif edad_persona > 2 and edad_persona <= 12:
    resultado = "menor"
  
  elif edad_persona > 12 and edad_persona <= 18:
    resultado = "adolescente"
  
  elif edad_persona > 18 and edad_persona <= 75:
    resultado = "adulto"
  
  elif edad_persona > 75:
    resultado = "adulto mayor"

  else:
    resultado ="ERROR año inválido"
  
  return resultado

print(etapa_persona(edad_persona(año_nacimiento)))
