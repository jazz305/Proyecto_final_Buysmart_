import tkinter as tk

def ventana_lista():
    v = tk.Toplevel()
    v.title("Lista de Productos")
    v.geometry("350x300")
    v.configure(bg="#f1f1f1")

    tk.Label(v, text="Lista de Productos", font=("Arial",14, "bold"), bg="#f1f1f1").pack(pady=10)

    #Campos
    tk.Label(v, text="Nombre:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Label(v, text="Cantidad:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Label(v, text="Precio unitario:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Button(v, text="Agregar",width=15 ,bg="#90ee90").pack(pady=10)
    tk.Button(v, text="Atrás", width=15, bg="#ff9999", command=v.destroy).pack(pady=5)

