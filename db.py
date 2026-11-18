import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("puntajes.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS puntajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            puntaje INTEGER
        )
    """)

    conexion.commit()
    conexion.close()


def guardar_puntaje(nombre, puntaje):
    conexion = sqlite3.connect("puntajes.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)",
        (nombre, puntaje)
    )

    conexion.commit()
    conexion.close()


def obtener_top5():
    conexion = sqlite3.connect("puntajes.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC LIMIT 5"
    )

    datos = cursor.fetchall()
    conexion.close()

    return datos