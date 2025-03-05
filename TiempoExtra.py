import tkinter as tk
from tkinter import messagebox
import math

def rellenar_con_ceros(valor, longitud):
    return valor.zfill(longitud)

def calcular_dias_trabajados(horas):
    return math.ceil(horas / 3)

def validar_fecha(fecha):
    if len(fecha) != 8 or not fecha.isdigit():
        return False
    dia, mes, anio = int(fecha[:2]), int(fecha[2:4]), int(fecha[4:])
    if not (1 <= mes <= 12 and 1 <= dia <= 31):
        return False
    return True

def guardar_datos():
    global empleado_actual, num_empleados, claves_empleados
    
    num_empleado = rellenar_con_ceros(entry_num_empleado.get(), 10)
    
    try:
        horas = int(entry_horas_pagar.get())
        if horas > 24:
            messagebox.showerror("Error", "No se pueden registrar más de 24 horas.")
            return
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de horas.")
        return
    
    horas_pagar = "00000000" + rellenar_con_ceros(str(horas), 2) + "0000"
    unidad_administrativa = rellenar_con_ceros(entry_unidad_administrativa.get(), 4)
    
    dias_trabajados = str(calcular_dias_trabajados(horas)).zfill(2)
    clave = num_empleado + clave_codigo + fecha_inicio + fecha_fin + horas_pagar + unidad_administrativa + dias_trabajados
    clave = clave[:50]
    claves_empleados.append(clave)
    
    entry_num_empleado.delete(0, tk.END)
    entry_horas_pagar.delete(0, tk.END)
    entry_unidad_administrativa.delete(0, tk.END)
    
    empleado_actual += 1
    if empleado_actual < num_empleados:
        label_empleado.config(text=f"Empleado {empleado_actual + 1}")
    else:
        mostrar_claves()
        frame_empleado.pack_forget()

def mostrar_claves():
    resultado_text.delete(1.0, tk.END)
    for i, clave in enumerate(claves_empleados):
        resultado_text.insert(tk.END, f"Empleado {i + 1}: {clave}\n")

def iniciar_ingreso():
    global empleado_actual, num_empleados, claves_empleados, clave_codigo, fecha_inicio, fecha_fin
    try:
        num_empleados = int(entry_num_empleados.get())
        if num_empleados <= 0:
            messagebox.showerror("Error", "El número de empleados debe ser mayor a 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de empleados.")
        return
    
    clave_tipo = menu_tipo_trabajo.get()
    if clave_tipo == "Tiempos Extra":
        clave_codigo = "4306"
    elif clave_tipo == "Guardias":
        clave_codigo = "1170"
    elif clave_tipo == "Prima Dominical":
        clave_codigo = "1621"
    else:
        messagebox.showerror("Error", "Seleccione un tipo de trabajo válido.")
        return
    
    fecha_inicio = entry_fecha_inicio.get()
    fecha_fin = entry_fecha_fin.get()
    
    if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
        messagebox.showerror("Error", "Ingrese fechas válidas en formato DDMMYYYY.")
        return
    
    empleado_actual = 0
    claves_empleados = []
    label_empleado.config(text=f"Empleado 1")
    frame_empleado.pack(pady=10)

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Claves de Empleados")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Número de empleados:").grid(row=0, column=0)
entry_num_empleados = tk.Entry(frame)
entry_num_empleados.grid(row=0, column=1)

tk.Label(frame, text="Tipo de trabajo:").grid(row=1, column=0)
menu_tipo_trabajo = tk.StringVar()
tipo_trabajo_dropdown = tk.OptionMenu(frame, menu_tipo_trabajo, "Tiempos Extra", "Guardias", "Prima Dominical")
tipo_trabajo_dropdown.grid(row=1, column=1)

tk.Label(frame, text="Fecha inicio (DDMMYYYY):").grid(row=2, column=0)
entry_fecha_inicio = tk.Entry(frame)
entry_fecha_inicio.grid(row=2, column=1)

tk.Label(frame, text="Fecha fin (DDMMYYYY):").grid(row=3, column=0)
entry_fecha_fin = tk.Entry(frame)
entry_fecha_fin.grid(row=3, column=1)

tk.Button(frame, text="Iniciar ingreso", command=iniciar_ingreso).grid(row=4, column=0, columnspan=2, pady=10)

frame_empleado = tk.Frame(root)
label_empleado = tk.Label(frame_empleado, text="Empleado 1", font=("Arial", 12, "bold"))
label_empleado.pack()

tk.Label(frame_empleado, text="Número de empleado:").pack()
entry_num_empleado = tk.Entry(frame_empleado)
entry_num_empleado.pack()

tk.Label(frame_empleado, text="Horas a pagar (máx 24h):").pack()
entry_horas_pagar = tk.Entry(frame_empleado)
entry_horas_pagar.pack()

tk.Label(frame_empleado, text="Unidad administrativa:").pack()
entry_unidad_administrativa = tk.Entry(frame_empleado)
entry_unidad_administrativa.pack()

tk.Button(frame_empleado, text="Guardar y continuar", command=guardar_datos).pack(pady=10)

resultado_text = tk.Text(root, height=10, width=60)
resultado_text.pack(pady=10)

root.mainloop()
