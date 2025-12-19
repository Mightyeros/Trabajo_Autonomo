# -*- coding: utf-8 -*-
"""
NOMBRE DEL ARCHIVO: main.py

DESCRIPCIÓN:
Este es el archivo principal que ejecutas para jugar.
Se encarga de mostrar los menús, pedirte que elijas opciones y llevar el marcador.
Para saber quién gana, le pregunta a nuestro otro archivo: 'libreria_juego.py'.
"""

import random
import time

# --- IMPORTACIÓN DE NUESTRA LIBRERÍA ---
# Intentamos cargar nuestra librería. Usamos un bloque try/except por si acaso 
# el archivo 'libreria_juego.py' no está en la carpeta.
libreria_cargada = False
try:
    import libreria_juego
    libreria_cargada = True
except ImportError:
    print("\n[ERROR CRÍTICO]: No encuentro el archivo 'libreria_juego.py'.")
    print("Por favor, asegúrate de que ambos archivos estén juntos en la misma carpeta.")
    input("Presiona Enter para salir...")


def mostrar_reglas_pantalla():
    """Pide las reglas a la librería y las muestra en pantalla."""
    print("\n--- REGLAS DEL JUEGO ---")
    # Llamamos a la función usando el nombre completo de la librería
    reglas = libreria_juego.obtener_reglas_texto()
    for regla in reglas:
        print(regla)
    print("\nEl juego sigue hasta que elijas 'Volver' en el menú.")
    input("Presiona Enter para volver al menú principal...")


def jugar_sesion():
    """
    Maneja una partida completa. Muestra el marcador y repite rondas
    hasta que el usuario quiera salir.
    """
    print("\nIniciando sesión de juego...")
    time.sleep(0.5)
    
    marcador_usu = 0
    marcador_pc = 0
    jugando_ronda = True

    while jugando_ronda:
        print(f"\n>>> Marcador: Jugador [{marcador_usu}] - PC [{marcador_pc}] <<<")
        print("1. Piedra | 2. Papel | 3. Tijera | 4. Volver al Menú")

        try:
            # Pedimos la opción y aseguramos que sea un número entero
            opcion = int(input("Elige tu jugada (1-4): "))

            if opcion == 4:
                print("Regresando al menú principal...")
                jugando_ronda = False
                
            elif 1 <= opcion <= 3:
                print("\n¡Piedra, Papel o Tijera!")
                time.sleep(0.5)

                # La PC elige al azar con la libreria random
                opcion_pc = random.randint(1, 3)

                # --- USO DE LA LIBRERÍA PARA OBTENER NOMBRES ---
                nombre_usu = libreria_juego.obtener_nombre_jugada(opcion)
                nombre_pc = libreria_juego.obtener_nombre_jugada(opcion_pc)

                print(f"Tú elegiste: [{nombre_usu}]")
                print(f"La PC eligió: [{nombre_pc}]")
                print("-------------------------")
                time.sleep(0.5)

                # --- USO DE LA LIBRERÍA PARA DETERMINAR GANADOR ---
                # Aquí está la clave: le preguntamos a la librería quién ganó.
                # Le pasamos los dos números y esperamos el resultado.
                resultado = libreria_juego.determinar_ganador(opcion, opcion_pc)

                if resultado == "empate":
                    print("¡Es un EMPATE!")
                elif resultado == "usuario":
                    print("¡TÚ GANAS la ronda!")
                    marcador_usu += 1
                else:
                    print("¡La PC GANA la ronda!")
                    marcador_pc += 1
                
                print("-------------------------")
                time.sleep(0.8)

            else:
                # Si pone un número que no es 1, 2, 3 o 4
                print("\n[AVISO]: Por favor elige un número entre 1 y 4.")

        except ValueError:
            # Si el usuario escribe letras en lugar de números
            print("\n[ERROR]: Entrada inválida. Debes ingresar un número entero.")

    # Al terminar el while, mostramos el resultado final
    print(f"\nFin de la sesión. Resultado final: Jugador [{marcador_usu}] - PC [{marcador_pc}]")
    time.sleep(1)


def main():
    """Función principal: Muestra el menú de inicio."""
    
    # Si la librería no se cargó correctamente al principio, no hacemos nada.
    if not libreria_cargada:
        return

    app_corriendo = True

    while app_corriendo:
        print("\n=======================================")
        print("     PIEDRA, PAPEL O TIJERA v2.0       ")
        print("=======================================")
        print("1. Jugar Nueva Partida")
        print("2. Ver Reglas")
        print("3. Salir")
        print("=======================================")

        try:
            seleccion = int(input("Selecciona una opción (1-3): "))

            # Estructura if/elif para el menú principal
            if seleccion == 1:
                jugar_sesion()
            elif seleccion == 2:
                mostrar_reglas_pantalla()
            elif seleccion == 3:
                print("\nCerrando aplicación. ¡Gracias por jugar!")
                app_corriendo = False
            else:
                print("\n[AVISO]: Opción no válida. Elige 1, 2 o 3.")

        except ValueError:
            print("\n[ERROR]: Debes ingresar el NÚMERO de la opción.")

# Ejecuta main() si este es el archivo principal.
if __name__ == "__main__":
    main()

