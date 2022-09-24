num = input("Ingrese un numero entero: ")
resultado = len(num)

while resultado <=6:
    resultado = len(num)
    if resultado == 1:
      print("unidad")
      num = input("Ingrese un nuevo numero entero: ")
    elif resultado == 2:
      print("decena")
      num = input("Ingrese un nuevo numero entero: ")
    elif resultado == 3:
      print("centena")
      num = input("Ingrese un nuevo numero entero: ")
    elif resultado == 4:
      print("milésima")
      num = input("Ingrese un nuevo numero entero: ")
    elif resultado == 5:
      print("decena de mil")
      num = input("Ingrese un nuevo numero entero: ")
    else:
      print("centena de mil")
      num = input("Ingrese un nuevo numero entero: ")

print("el ciclo termino")