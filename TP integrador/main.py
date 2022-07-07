lista_datos = [['Emiliano', 'Martinez', 'arq', 29, 195, 18, 0, 50.0], ['Franco', 'Armani', 'arq', 34, 189, 29, 0, 5.0], ['Cristian', 'Romero', 'def', 23, 185, 15, 2, 80.0], ['Nicolas', 'Otamendi', 'def', 33, 183, 70, 6, 15.0], ['Rodrigo', 'De Paul', 'med', 27, 180, 45, 11, 60.0], ['Angel', 'Di Maria', 'del', 33, 180, 123, 25, 65.0], ['Giovani', 'Lo Celso', 'med', 25, 177, 58, 8, 70.0], ['Lautaro', 'Martinez', 'del', 24, 174, 38, 20, 90.0], ['Lionel', 'Messi', 'del', 35, 169, 165, 86, 150.0], ['Julian', 'Alvarez', 'del', 21, 177, 8, 1, 60.0]]

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
      altura = float(input("Altura en centimetros: "))
      while len(str(altura)) > 3:
        altura = int(input("Por favor ingrese una altura válida: "))
      partidos = int(input("Cantidad de partidos jugados: "))
      goles = int(input("Goles: "))
      cotizacion = float(input("Cotización en millones $USD: "))
      datos = [nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion]
      lista.append(datos)
  return lista

def promedio(lista,indice_a_promediar):
  suma = 0
  cant = 0
  promedio = 0
  for i in lista:
    suma += i[indice_a_promediar]
    cant += 1
  promedio = float(suma/cant)
  return promedio

#edad
edad = promedio(lista_datos,3)
#print(edad)
#altura
alt = promedio(lista_datos,4)
#print(alt)
#valor
val = promedio(lista_datos,7)
#print(val)

def obtener_mayor(lista,indice_a_comparar):
  lista2 = []
  cant = 0
  for i in lista:
    if i[indice_a_comparar] > cant:
      cant = i[indice_a_comparar]
      nombre = i[0]
      apellido = i[1]
      valor = i[indice_a_comparar]
      dato = [nombre + " " + apellido, valor]
      lista2 = dato
  return lista2

def obtener_menor(lista,indice_a_comparar):
  lista2 = []
  cant = 999999
  for i in lista:
    if i[indice_a_comparar] < cant:
      cant = i[indice_a_comparar]
      nombre = i[0]
      apellido = i[1]
      valor = i[indice_a_comparar]
      dato = [nombre + " " + apellido, valor]
      lista2 = dato
  return lista2

#goleador
gol = obtener_mayor(lista_datos,6)
#print(gol)
#mas partidos
part = obtener_mayor(lista_datos,5)
#print(part)
#mas viejo
viejo = obtener_mayor(lista_datos,3)
#print(viejo)
#mas caro
caro = obtener_mayor(lista_datos,7)
#print(caro)
#mas joven
joven = obtener_menor(lista_datos,3)
#print(joven)

def actualizar_datos(lista):
  print("\nIngrese los datos del jugador a eliminar:")
  nombre_borrar = input("\nIngrese el nombre: ")
  apellido_borrar = input("Ingrese el apellido: ")
  
  for i in lista:
    #borrar si existe
    if i[0].lower() == nombre_borrar.lower() and i[1].lower() == apellido_borrar.lower():
      lista.remove(i)
      #agregar jugador nuevo
      print("\nIngrese los datos del jugador a agregar:")
      nombre = input("\nNombre: ")
      apellido = input("Apellido: ")
      posicion = input("Posición (ARQ, DEF, MED o DEL): ")
      while posicion.upper() != "ARQ" and posicion.upper() != "DEF" and posicion.upper() != "MED" and posicion.upper() != "DEL":
        posicion = input("Por favor ingrese una posición válida (ARQ, DEF, MED o DEL): ")
      edad = int(input("Edad: "))
      while len(str(edad)) > 2:
        edad = int(input("Por favor ingrese una edad válida: "))
      altura = float(input("Altura en centimetros: "))
      while len(str(altura)) > 3:
        altura = int(input("Por favor ingrese una altura válida: "))
      partidos = int(input("Cantidad de partidos jugados: "))
      goles = int(input("Goles: "))
      cotizacion = float(input("Cotización en millones $USD: "))
      datos = [nombre,apellido,posicion,edad,altura,partidos,goles,cotizacion]
      lista.append(datos)
    return lista

def imprimir_lista_de_listas(lista):
  for i in lista:
    for j in i:
      print(j)

def cantidad_por_posicion(lista):
  pos = input("\nIngrese la posición: ")
  while pos.upper() != "ARQ" and pos.upper() != "DEF" and pos.upper() != "MED" and pos.upper() != "DEL":
    pos = input("Por favor ingrese una posición válida (ARQ, DEF, MED o DEL): ")
  lista_pos = []

  for i in lista:
    if i[2] == pos:
      dato = [pos.upper() + ": " + i[0] + " " + i[1]]
      lista_pos.append(dato)

  return imprimir_lista_de_listas(lista_pos)
  

def menu(lista):
  print("\nMENÚ")
  salir = False
  while not salir:
    op = input("\nIngrese una opción:\n 1 - Ver lista de jugadores por posición.\n 2 - Obtener promedio de edad del plantel.\n 3 - Obtener promedio de altura del plantel.\n 4 - Obtener valor promedio del plantel.\n 5 - Ver goleador.\n 6 - Ver jugador con más presencias.\n 7 - Ver jugador más jovén.\n 8 - Actualizar datos.\n 0 - Salir.\n")

    if op == "1":
      cantidad_por_posicion(lista)
    elif op == "2":
      print(promedio(lista,3))
    elif op == "3":
      print(promedio(lista,4))
    elif op == "4":
      print(promedio(lista,7))
    elif op == "5":
      print(obtener_mayor(lista,6))
    elif op == "6":
      print(obtener_mayor(lista,5))
    elif op == "7":
      print(obtener_menor(lista,3))
    elif op == "8":
      actualizar_datos(lista)
    elif op == "0":
      salir = True
    else:
      print("\nDato inválido")

menu(lista_datos)
