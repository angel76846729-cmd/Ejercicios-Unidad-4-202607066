import tkinter as tk

ventana = tk.Tk()
ventana.title("Suma de números")
ventana.geometry("300x200")

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 + num2}")
    except ValueError:
        resultado.config(text="Ingresa números válidos")

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack(pady=5)

ventana.mainloop()
