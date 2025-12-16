import tkinter as tk
from tkinter import messagebox
from datetime import date
import os

# Creamos una funcion para agregar el producto actual al Listbox y limpiar campos
def agregar_a_lista(nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label, nombre_entry):
    try:
        nombre = nombre_var.get()
        cantidad = int(cantidad_var.get())
        precio = float(precio_var.get())
        
        if not nombre or cantidad <= 0 or precio <= 0:
            raise ValueError("Dato invalido")
            
        subtotal = cantidad * precio
        item_para_lista = f"{nombre:<15} | {cantidad} x {precio:.2f} = {subtotal:.2f}"
        
        lista_productos_box.insert(tk.END, item_para_lista)
        
        nombre_var.set("")
        cantidad_var.set("")
        precio_var.set("")
        calcular_total_lista(lista_productos_box, total_general_label)

        #Cursor vuelve a la primera casilla
        nombre_entry.focus_set()

    except ValueError:
        messagebox.showerror("Error", "Asegurese de que los datos ingresados sean validos.")

#Creamos una funcion para calcular el total de la lista
def calcular_total_lista(lista_productos_box, total_general_label):
    total_general = 0.0
    
    for i in range(lista_productos_box.size()):
        item = lista_productos_box.get(i)
        try:
            partes = item.split("=")
            subtotal = float(partes[-1].strip())
            total_general += subtotal
        except (ValueError, IndexError):
            continue
    
    total_general_label.config(text=f"Total de la Lista: gs {total_general:.2f}")
    return total_general
#Creamos la funcion para guardar la lista
def guardar_lista(fecha_var, lista_productos_box, total_general_label):
    fecha = fecha_var.get()
    total_final = total_general_label.cget("text").split("gs ")[-1]
    
    if lista_productos_box.size() == 0:
        messagebox.showwarning("No hay productos para guardar en la lista")
        return

    try:
        ruta_archivo = os.path.join(os.path.dirname(__file__), "lista_de_compras.txt")

        with open(ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write("="*40 + "\n")
            archivo.write(f"Lista de Compras - Fecha: {fecha}\n")
            archivo.write("-" * 40 + "\n")
            
            for i in range(lista_productos_box.size()):
                archivo.write(lista_productos_box.get(i) + "\n")
                
            archivo.write("-" * 40 + "\n")
            archivo.write(f"TOTAL FINAL DE LA LISTA: gs {total_final}\n")
            archivo.write("="*40 + "\n\n")

        messagebox.showinfo("Bien!", f"Lista de {lista_productos_box.size()} productos guardada en lista_de_compras.txt")
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error al guardar: {e}")

# Funcion NUEVA lista
def nueva_lista(fecha_var, nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label, nombre_entry):
    fecha_actual = date.today().strftime("%d/%m/%Y")
    fecha_var.set(fecha_actual)
    nombre_var.set("")
    cantidad_var.set("")
    precio_var.set("")
    lista_productos_box.delete(0, tk.END)
    total_general_label.config(text="Total de la Lista: gs 0.00")

    # Cursor a la primera casilla
    nombre_entry.focus_set()

#Interfaz de la ventana
def ventana_lista():
    v = tk.Toplevel()
    v.title("Lista de Productos")
    v.geometry("500x350")
    v.configure(bg="#f1f1f1")

    fecha_var = tk.StringVar(value=date.today().strftime("%d/%m/%Y"))
    nombre_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    precio_var = tk.StringVar()
    
    input_frame = tk.Frame(v, bg="#f1f1f1")
    input_frame.place(x=10, y=10) 

    display_frame = tk.Frame(v, bg="#f1f1f1")
    display_frame.place(x=260, y=10) 
    
    button_frame = tk.Frame(v, bg="#f1f1f1")
    button_frame.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    
    row_idx = 0
    tk.Label(input_frame, text="Fecha:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=fecha_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Nombre del Producto:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    nombre_entry = tk.Entry(input_frame, textvariable=nombre_var, width=20)
    nombre_entry.grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Cantidad:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=cantidad_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Precio:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=precio_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Button(
        input_frame,
        text="Agregar a Lista",
        width=15,
        command=lambda: agregar_a_lista(
            nombre_var, cantidad_var, precio_var,
            lista_productos_box, total_general_label,
            nombre_entry
        )
    ).grid(row=row_idx, column=0, columnspan=2, pady=10)
    
    lista_productos_box = tk.Listbox(display_frame, width=35, height=10, bd=2, relief=tk.SOLID)
    lista_productos_box.pack(pady=5, padx=5)
    
    total_general_label = tk.Label(
        display_frame,
        text="Total de la Lista: gs 0.00",
        bg="white",
        relief=tk.SUNKEN,
        anchor="w",
        width=35,
        font=("Arial", 10, "bold")
    )
    total_general_label.pack(pady=5, padx=5)

    tk.Button(
        button_frame,
        text="Calcular Total",
        width=12,
        command=lambda: calcular_total_lista(lista_productos_box, total_general_label)
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame,
        text="Nuevo",
        width=12,
        command=lambda: nueva_lista(
            fecha_var, nombre_var, cantidad_var, precio_var,
            lista_productos_box, total_general_label,
            nombre_entry
        )
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame,
        text="Guardar",
        width=12,
        command=lambda: guardar_lista(fecha_var, lista_productos_box, total_general_label)
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(button_frame, text="Salir", width=12, command=v.destroy).pack(side=tk.LEFT, padx=5)

    #foco inicial
    nombre_entry.focus_set()
