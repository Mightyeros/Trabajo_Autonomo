# -*- coding: utf-8 -*-
"""
Created on [Diciembre 2025]
@author: [Ismael Vasquez]

Descripción:
Esqueleto estructurado para el juego Piedra, Papel o Tijera (FASE 1).
Incluye menú principal, bucles de juego y manejo de errores.
"""

import random # Esta libreria permitira que la elecciones de la PC sean totalmente aleatorias
import time # Esta libreria nos permitirá agregar una pausa dramática

def mostrar_reglas():
    """
    Función para mostrar las reglas del juego.
    """
    print("\n--- REGLAS DEL JUEGO ---")
    print("1. Piedra aplasta Tijera.")
    print("2. Tijera corta Papel.")
    print("3. Papel envuelve Piedra.")
    print("El juego continúa ronda tras ronda hasta que elijas 'Volver' en el menú del juego.")
    print("¡Intenta acumular más puntos que la computadora!")
    
    # Pausa el programa hasta que el usuario presiona Enter
    input("\nPresiona Enter para volver al menú principal...")

def jugar_partida():
    """
    Contiene la lógica principal del bucle del juego y los marcadores.
    """
    print("\n¡Iniciando el juego...")
    time.sleep(1) # Pausa dramática de 1 segundo
    
    # --- VARIABLES (Marcadores) ---
    # Se reinician a 0 cada vez que empieza una nueva partida
    marcador_jugador = 0
    marcador_pc = 0
    
    # Variable para controlar el bucle interno
    jugando_ronda = True
    
    # --- BUCLE DEL JUEGO INTERNO ---
    while jugando_ronda:
        print("\n-----------------------------------")
        print(f"Marcador Actual: Jugador [{marcador_jugador}] - PC [{marcador_pc}]")
        print("1. Piedra | 2. Papel | 3. Tijera | 4. Volver al Menú Principal")
        
        try:
            # Atrapamos lo que escribe el usuario
            opcion_juego = int(input("Elige tu jugada (1-4): "))
            
            if opcion_juego == 4:
                # La puerta de salida del bucle interno
                print("Regresando al menú principal...")
                jugando_ronda = False # Apaga el interruptor, el bucle while terminará
                
            elif 1 <= opcion_juego <= 3:
                # --- FASE 2 COMPLETA: LÓGICA Y PUNTUACIÓN ---
                print("\n--- ¡Piedra, Papel o Tijera! ---")
                time.sleep(0.5) # Pequeña pausa de suspenso

                # 1. ELECCIÓN DE LA PC Y MOSTRAR TEXTOS
                opcion_pc = random.randint(1, 3)
                nombres_opciones = ["", "Piedra", "Papel", "Tijera"]
                
                print(f"Tú elegiste: [{nombres_opciones[opcion_juego]}]")
                print(f"La PC eligió: [{nombres_opciones[opcion_pc]}]")
                print("--------------------------------")
                time.sleep(0.5)

                # 2. EL ÁRBITRO Y 3. ACTUALIZACION MARCADORES
                
                # CASO A: EMPATE
                if opcion_juego == opcion_pc:
                    print("Resultado: ¡Es un EMPATE!")
                
                # CASO B: TÚ GANAS (Las 3 combinaciones ganadoras)
                # Usamos 'or' para decir "si pasa esto O esto O esto"
                # Usamos 'and' para decir "si yo elegí X Y la pc eligió Y"
                # (1=Piedra, 2=Papel, 3=Tijera)
                elif (opcion_juego == 1 and opcion_pc == 3) or \
                     (opcion_juego == 2 and opcion_pc == 1) or \
                     (opcion_juego == 3 and opcion_pc == 2):
                         print("Resultado: ¡TÚ GANAS la ronda!")
                         # Actualizamos tu marcador sumando 1
                         marcador_jugador += 1
                         
                # CASO C: TÚ PIERDES (Cualquier otro caso)
                else:
                    print("Resultado: ¡La PC GANA la ronda!")
                    # Actualizamos el marcador de la PC sumando 1
                    marcador_pc += 1
                
                print("--------------------------------")
                time.sleep(1) # Pausa para leer el resultado antes de la siguiente ronda
                
            else:
                # Si puso un número, pero no es 1, 2, 3 ni 4.
                print("\n[ERROR]: Opción no válida. Por favor elige entre 1 y 4.")
                
        except ValueError:
            # Si puso letras en lugar de números saldra un mensaje de error pero no cerrara el programa.
            print("\n[ERROR]: Entrada inválida. Debes ingresar un número entero.")

    # Cuando el while termina (porque eligió 4), se muestra el resultado final de esta sesión.
    print(f"\nFin de la partida. Resultado final: Jugador [{marcador_jugador}] - PC [{marcador_pc}]")
    time.sleep(1)

def main():
    """
    Función principal que maneja el MENÚ DE INICIO de la aplicación.
    """
    # --- VARIABLE (Interruptor principal) ---
    juego_corriendo = True 
    
    # El bucle principal "mientras la aplicación esté corriendo"
    while juego_corriendo:
        print("\n=======================================")
        print("   PIEDRA, PAPEL O TIJERA - JUEGO   ")
        print("=======================================")
        print("1. Iniciar Nueva Partida")
        print("2. Ver Reglas")
        print("3. Salir de la Aplicación")
        print("=======================================")
        
        try:
            # Leemos la elección del menú principal
            menu_principal = int(input("Selecciona una opción del menú: "))
            
            # El cerebro que dirige el tráfico a las otras funciones
            if menu_principal == 1:
                jugar_partida() # Salta a la función del juego
            elif menu_principal == 2:
                mostrar_reglas() # Salta a la función de reglas
            elif menu_principal == 3:
                print("\nCerrando aplicación. ¡Hasta luego!")
                juego_corriendo = False # Apaga el interruptor principal, el programa terminará
            else:
                 print("\n[ERROR]: Por favor elige 1, 2 o 3.")
                 
        except ValueError:
             print("\n[ERROR]: Entrada inválida en el menú principal. Ingresa un número.")

# --- PUNTO DE ARRANQUE ---
# Esta es la orden final que le dice a Python: "¡Empieza a ejecutar la función principal ya!"
main()