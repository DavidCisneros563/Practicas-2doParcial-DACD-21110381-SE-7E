# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:37:10 2024

@author: David
"""

import tkinter as tk
from tkinter import messagebox

def jugar_clue_spiderman():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("¡Clue: Spider-Man!")
    root.geometry("800x600")
    root.config(bg="#ff0000")  # Fondo rojo
    root.resizable(False, False)

    # Título en la parte superior
    titulo = tk.Label(root, text="¡Bienvenido a Clue: Spider-Man!", font=("Arial", 24, "bold"), bg="#ff0000", fg="#ffffff")
    titulo.pack(pady=20)

    def iniciar_juego():
        # Crear nueva ventana para la selección
        seleccion_window = tk.Toplevel(root)
        seleccion_window.title("Selecciona tus Opciones")
        seleccion_window.geometry("800x800")
        seleccion_window.config(bg="#0033cc")  # Fondo azul

        # Culpables, armas y locaciones
        culpables = ["Green Goblin", "Doctor Octopus", "Black Cat", "Spider-Man", "Mary Jane Watson"]
        armas = ["Bomba de gas", "Tentáculos mecánicos", "Telarañas", "Bastón", "Cuchillo de cocina"]
        locaciones = ["El Edificio Daily Bugle", "La Torre Oscorp", "El Apartamento de Peter", "El Puente de Queensboro", "La Calle de Nueva York"]

        # Variables para las selecciones
        culpable_seleccionado = tk.StringVar()
        arma_seleccionada = tk.StringVar()
        locacion_seleccionada = tk.StringVar()

        def jugar():
            # Verificar si todas las selecciones están hechas
            if not culpable_seleccionado.get() or not arma_seleccionada.get() or not locacion_seleccionada.get():
                messagebox.showwarning("Advertencia", "¡Debes seleccionar un culpable, un arma y una locación!")
                return  # No continuar si no se ha hecho una selección

            mostrar_historia(culpable_seleccionado.get(), arma_seleccionada.get(), locacion_seleccionada.get())
            seleccion_window.destroy()  # Cerrar la ventana de selección

        # Culpables
        tk.Label(seleccion_window, text="Selecciona el culpable:", bg="#0033cc", fg="#ffffff").pack(pady=10)
        culpable_listbox = tk.Listbox(seleccion_window, bg="#ffffff", fg="#000000")
        for culpable in culpables:
            culpable_listbox.insert(tk.END, culpable)
        culpable_listbox.pack(pady=10)
        culpable_listbox.bind('<<ListboxSelect>>', lambda e: culpable_seleccionado.set(culpable_listbox.get(culpable_listbox.curselection())))

        # Armas
        tk.Label(seleccion_window, text="Selecciona el arma:", bg="#0033cc", fg="#ffffff").pack(pady=10)
        arma_listbox = tk.Listbox(seleccion_window, bg="#ffffff", fg="#000000")
        for arma in armas:
            arma_listbox.insert(tk.END, arma)
        arma_listbox.pack(pady=10)
        arma_listbox.bind('<<ListboxSelect>>', lambda e: arma_seleccionada.set(arma_listbox.get(arma_listbox.curselection())))

        # Locaciones
        tk.Label(seleccion_window, text="Selecciona la locación:", bg="#0033cc", fg="#ffffff").pack(pady=10)
        locacion_listbox = tk.Listbox(seleccion_window, bg="#ffffff", fg="#000000")
        for locacion in locaciones:
            locacion_listbox.insert(tk.END, locacion)
        locacion_listbox.pack(pady=10)
        locacion_listbox.bind('<<ListboxSelect>>', lambda e: locacion_seleccionada.set(locacion_listbox.get(locacion_listbox.curselection())))

        # Botón para jugar
        boton_jugar = tk.Button(seleccion_window, text="Jugar", command=jugar, font=("Arial", 12), bg="#00cc00", fg="#ffffff")
        boton_jugar.pack(pady=20)

    # Función para salir del juego
    def salir_del_juego():
        if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
            root.destroy()  # Cerrar la ventana principal

    # Botón para salir
    boton_salir = tk.Button(root, text="Salir", command=salir_del_juego, font=("Arial", 12), bg="#ff0000", fg="#ffffff")
    boton_salir.pack(pady=10)

    # Botón para iniciar el juego
    boton_iniciar = tk.Button(root, text="Iniciar Juego", command=iniciar_juego, font=("Arial", 16), bg="#0033cc", fg="#ffffff")
    boton_iniciar.pack(pady=50)

    # Iniciar el bucle principal
    root.mainloop()

def mostrar_historia(culpable, arma, locacion):
    verdadero_culpable = "Green Goblin"
    historia_final = ""

    if culpable == verdadero_culpable:
        historia_final += f"El culpable de este crimen es {culpable}. "
        historia_final += f"En una noche oscura, el {culpable} lanzó una {arma} en {locacion}."
    else:
        historia_final += f"{culpable} no es el culpable. "
        if culpable == "Doctor Octopus":
            historia_final += f"Él estaba usando sus tentáculos mecánicos para ayudar a un amigo en {locacion} cuando se encontró con una {arma}."
        elif culpable == "Black Cat":
            historia_final += f"Estaba en {locacion} buscando un tesoro perdido y llevaba una {arma} como herramienta."
        elif culpable == "Spider-Man":
            historia_final += f"Él venía patrullando {locacion} con una {arma}, que pensó que podría ser útil en una emergencia."
        elif culpable == "Mary Jane Watson":
            historia_final += f"Venía con un {arma} que compró en una tienda en {locacion} para ayudar a un amigo."

    messagebox.showinfo("Tu historia final", historia_final)
    jugar_de_nuevo()

def jugar_de_nuevo():
    respuesta = messagebox.askyesno("¿Jugar de nuevo?", "¿Quieres jugar otra partida?")
    if respuesta:
        jugar_clue_spiderman()
    else:
        exit()

# Ejecutar el juego
jugar_clue_spiderman()
