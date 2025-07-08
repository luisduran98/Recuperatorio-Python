# 5.Ejercicio 5 - Registro de ventas en JSON
# Permitir ingresar ventas (cliente, producto, cantidad, total).
# Guardarlas en un archivo JSON.
# Luego, leer el archivo y mostrar:
# - Ventas totales realizadas
# - Monto total vendido
# - Listado de clientes únicos

import json

ventas = []
nombre_json = "Ventas"

while True:

    cliente = input("Nombre del cliente: ")
    while not cliente.isalpha():
        cliente = input("Nombre del cliente: ")

    producto = input("Ingrese el Producto: ")
    while not producto.isalpha():
        producto = input("Ingrese el Producto: ")

    cantidad = input("Ingrese la cantidad: ")
    while not cantidad.isdigit():
        print("Tiene que ser un numero")
        cantidad = input("Ingrese la cantidad: ")
    while int(cantidad) < 1:
        print("tiene que ser mayor a 0")
        cantidad = input("Ingrese la cantidad: ")

    precio = input("Ingrese el precio: ")
    while not precio.isdigit():
        print("Tiene que ser un numero")
        precio = input("Ingrese el precio: ")
    while int(precio) < 1:
        print("tiene que ser mayor a 0")
        precio = input("Ingrese el precio: ")

    total = int(precio) * int(cantidad)
    ventas.append({"cliente": cliente.lower(), "producto":producto.lower(), "cantidad": int(cantidad),"precio": int(precio), "total": total})

    pregunta = input("deseas seguir agregando pacientes? (si o no)")
    while not pregunta.isalpha() and pregunta.lower() != "si" and pregunta.lower() != "no":
        pregunta = input("deseas seguir agregando pacientes? (si o no)")

    if pregunta == "no":
        break


with open(nombre_json, "w",encoding="utf-8") as data:
    json.dump(ventas, data, indent=4)

with open(nombre_json, "r", encoding="utf-8") as data:
    cache = json.load(data)
    print(cache)

# - Ventas totales realizadas
print(f"Ventas totales realizadas: {len(cache)}")

# - Monto total vendido
sum_ventas = 0
for elem in cache:
    sum_ventas += elem["total"]
print(f"El monto total vendido es de {sum_ventas}")

# - Listado de clientes únicos
clientes = []
for elem in cache:
    clientes.append(elem["cliente"])
clientes_filtrados = set(clientes)
print(f"Los clientes unicos son {clientes_filtrados}")

