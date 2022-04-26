nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
nacimiento = input("ingrese su fecha de nacimiento (DD/MM/AAAA): ")

print("su nueva clave es: " + nombre[0] + apellido[0] + "_" + nacimiento[-4:])
