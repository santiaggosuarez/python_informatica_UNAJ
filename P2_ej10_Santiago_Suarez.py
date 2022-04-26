#pedimos ancho y largo para calcular el area del terreno

ancho = input("ingrese ancho del terreno: ")
largo = input("ingrese largo del terreno: ")
area = int(ancho) * int(largo)

#calculamos el area de los paneles de pasto

paneles = 0.60*0.60

#calculamos la cantidad de paneles y redondeamos para arriba con ROUND para que no dé un número flotante

cantidad_paneles = round(area/paneles)

#final

print("necesita comprar " + str(cantidad_paneles) + " paneles de pasto.")
