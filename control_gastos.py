import tkinter as tk

def ventana_control():
    v = tk.Toplevel()
    v.title("Control de Gastos")
    v.geometry("350x200")
    v.configure(bg="#f1f1f1")

    tk.Label(v, text="Control de Gastos", font=("Arial",14,"bold"), bg="#f1f1f1").pack(pady=10)
    tk.Label(v, text="Maneja tsu gastos personales", font=("Arial", 14, "bold")).pack(pady=10)

    #Campos
    tk.Label(v, text="Ingreso:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Label(v, text="Egreso:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Label(v, text="Fecha:", bg="#f1f1f1").pack()
    tk.Entry(v, width=30).pack(pady=5)

    tk.Button(v, text="Agregar",width=15 ,bg="#90ee90").pack(pady=15)
    tk.Button(v, text="Guardar", width=15, bg="#90ee90").pack(pady=10)
    tk.Button(v, text="Atrás", width=15, bg="#ff9999", command=v.destroy).pack(pady=5)