def jugar_clue_spiderman():
    while True:  # Bucle para permitir múltiples partidas
        print("¡Bienvenido al juego Clue: Spider-Man!")
        
        culpables = ["Green Goblin", "Doctor Octopus", "Black Cat", "Spider-Man", "Mary Jane Watson"]
        armas = ["Bomba de gas", "Tentáculos mecánicos", "Telarañas", "Bastón", "Cuchillo de cocina"]
        locaciones = ["El Edificio Daily Bugle", "La Torre Oscorp", "El Apartamento de Peter", "El Puente de Queensboro", "La Calle de Nueva York"]

        # Seleccionar culpable
        print("\nPersonajes disponibles:")
        for i, culpable in enumerate(culpables, 1):
            print(f"{i}. {culpable}")
        
        eleccion_culpable = int(input("\nSelecciona el culpable (número): ")) - 1

        # Seleccionar arma
        print("\nArmas disponibles:")
        for i, arma in enumerate(armas, 1):
            print(f"{i}. {arma}")

        eleccion_arma = int(input("\nSelecciona el arma (número): ")) - 1

        # Seleccionar locación
        print("\nLocaciones disponibles:")
        for i, locacion in enumerate(locaciones, 1):
            print(f"{i}. {locacion}")

        eleccion_locacion = int(input("\nSelecciona la locación (número): ")) - 1

        # Crear la historia final
        historia_final = ""

        if eleccion_culpable == 0:
            historia_final += ("En una noche oscura, el Green Goblin, decidido a eliminar cualquier prueba en su contra, ")
        elif eleccion_culpable == 1:
            historia_final += ("Durante un audaz robo, el Doctor Octopus utilizó su ingenio y sus tentáculos mecánicos para ")
        elif eleccion_culpable == 2:
            historia_final += ("Black Cat, siempre en busca de un tesoro, irrumpió en el lugar y encontró la oportunidad de ")
        elif eleccion_culpable == 3:
            historia_final += ("Spider-Man, en medio de una confrontación, se vio obligado a usar sus habilidades para ")
        elif eleccion_culpable == 4:
            historia_final += ("Mary Jane, defendiendo a un amigo, tomó una decisión audaz y utilizó un arma inesperada para ")

        if eleccion_arma == 0:
            historia_final += "lanzar una bomba de gas, creando un caos repentino."
        elif eleccion_arma == 1:
            historia_final += "atacar con sus tentáculos mecánicos, dejando a todos a su paso atónitos."
        elif eleccion_arma == 2:
            historia_final += "atrapar a su oponente con telarañas, intentando desactivar la situación."
        elif eleccion_arma == 3:
            historia_final += "usar un bastón, sorprendiendo a los presentes con su agilidad."
        elif eleccion_arma == 4:
            historia_final += "defenderse con un cuchillo de cocina, convirtiéndose en una heroína inesperada."

        if eleccion_locacion == 0:
            historia_final += " El escenario de esta intensa acción fue el Edificio Daily Bugle, donde el peligro acechaba."
        elif eleccion_locacion == 1:
            historia_final += " La Torre Oscorp se convirtió en el campo de batalla, donde la tecnología y el crimen colisionaron."
        elif eleccion_locacion == 2:
            historia_final += " En el apartamento de Peter, se desató un conflicto que reveló secretos ocultos."
        elif eleccion_locacion == 3:
            historia_final += " El Puente de Queensboro fue testigo de una confrontación que pondría a prueba la valentía de todos."
        elif eleccion_locacion == 4:
            historia_final += " En una oscura calle de Nueva York, la noche se tornó peligrosa y llena de suspenso."

        # Mostrar la historia final
        print("\nTu historia final es:")
        print(historia_final)

        # Preguntar al usuario si quiere jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar otra partida? (sí/no): ").lower()
        if jugar_de_nuevo != 'sí':
            print("¡Gracias por jugar! Hasta luego.")
            break  # Salir del bucle si el usuario no quiere jugar de nuevo

# Ejecutar el juego
jugar_clue_spiderman()