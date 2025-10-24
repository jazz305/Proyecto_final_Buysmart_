import tkinter as tk

def ventana_resumen():
    v= tk.Toplevel()
    v.title("Control de Gastos")
    v.geometry("350x200")
    v.configure(bg="#f1f1f1")

    tk.Label(v, text="Control de gastos", font=("Arial",14,"bold"),bg="#f1f1f1").pack(pady=10)
    
    tk.Button(v, text="Cerrar",width=15, command=v.destroy).pack(pady=20)