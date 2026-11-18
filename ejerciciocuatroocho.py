import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Formulario")
ventana.geometry("300x180")

tk.Label(ventana, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad").grid(row=1, column=0, padx=5, pady=5)
edad = tk.Entry(ventana)
edad.grid(row=1, column=1)

tk.Label(ventana, text="Correo").grid(row=2, column=0, padx=5, pady=5)
correo = tk.Entry(ventana)
correo.grid(row=2, column=1)

def guardar():
    if nombre.get().strip() == "":
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return

    try:
        num_edad = int(edad.get())

        if num_edad < 1 or num_edad > 120:
            messagebox.showerror("Error", "La edad debe estar entre 1 y 120.")
            return

    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número entero.")
        return

    if "@" not in correo.get():
        messagebox.showerror("Error", "El correo debe contener '@'.")
        return

    messagebox.showinfo("Éxito", "Todos los datos son válidos.")

tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, column=1, pady=10)

ventana.mainloop()