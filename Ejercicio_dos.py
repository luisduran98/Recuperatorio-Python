# 2.Ejercicio 2 - Gestión de notas

# Cargar una lista con las notas de 10 alumnos.
Alumnos = [10,9,7,5,4,3,2,3,8,7]

# Implementar una función que reciba la lista de notas y retorne:

# Mostrar los resultados.

def notas(arg:list):
    contador = 0
    sum_notas = 0
    mayor_nota = 0
    posicion = 0

    for i in range(0,len(arg)):
        sum_notas += arg[i]

        if arg[i] >= 6:
            contador += 1

    for y in range(1,len(arg)):
        mayor_nota = arg[0]
        if arg[y] > mayor_nota:
            mayor_nota = arg[y]
            posicion = y
# Mostrar los resultados.

# - Cantidad de aprobados (nota >= 6)
    print(f"La cantidad de aprobados es {contador}")

# - Nota promedio general
    print(f"La nota promedio general es: {sum_notas/len(arg)}")

# - Mayor nota y su posición en la lista
    print(f"Mayor nota: {mayor_nota} y su posicion es {posicion}")


notas(Alumnos)

