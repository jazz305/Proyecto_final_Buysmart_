import tkinter as tk
from tkinter import messagebox
from datetime import date

# Creamos una funcion para agregar el producto actual al Listbox y limpiar campos
def agregar_a_lista(nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label):
    try:
        nombre = nombre_var.get()
        cantidad = int(cantidad_var.get())
        precio = float(precio_var.get())
        
        if not nombre or cantidad <= 0 or precio <= 0:
            raise ValueError("Dato invalido")
            
        # Calculamos el subtotal del item a ingresar
        subtotal = cantidad * precio
        # Formato del item a mostrar en el Listbox: "Nombre | Cantidad x Precio = Subtotal
        item_para_lista = f"{nombre:<15} | {cantidad} x {precio:.2f} = {subtotal:.2f}"
        
        lista_productos_box.insert(tk.END, item_para_lista)
        
        # Limpiamos los campos de entrada para poder ingresar el siguiente producto
        nombre_var.set("")
        cantidad_var.set("")
        precio_var.set("")
        # Recalculamos el total general 
        calcular_total_lista(lista_productos_box, total_general_label)

    except ValueError:
        messagebox.showerror("Error en la entrada", "Asegurese de que Nombre, Cantidad (>0) y Precio (>0) sean validos.")

# Creamos una funcion para calcular el total de TODOS los productos en el Listbox
def calcular_total_lista(lista_productos_box, total_general_label):
    total_general = 0.0
    
    # Iteraramos sobre todos los elementos del Listbox
    for i in range(lista_productos_box.size()):
        item = lista_productos_box.get(i)
        
        # El subtotal es el valor despues del signo "="
        try:
            # Buscar el subtotal (el ultimo valor despues del "=")
            partes = item.split("=")
            subtotal = float(partes[-1].strip())
            total_general += subtotal
        except (ValueError, IndexError):
            # Ignoramos items que no tienen el formato esperado
            continue
    
    total_general_label.config(text=f"Total de la Lista: gs {total_general:.2f}")
    return total_general

# Creamos una funcion para guardar la lista completa en un archivo .txt
def guardar_lista(fecha_var, lista_productos_box, total_general_label):
    fecha = fecha_var.get()
    total_final = total_general_label.cget("text").split("gs. ")[-1]
    
    if lista_productos_box.size() == 0:
        messagebox.showwarning("No hay productos para guardar en la lista")
        return

    try:
        with open("lista_de_compras.txt", "a") as archivo:
            archivo.write("="*40 + "\n")
            archivo.write(f"Lista de Compras - Fecha: {fecha}\n")
            archivo.write("-" * 40 + "\n")
            
            # Guardamos cada item del Listbox
            for i in range(lista_productos_box.size()):
                archivo.write(lista_productos_box.get(i) + "\n")
                
            archivo.write("-" * 40 + "\n")
            archivo.write(f"TOTAL FINAL DE LA LISTA: gs. {total_final}\n")
            archivo.write("="*40 + "\n\n")

        messagebox.showinfo("Bien!", f"Lista de {lista_productos_box.size()} productos guardada en lista_de_compras.txt")
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrio un error al guardar: {e}")

# Creamos una funcion para iniciar una lista nueva (y limpiar todo)
def nueva_lista(fecha_var, nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label):
    fecha_actual = date.today().strftime("%d/%m/%Y")
    fecha_var.set(fecha_actual)
    nombre_var.set("")
    cantidad_var.set("")
    precio_var.set("")
    lista_productos_box.delete(0, tk.END) # Limpia el Listbox
    total_general_label.config(text="Total de la Lista: gs 0.00")


def ventana_lista():
    v = tk.Toplevel()
    v.title("Lista de Productos")
    v.geometry("500x350")
    v.configure(bg="#f1f1f1")

# Variables de control
    fecha_var = tk.StringVar(value=date.today().strftime("%d/%m/%Y"))
    nombre_var = tk.StringVar()
    cantidad_var = tk.StringVar()
    precio_var = tk.StringVar()
    
    # --- Estructura principal ---
    
    # Frame para los campos de entrada (izquierda)
    input_frame = tk.Frame(v, bg="#f1f1f1")
    input_frame.place(x=10, y=10) 

    # Frame para el Listbox y el Total (derecha)
    display_frame = tk.Frame(v, bg="#f1f1f1")
    display_frame.place(x=260, y=10) 
    
    # Frame para los botones de accion (abajo)
    button_frame = tk.Frame(v, bg="#f1f1f1")
    button_frame.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    
    # --- Widgets en el Frame de Entrada (grid) ---
    
    # Etiquetas y Campos de entrada
    row_idx = 0
    tk.Label(input_frame, text="Fecha:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=fecha_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Nombre del Producto:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=nombre_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Cantidad:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=cantidad_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    row_idx += 1
    tk.Label(input_frame, text="Precio:", bg="#f1f1f1").grid(row=row_idx, column=0, sticky="w", pady=5, padx=5)
    tk.Entry(input_frame, textvariable=precio_var, width=20).grid(row=row_idx, column=1, pady=5, padx=5)
    
    # Boton para AGREGAR el producto actual a la lista
    row_idx += 1
    tk.Button(input_frame, text="Agregar a Lista", 
              command=lambda: agregar_a_lista(nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label),
              width=15).grid(row=row_idx, column=0, columnspan=2, pady=10)
    
    # --- Widgets en el Frame de Visualizacion (Listbox y Total) ---
    
    # Listbox para los productos
    lista_productos_box = tk.Listbox(display_frame, width=35, height=10, bd=2, relief=tk.SOLID)
    lista_productos_box.pack(pady=5, padx=5)
    
    # Label para el Total General de la lista (simula la caja de total del boceto)
    total_general_label = tk.Label(display_frame, text="Total de la Lista: gs 0.00", bg="white", 
                                   relief=tk.SUNKEN, anchor="w", width=35, font=("Arial", 10, "bold"))
    total_general_label.pack(pady=5, padx=5)
    
    # --- Widgets en el Frame de Botones de Accion (pack) ---
    
    # Boton Calcular Total (Recalcula el total de la lista)
    tk.Button(button_frame, text="Calcular Total", width=12, 
              command=lambda: calcular_total_lista(lista_productos_box, total_general_label)).pack(side=tk.LEFT, padx=5)
    
    # Boton Nuevo (Limpia todos los campos e inicia una lista nueva)
    tk.Button(button_frame, text="Nuevo", width=12, 
              command=lambda: nueva_lista(fecha_var, nombre_var, cantidad_var, precio_var, lista_productos_box, total_general_label)).pack(side=tk.LEFT, padx=5)
    
    # Boton Guardar
    tk.Button(button_frame, text="Guardar", width=12, 
              command=lambda: guardar_lista(fecha_var, lista_productos_box, total_general_label)).pack(side=tk.LEFT, padx=5)
    
    # Boton Salir
    tk.Button(button_frame, text="Salir", width=12, command=v.destroy).pack(side=tk.LEFT, padx=5)