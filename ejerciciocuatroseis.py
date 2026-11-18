import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Formulario")

tk.Label(ventana, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad").grid(row=1, column=0, padx=5, pady=5)
edad = tk.Entry(ventana)
edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Correo").grid(row=2, column=0, padx=5, pady=5)
correo = tk.Entry(ventana)
correo.grid(row=2, column=1, padx=5, pady=5)


def guardar():
    messagebox.showinfo(
        "Datos ingresados",
        f"Nombre: {nombre.get()}\nEdad: {edad.get()}\nCorreo: {correo.get()}",
    )


tk.Button(ventana, text="Guardar", command=guardar).grid(
    row=3, column=1, padx=5, pady=5
)

ventana.mainloop()