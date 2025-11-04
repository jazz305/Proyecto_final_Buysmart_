import tkinter as tk
from tkinter import messagebox
import lista_productos
import control_gastos
import resumen

#Funciones de los botones para abrir las otras ventanas
def abrir_lista():
   lista_productos.ventana_lista()

def abrir_control():
   control_gastos.ventana_control()

def abrir_resumen():
   resumen.ventana_resumen()

def salir():
   ventana.destroy

#Ventana Principal/Inicio.
ventana= tk.Tk()
ventana.title("BuySmart-tu Gestor de Supermercado y controlador de gastos personales.")
ventana.geometry("350x400")
ventana.resizable(False,False)
ventana.configure(bg="#f1f1f1")

#Titulo de la App
titulo= tk.Label(ventana, text="BuySmart", font=("Arial",18,"bold"), bg="#f1f1f1")
titulo.pack(pady=(30,10))

#Texto breve sobre la app
descripcion= tk.Label(
    ventana,
    text="Tu Asistente para gestionar listas de compras y controlar tus gastos personales.",
    font=("Arial", 10),
    wraplength=280,
    bg="#f1f1f1",
    justify="center"
)
descripcion.pack(pady=(0,20))

#Botones principales
tk.Button(ventana, text="Lista de Productos", width=25, height=2, command=abrir_lista).pack(pady=5)
tk.Button(ventana, text="Control de Gastos", width=25, height=2, command=abrir_control).pack(pady=5)
tk.Button(ventana, text="Ver Resumen", width=25, height=2, command=abrir_resumen).pack(pady=5)
tk.Button(ventana, text="Salir", width=25, height=2,bg="#ff5c5c",fg="white" ,command=ventana.destroy).pack(pady=20)

ventana.mainloop()