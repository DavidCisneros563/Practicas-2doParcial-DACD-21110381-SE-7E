# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:55:29 2024

@author: David
"""

import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# Conectar a la base de datos o crearla si no existe
conn = sqlite3.connect('futbol_game.db')
cursor = conn.cursor()

# Crear la tabla para almacenar las respuestas
cursor.execute('''CREATE TABLE IF NOT EXISTS respuestas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pregunta TEXT,
                    respuesta TEXT)''')

# Crear la tabla para los jugadores y sus características
cursor.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                    nombre TEXT PRIMARY KEY,
                    nacionalidad TEXT,
                    posicion TEXT,
                    club TEXT,
                    habilidades TEXT)''')

# Función para agregar jugadores iniciales en la base de datos si no existen
def agregar_jugadores_iniciales():
    jugadores_iniciales = {
        "Lionel Messi": {"nacionalidad": "Argentina", "posicion": "Delantero", "club": "Inter Miami", "habilidades": "Regate, Tiros libres"},
        "Cristiano Ronaldo": {"nacionalidad": "Portugal", "posicion": "Delantero", "club": "Al Nassr", "habilidades": "Velocidad, Tiros de cabeza"},
        "Neymar Jr.": {"nacionalidad": "Brasil", "posicion": "Delantero", "club": "Al Hilal", "habilidades": "Regate, Tiros precisos"},
        "Kylian Mbappé": {"nacionalidad": "Francia", "posicion": "Delantero", "club": "Paris Saint-Germain", "habilidades": "Velocidad, Dribbling"},
        "Kevin De Bruyne": {"nacionalidad": "Bélgica", "posicion": "Centrocampista", "club": "Manchester City", "habilidades": "Pases, Tiros lejanos"},
        "Virgil van Dijk": {"nacionalidad": "Países Bajos", "posicion": "Defensa", "club": "Liverpool", "habilidades": "Cabeza, Marcaje"},
    }

    for nombre, caracteristicas in jugadores_iniciales.items():
        cursor.execute('''INSERT OR IGNORE INTO jugadores (nombre, nacionalidad, posicion, club, habilidades)
                          VALUES (?, ?, ?, ?, ?)''',
                       (nombre, caracteristicas['nacionalidad'], caracteristicas['posicion'], caracteristicas['club'], caracteristicas['habilidades']))
    conn.commit()

# Función para hacer preguntas al usuario
def hacer_pregunta(pregunta):
    respuesta = messagebox.askyesno("Pregunta", pregunta)
    cursor.execute("INSERT INTO respuestas (pregunta, respuesta) VALUES (?, ?)", (pregunta, 'sí' if respuesta else 'no'))
    conn.commit()
    return respuesta

# Función para agregar un nuevo jugador a la base de datos
def agregar_jugador():
    nombre = simpledialog.askstring("Agregar Jugador", "¿Cuál era el jugador correcto?:")
    if cursor.execute("SELECT * FROM jugadores WHERE nombre = ?", (nombre,)).fetchone():
        messagebox.showinfo("Info", "Este jugador ya está registrado.")
        return

    nacionalidad = simpledialog.askstring("Agregar Jugador", f"¿Cuál es la nacionalidad de {nombre}?:")
    posicion = simpledialog.askstring("Agregar Jugador", f"¿Cuál es la posición de {nombre}?:")
    club = simpledialog.askstring("Agregar Jugador", f"¿Cuál es el club de {nombre}?:")
    habilidades = simpledialog.askstring("Agregar Jugador", f"¿Cuáles son las habilidades de {nombre}?:")
    
    cursor.execute('''INSERT INTO jugadores (nombre, nacionalidad, posicion, club, habilidades)
                      VALUES (?, ?, ?, ?, ?)''', (nombre, nacionalidad, posicion, club, habilidades))
    conn.commit()
    messagebox.showinfo("Info", f"{nombre} ha sido agregado a la base de datos.")

# Función para mostrar la imagen del jugador
def mostrar_imagen(jugador):
    try:
        image_path = f"{jugador.lower().replace(' ','_')}.png"  # Asegúrate de que los nombres de imagen coincidan
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        img_label.config(image=img_tk)
        img_label.image = img_tk  # Mantener una referencia a la imagen
    except Exception as e:
        messagebox.showerror("Error", "No se pudo cargar la imagen.")

# Función principal del juego
def encadenamiento_adelante():
    cursor.execute("SELECT * FROM jugadores")
    jugadores = cursor.fetchall()
    
    posibles = {j[0]: {"nacionalidad": j[1], "posicion": j[2], "club": j[3], "habilidades": j[4]} for j in jugadores}

    if hacer_pregunta("¿El jugador es argentino?"):
        posibles = {k: v for k, v in posibles.items() if v["nacionalidad"] == "Argentina"}
    elif hacer_pregunta("¿El jugador es portugués?"):
        posibles = {k: v for k, v in posibles.items() if v["nacionalidad"] == "Portugal"}

    if hacer_pregunta("¿Juega como delantero?"):
        posibles = {k: v for k, v in posibles.items() if v["posicion"] == "Delantero"}
    elif hacer_pregunta("¿Juega como defensa?"):
        posibles = {k: v for k, v in posibles.items() if v["posicion"] == "Defensa"}

    if len(posibles) > 1:
        messagebox.showinfo("Info", "Todavía quedan varios jugadores posibles.")
        for habilidades in set(v["habilidades"] for v in posibles.values()):
            if hacer_pregunta(f"¿El jugador tiene habilidades de {habilidades}?"):
                posibles = {k: v for k, v in posibles.items() if v["habilidades"] == habilidades}
                break
    
    if len(posibles) == 1:
        jugador_adivinado = list(posibles.keys())[0]
        mostrar_imagen(jugador_adivinado)  # Mostrar la imagen del jugador
        if hacer_pregunta(f"¿El jugador es {jugador_adivinado}?"):
            messagebox.showinfo("Info", "¡He adivinado correctamente!")
        else:
            messagebox.showinfo("Info", "Vaya, no lo adiviné.")
            agregar_jugador()
    elif len(posibles) > 1:
        messagebox.showinfo("Info", f"Aún hay varios jugadores: {', '.join(posibles.keys())}")
    else:
        messagebox.showinfo("Info", "No se pudo determinar el jugador.")
        agregar_jugador()

# Lógica del juego
def juego():
    agregar_jugadores_iniciales()  # Asegurar que los jugadores iniciales estén cargados en la base de datos
    encadenamiento_adelante()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Juego de Adivina Quién - Versión Futbolística")
root.geometry("400x500")
root.config(bg="#a3c1ad")

# Crear botón para iniciar el juego
start_button = tk.Button(root, text="Iniciar Juego", command=juego, bg="#ffdd57", font=("Arial", 14))
start_button.pack(pady=20)

# Label para mostrar la imagen
img_label = tk.Label(root, bg="#a3c1ad")
img_label.pack(pady=10)

root.mainloop()

# Cerrar la conexión a la base de datos al final
conn.close()
