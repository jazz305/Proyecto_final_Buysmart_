import tkinter as tk
from tkinter import messagebox
from datetime import date
import os

#Funcion Guardar movimiento
def guardar_movimiento(fecha_var, ingreso_var, egreso_var, ingreso_entry):
    fecha = fecha_var.get()
    ingreso = ingreso_var.get()
    egreso = egreso_var.get()

    if not ingreso and not egreso:
        messagebox.showwarning("Debe ingresar un valor para Ingreso o Egreso.")
        return
       
    try:
        if ingreso:
            float(ingreso)
        if egreso:
            float(egreso)
    except ValueError:
        messagebox.showerror("Error", "Ingreso y Egreso deben ser números válidos.")
        return
    
    try:
        linea = f"Fecha: {fecha} | Ingreso: {ingreso if ingreso else '0'} | Egreso: {egreso if egreso else '0'}\n"

        ruta_archivo = os.path.join(os.path.dirname(__file__), "control_gastos.txt")

        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(linea)

        messagebox.showinfo("Bien!", "Movimiento guardado correctamente en control_gastos.txt")

        # cursor vuelve a la primera casilla (Ingreso)
        ingreso_var.set("")
        egreso_var.set("")
        ingreso_entry.focus_set()
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al guardar: {e}")

#Funcion limpiar campos
def limpiar_campos(fecha_var, ingreso_var, egreso_var, ingreso_entry):
    fecha_actual = date.today().strftime("%d/%m/%Y")
    fecha_var.set(fecha_actual)
    ingreso_var.set("")
    egreso_var.set("")

    # cursor a la primera casilla (Ingreso)
    ingreso_entry.focus_set()
    
#Interfaz de la ventana
def ventana_control():
    v = tk.Toplevel()
    v.title("Control de Gastos")
    v.geometry("350x250")
    v.resizable(False, False)
    v.configure(bg="#f1f1f1")

    fecha_var = tk.StringVar(value=date.today().strftime("%d/%m/%Y"))
    ingreso_var = tk.StringVar()
    egreso_var = tk.StringVar()
    
    form_frame = tk.Frame(v, bg="#f1f1f1")
    form_frame.pack(pady=20) 
    
    row_idx = 0
    tk.Label(form_frame, text="Fecha:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(form_frame, textvariable=fecha_var, width=20, state="readonly")\
        .grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(form_frame, text="Ingreso:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    ingreso_entry = tk.Entry(form_frame, textvariable=ingreso_var, width=20)
    ingreso_entry.grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(form_frame, text="Egreso:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(form_frame, textvariable=egreso_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    button_frame = tk.Frame(v, bg="#f1f1f1")
    button_frame.pack(pady=20) 
    
    tk.Button(
        button_frame, text="Nuevo", width=10,
        command=lambda: limpiar_campos(fecha_var, ingreso_var, egreso_var, ingreso_entry)
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame, text="Guardar", width=10,
        command=lambda: guardar_movimiento(fecha_var, ingreso_var, egreso_var, ingreso_entry)
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(button_frame, text="Salir", width=10, command=v.destroy).pack(side=tk.LEFT, padx=5)

    # foco inicial
    ingreso_entry.focus_set()
