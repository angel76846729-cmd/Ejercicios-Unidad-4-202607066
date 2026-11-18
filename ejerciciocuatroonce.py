import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json

ventana = tk.Tk()
ventana.title("Cargar preguntas")
ventana.geometry("600x300")

tabla = ttk.Treeview(
    ventana,
    columns=("Texto", "Dificultad", "Tipo"),
    show="headings"
)

tabla.heading("Texto", text="Texto")
tabla.heading("Dificultad", text="Dificultad")
tabla.heading("Tipo", text="Tipo")

tabla.column("Texto", width=350)
tabla.column("Dificultad", width=100)
tabla.column("Tipo", width=100)

tabla.pack(fill="both", expand=True, padx=10, pady=10)


def cargar():
    archivo = filedialog.askopenfilename(
        filetypes=[("Archivos JSON", "*.json")]
    )

    if not archivo:
        return

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            preguntas = json.load(f)

        if not isinstance(preguntas, list):
            raise ValueError("El archivo debe contener una lista.")

        for p in preguntas:
            if not isinstance(p, dict):
                raise ValueError("Una pregunta tiene formato incorrecto.")

            if not all(k in p for k in ("texto", "dificultad", "tipo", "correcta")):
                raise ValueError("Faltan campos obligatorios.")

            if p["tipo"] not in ("multiple", "vf"):
                raise ValueError("El tipo de pregunta no es válido.")

            if not isinstance(p["texto"], str) or not p["texto"].strip():
                raise ValueError("El texto de una pregunta no es válido.")

            if type(p["dificultad"]) is not int or p["dificultad"] not in (1, 2, 3):
                raise ValueError("La dificultad debe ser 1, 2 o 3.")

            if p["tipo"] == "multiple":
                if not isinstance(p.get("opciones"), list) or len(p["opciones"]) != 4:
                    raise ValueError("La pregunta múltiple debe tener 4 opciones.")

                if type(p["correcta"]) is not int or p["correcta"] not in range(4):
                    raise ValueError("La respuesta correcta debe ser un índice de 0 a 3.")

            elif p["tipo"] == "vf":
                if type(p["correcta"]) is not bool:
                    raise ValueError("La respuesta correcta debe ser True o False.")

        for fila in tabla.get_children():
            tabla.delete(fila)

        for p in preguntas:
            tabla.insert("", "end", values=(
                p["texto"],
                p["dificultad"],
                p["tipo"]
            ))

        messagebox.showinfo("Éxito", "Preguntas cargadas correctamente.")

    except (json.JSONDecodeError, ValueError, KeyError, TypeError) as e:
        messagebox.showerror("Error", f"Formato incorrecto: {e}")

    except OSError:
        messagebox.showerror("Error", "No se pudo abrir el archivo.")


tk.Button(
    ventana,
    text="Cargar Preguntas",
    command=cargar
).pack(pady=5)

ventana.mainloop()
