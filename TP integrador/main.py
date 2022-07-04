lista_datos = [['Emiliano', 'Martinez', 'arq', 29, 1.95, 18, 0, 50.0], ['Franco', 'Armani', 'arq', 34, 1.89, 29, 0, 5.0], ['Cristian', 'Romero', 'def', 23, 1.85, 15, 2, 80.0], ['Nicolas', 'Otamendi', 'def', 33, 1.83, 70, 6, 15.0], ['Rodrigo', 'De Paul', 'med', 27, 1.8, 45, 11, 60.0], ['Angel', 'Di Maria', 'del', 33, 1.8, 123, 25, 65.0], ['Giovani', 'Lo Celso', 'med', 25, 1.77, 58, 8, 70.0], ['Lautaro', 'Martinez', 'del', 24, 1.74, 38, 20, 90.0], ['Lionel', 'Messi', 'del', 35, 1.69, 165, 86, 150.0], ['Julian', 'Alvarez', 'del', 21, 1.77, 8, 1, 60.0]]

#carga de datos
def carga_datos():
  lista = []
  for i in range(10):
      nombre = input("\nNombre: ")
      apellido = input("Apellido: ")
      posicion = input("Posición (ARQ, DEF, MED o DEL): ")
      while posicion.upper() != "ARQ" and posicion.upper() != "DEF" and posicion.upper() != "MED" and posicion.upper() != "DEL":
        posicion = input("Por favor ingrese una posición válida (ARQ, DEF, MED o DEL): ")
      edad = int(input("Edad: "))
      while len(str(edad)) > 2:
        edad = int(input("Por favor ingrese una edad válida: "))
      altura = float(input("Altura en metros: "))
      partidos = int(input("Cantidad de partidos jugados: "))
      goles = int(input("Goles: "))
      cotizacion = float(input("Cotización en millones $USD: "))
      datos = [nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion]
      lista.append(datos)
  return lista

def promedio_edad(lista):
  suma = 0
  cant = 0
  promedio = 0
  for i in lista:
    suma += i[3]
    cant += 1
  promedio = float(suma/cant)
  return promedio
#print("El promedio de edad en el plantel es de: " + str(promedio_edad(lista_datos)) + " años.")

def promedio_altura(lista):
  suma = 0
  cant = 0
  promedio = 0
  for i in lista:
    suma += i[4]
    cant += 1
  promedio = float(suma/cant)
  return promedio
#print("La altura promedio del plantel es de: " + str(promedio_altura(lista_datos)) + " mts.")

def promedio_valor(lista):
  suma = 0
  cant = 0
  promedio = 0
  for i in lista:
    suma += i[7]
    cant += 1
  promedio = float(suma/cant)
  return promedio
#print("El valor promedio del plantel es de: " + str(promedio_valor(lista_datos)) + " millones $USD.")

def goleador(lista):
  lista_goleador = []
  cant = 0
  for i in lista:
    if i[6] > cant:
      cant = i[6]
      nombre = i[0]
      apellido = i[1]
      goles = i[6]
      dato = [nombre + " " + apellido, goles]
      lista_goleador = dato
  return lista_goleador
#print(goleador(lista_datos))

def mas_partidos(lista):
  lista_mas_partidos = []
  cant = 0
  for i in lista:
    if i[5] > cant:
      cant = i[5]
      nombre = i[0]
      apellido = i[1]
      partidos = i[5]
      dato = [nombre + " " + apellido, partidos]
      lista_mas_partidos = dato
  return lista_mas_partidos
#print(mas_partidos(lista_datos))

def mas_viejo(lista):
  lista_viejo = []
  edad_mayor = 0
  for i in lista:
    if i[3] > edad_mayor:
      edad_mayor = i[3]
      nombre = i[0]
      apellido = i[1]
      edad = i[3]
      dato = [nombre + " " + apellido, edad]
      lista_viejo = dato
  return lista_viejo
#print(mas_viejo(lista_datos))

def mas_joven(lista):
  lista_joven = []
  edad_menor = 100
  for i in lista:
    if i[3] < edad_menor:
      edad_menor = i[3]
      nombre = i[0]
      apellido = i[1]
      edad = i[3]
      dato = [nombre + " " + apellido, edad]
      lista_joven = dato
  return lista_joven
#print(mas_joven(lista_datos))

def mas_caro(lista):
  lista_caro = []
  valor_max = 0
  for i in lista:
    if i[7] > valor_max:
      valor_max = i[7]
      nombre = i[0]
      apellido = i[1]
      valor = i[7]
      dato = [nombre + " " + apellido, valor]
      lista_caro = dato
  return lista_caro
print(mas_caro(lista_datos))
