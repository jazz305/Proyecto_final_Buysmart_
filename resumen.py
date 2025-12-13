import tkinter as tk
import os

def ventana_resumen():
    v = tk.Toplevel()
    v.title("Resumen del Mes")
    v.geometry("450x400")
    v.configure(bg="#f1f1f1")

    tk.Label(v, text="Resumen de archivos guardados", font=("Arial",14,"bold"),
             bg="#f1f1f1").pack(pady=10)

    # Área de texto con scroll
    frame_texto = tk.Frame(v)
    frame_texto.pack(fill="both", expand=True, pady=5)

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")

    texto = tk.Text(frame_texto, wrap="word", yscrollcommand=scrollbar.set)
    texto.pack(fill="both", expand=True)

    scrollbar.config(command=texto.yview)

    # Carpeta actual del proyecto
    carpeta_actual = os.getcwd()

    # Buscar todos los archivos .txt existentes
    archivos = [f for f in os.listdir(carpeta_actual) if f.endswith(".txt")]

    if archivos:
        for archivo in archivos:
            ruta = os.path.join(carpeta_actual, archivo)
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read()
                texto.insert("end", f"--- {archivo} ---\n")
                texto.insert("end", contenido + "\n\n")
            except:
                texto.insert("end", f"No se pudo leer {archivo}\n\n")
    else:
        texto.insert("end", "No hay archivos .txt guardados en la carpeta del proyecto.")

    tk.Button(v, text="Cerrar", width=15, command=v.destroy).pack(pady=10)


