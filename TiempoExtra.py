import tkinter as tk
from tkinter import messagebox
import math

def rellenar_con_ceros(valor, longitud):
    return valor.zfill(longitud)

def calcular_dias_trabajados(horas):
    return math.ceil(horas / 3)

def generar_clave():
    try:
        num_empleados = int(entry_num_empleados.get())
        if num_empleados <= 0:
            messagebox.showerror("Error", "El número de empleados debe ser mayor a 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de empleados.")
        return
    
    claves_empleados.clear()
    
    for i in range(num_empleados):
        num_empleado = rellenar_con_ceros(entry_num_empleado[i].get(), 10)
        fecha_inicio = rellenar_con_ceros(entry_fecha_inicio[i].get(), 8)
        fecha_fin = rellenar_con_ceros(entry_fecha_fin[i].get(), 8)
        
        try:
            horas = int(entry_horas_pagar[i].get())
            if horas > 24:
                messagebox.showerror("Error", f"Empleado {i + 1}: No se pueden más de 24 horas.")
                return
        except ValueError:
            messagebox.showerror("Error", f"Empleado {i + 1}: Ingrese un número válido de horas.")
            return
        
        horas_pagar = "00000000" + rellenar_con_ceros(str(horas), 2) + "0000"
        unidad_administrativa = rellenar_con_ceros(entry_unidad_administrativa[i].get(), 4)
        
        dias_trabajados = str(calcular_dias_trabajados(horas)).zfill(2)
        clave = num_empleado + "4306" + fecha_inicio + fecha_fin + horas_pagar + unidad_administrativa + dias_trabajados
        clave = clave[:50]
        claves_empleados.append(clave)
    
    mostrar_claves()

def mostrar_claves():
    resultado_text.delete(1.0, tk.END)
    for i, clave in enumerate(claves_empleados):
        resultado_text.insert(tk.END, f"Empleado {i + 1}: {clave}\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Claves de Empleados")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Número de empleados:").grid(row=0, column=0)
entry_num_empleados = tk.Entry(frame)
entry_num_empleados.grid(row=0, column=1)

tk.Button(frame, text="Generar formulario", command=lambda: crear_formulario()).grid(row=0, column=2)

def crear_formulario():
    try:
        num_empleados = int(entry_num_empleados.get())
        if num_empleados <= 0:
            messagebox.showerror("Error", "El número de empleados debe ser mayor a 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido de empleados.")
        return
    
    global entry_num_empleado, entry_fecha_inicio, entry_fecha_fin, entry_horas_pagar, entry_unidad_administrativa, claves_empleados
    entry_num_empleado = []
    entry_fecha_inicio = []
    entry_fecha_fin = []
    entry_horas_pagar = []
    entry_unidad_administrativa = []
    claves_empleados = []
    
    for widget in frame_formulario.winfo_children():
        widget.destroy()
    
    for i in range(num_empleados):
        tk.Label(frame_formulario, text=f"Empleado {i + 1}").grid(row=i*5, column=0, columnspan=2)
        
        tk.Label(frame_formulario, text="Número de empleado:").grid(row=i*5+1, column=0)
        entry = tk.Entry(frame_formulario)
        entry.grid(row=i*5+1, column=1)
        entry_num_empleado.append(entry)
        
        tk.Label(frame_formulario, text="Fecha inicio (DDMMYYYY):").grid(row=i*5+2, column=0)
        entry = tk.Entry(frame_formulario)
        entry.grid(row=i*5+2, column=1)
        entry_fecha_inicio.append(entry)
        
        tk.Label(frame_formulario, text="Fecha fin (DDMMYYYY):").grid(row=i*5+3, column=0)
        entry = tk.Entry(frame_formulario)
        entry.grid(row=i*5+3, column=1)
        entry_fecha_fin.append(entry)
        
        tk.Label(frame_formulario, text="Horas a pagar (máx 24h):").grid(row=i*5+4, column=0)
        entry = tk.Entry(frame_formulario)
        entry.grid(row=i*5+4, column=1)
        entry_horas_pagar.append(entry)
        
        tk.Label(frame_formulario, text="Unidad administrativa:").grid(row=i*5+5, column=0)
        entry = tk.Entry(frame_formulario)
        entry.grid(row=i*5+5, column=1)
        entry_unidad_administrativa.append(entry)
    
    tk.Button(frame_formulario, text="Generar Claves", command=generar_clave).grid(row=num_empleados*5+1, column=0, columnspan=2)

frame_formulario = tk.Frame(root)
frame_formulario.pack(pady=10)

resultado_text = tk.Text(root, height=10, width=60)
resultado_text.pack(pady=10)

root.mainloop()
