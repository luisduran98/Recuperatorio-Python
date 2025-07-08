# 1.Ejercicio 1 - Registro de pacientes
# Solicitar al usuario que ingrese los datos de pacientes (nombre, edad y síntoma principal).

# Validar que la edad sea mayor a 0.

# Finalizar el ingreso con un nombre vacío, o pueden buscar otra salida del bucle.
# Al finalizar, mostrar:
# - Promedio de edades
# - Cantidad de pacientes mayores de 60
# - Porcentaje de pacientes con síntoma 'fiebre' (ignorar mayúsculas/minúsculas)

edades = []
sintomas = []
contador = 0
while True:
    nombre = input("Nombre del paciente: ")
    while not nombre.isalpha():
        print("no debe tener numeros el nombre")
        nombre = input("Nombre del paciente: ")

    edad = input("Coloca la edad del paciente: ")
    while not edad.isdigit():
        print("la edad tiene que ser un numero no un digito")
        edad = input("Coloca la edad del paciente: ")

    while int(edad) < 0:
        print("la edad tiene que ser mayor a 0")
        edad = input("Coloca la edad del paciente: ")

    sintoma = input("Cual es el sintoma principal?: ")
    while not sintoma.isalpha():
        print("no debe tener numeros el sintoma")
        sintoma = input("Sintoma Principal del paciente: ")

    edades.append(int(edad))
    sintomas.append(sintoma)

    pregunta = input("deseas seguir agregando pacientes? (si o no)")
    while not pregunta.isalpha() and pregunta.lower() != "si" and pregunta.lower() != "no":
        pregunta = input("deseas seguir agregando pacientes? (si o no)")

    if pregunta == "no":
        break

for item in edades:
    contador += item
print(f"El promedio de edades es de {int(contador/len(edades))} años")
contador = 0

for item in edades:
    if item > 60:
        contador += 1
print(f"La cantidad de pacientes mayores a 60 es {contador}")
contador = 0

for item in sintomas:
    if item.lower() == "fiebre":
        contador += 1
print(f"La cantidad de pacientes con fiebre es de {contador}")
