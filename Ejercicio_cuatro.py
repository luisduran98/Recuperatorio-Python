# 4.Ejercicio 4 - Inventario de productos
# Usar un diccionario para registrar productos.
productos = []
bandera = True
# Clave: código (str), Valor: tupla con (nombre, stock, precio).
# Implementar un menú con las opciones:
# 1. Agregar producto
# 2. Modificar stock
# 3. Mostrar productos con stock menor a 5
# 4. Salir
# Validar entradas numéricas donde sea necesario.

while True:
    print("1. Agregar producto")
    print("2. Modificar stock)")
    print("3. Mostrar productos con stock menor a 5")
    print("4. Salir")
    pregunta = input("Elige una opcion: ")
    while not pregunta.isdigit():
        print("debe ser un numero de el 1 al 4 :")
        pregunta = input("Elige una opcion: ")
    while int(pregunta) < 1 or int(pregunta) > 4:
        print("debe ser un numero de el 1 al 4 :")
        pregunta = input("Elige una opcion: ")
    
    if int(pregunta) == 1:
        codigo = input("Coloca el codigo: ")
        while not codigo.isalpha():
            print("deben ser solo letras")
            codigo = input("Coloca el codigo: ")
        # for i in range(len(productos)):
            # if codigo == productos[]
    break