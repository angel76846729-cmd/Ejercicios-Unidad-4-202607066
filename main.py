import tkinter as tk
from tkinter import messagebox
import db

db.crear_tabla()

ventana = tk.Tk()
ventana.title("Guardar puntajes")
ventana.geometry("300x200")

tk.Label(ventana, text="Nombre:").pack(pady=5)
nombre = tk.Entry(ventana)
nombre.pack()

tk.Label(ventana, text="Puntaje:").pack(pady=5)
puntaje = tk.Entry(ventana)
puntaje.pack()

def guardar():
    try:
        n = nombre.get().strip()
        p = int(puntaje.get())

        if n == "":
            messagebox.showerror("Error", "Ingresa un nombre.")
            return

        db.guardar_puntaje(n, p)
        messagebox.showinfo("Éxito", "Puntaje guardado correctamente.")

        nombre.delete(0, tk.END)
        puntaje.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "El puntaje debe ser un número entero.")

tk.Button(ventana, text="Guardar", command=guardar).pack(pady=15)

ventana.mainloop()