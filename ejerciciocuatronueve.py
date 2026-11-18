import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Tabla de jugadores")
ventana.geometry("500x250")

tabla = ttk.Treeview(ventana, columns=("Posición", "Jugador", "Puntaje"), show="headings")

tabla.heading("Posición", text="Posición")
tabla.heading("Jugador", text="Jugador")
tabla.heading("Puntaje", text="Puntaje")

tabla.pack(fill="both", expand=True)

datos = [
    (1, "Carlos", 950),
    (2, "Ana", 870),
    (3, "Luis", 800),
    (4, "María", 750),
    (5, "Pedro", 680)
]

for dato in datos:
    tabla.insert("", "end", values=dato)

ventana.mainloop()