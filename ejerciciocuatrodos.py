import tkinter as ventana


formulario = ventana.Tk()
formulario.title("Formularios")
formulario.geometry("550x300")
formulario.configure(bg="lightblue")
etiqueta=ventana.Label(formulario, text="Haz clic en el boton", width=10, justify="center")
formulario.mainloop()