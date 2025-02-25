import math
def rellenar_con_ceros(valor, longitud):
    # Rellena el valor con ceros a la izquierda hasta la longitud especificada
    return valor.zfill(longitud)

import math

def calcular_dias_trabajados(horas):
    # Redondear al siguiente número entero que sea múltiplo de 3 horas
    return math.ceil(horas / 3)

def generar_clave():
    # Preguntar al usuario cuántos empleados tiene
    num_empleados = int(input("¿Cuántos empleados tienes? "))

    # Iniciar la lista para las claves generadas
    claves_empleados = []

    # Recopilar datos de cada empleado
    for i in range(num_empleados):
        print(f"\nEmpleado {i + 1}:")

        # 1. Número de empleado
        num_empleado = input("Número de empleado (10 dígitos): ")
        num_empleado = rellenar_con_ceros(num_empleado, 10)

        # 2. Fecha de inicio del periodo (8 caracteres)
        fecha_inicio = input("Fecha de inicio del periodo (DDMMYYYY): ")
        fecha_inicio = rellenar_con_ceros(fecha_inicio, 8)

        # 3. Fecha de fin del periodo (8 caracteres)
        fecha_fin = input("Fecha de fin del periodo (DDMMYYYY): ")
        fecha_fin = rellenar_con_ceros(fecha_fin, 8)

        # 4. Horas a pagar (máximo 24 horas, 8 dígitos con ceros a la izquierda y 4 ceros a la derecha)
        horas = int(input("Horas a pagar (máximo 24 horas): "))
        if horas > 24:
            print("Error: No se pueden más de 24 horas.")
            continue
        horas_pagar =  "00000000" + rellenar_con_ceros(str(horas), 2) + "0000"

        # 5. Unidad administrativa (4 dígitos)
        unidad_administrativa = input("Unidad administrativa (4 dígitos): ")
        unidad_administrativa = rellenar_con_ceros(unidad_administrativa, 4)

        # 6. Calcular los días trabajados (1 día = 3 horas)
        dias_trabajados = calcular_dias_trabajados(horas)
        dias_trabajados = str(dias_trabajados).zfill(2)

        # Concatenar todos los datos para generar la clave
        clave = num_empleado + "4306" + fecha_inicio + fecha_fin + horas_pagar + unidad_administrativa + dias_trabajados
        clave = clave[:50]  # Asegurarse de que la clave no exceda 50 caracteres

        # Agregar la clave generada a la lista
        claves_empleados.append(clave)
        print(f"Clave generada para el empleado {i + 1}: {clave}")

    return claves_empleados

# Ejecutar el programa
claves = generar_clave()

# Mostrar las claves generadas
print("\nClaves generadas para todos los empleados:")
for i, clave in enumerate(claves):
    print(f"Empleado {i + 1}: {clave}")