
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mostrar texto")
ventana.geometry("300x200")

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=10)

def mostrar():
    etiqueta.config(text=entrada.get())

boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack(pady=10)

ventana.mainloop()
