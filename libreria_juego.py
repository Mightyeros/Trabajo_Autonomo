# -*- coding: utf-8 -*-
"""
NOMBRE DEL ARCHIVO: libreria_juego.py

DESCRIPCIÓN:
Aquí guardamos las reglas del juego
y las funciones que deciden quién gana.
Este archivo no hace nada si lo ejecutas solo; sirve para que el programa
principal (main.py) lo use.
"""

# --- Diccionario ---

# Este diccionario es el corazón del juego. Define las reglas "piedra, papel o tijera".
# La clave es la jugada, y el valor es a qué le gana esa jugada.
# Usamos números para hacerlo más fácil: 1=Piedra, 2=Papel, 3=Tijera.
REGLAS_VICTORIA = {
    1: 3, # Piedra le gana a Tijera (1 le gana a 3)
    2: 1, # Papel le gana a Piedra (2 le gana a 1)
    3: 2  # Tijera le gana a Papel (3 le gana a 2)
}

# Este diccionario simple nos ayuda a traducir los números a palabras
# para mostrar mensajes bonitos en pantalla.
NOMBRES_OPCIONES = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera"
}

# --- FUNCIONES ---

def obtener_nombre_jugada(opcion_numerica):
    """
    Le das un número (1, 2 o 3) y te devuelve el nombre (Piedra, Papel...).
    Si el número no es válido, te dice "Desconocido".
    Usa el método .get() del diccionario para no fallar si la clave no existe.
    """
    return NOMBRES_OPCIONES.get(opcion_numerica, "Desconocido")

def determinar_ganador(jugada_usuario, jugada_pc):
    """
    Esta es la función más importante. Recibe lo que eligieron tú y la PC,
    consulta el diccionario de reglas, y decide quién ganó la ronda.
    
    Devuelve una de tres palabras clave: "empate", "usuario" o "pc".
    """
    # Primero, lo más fácil: si eligieron lo mismo, es empate.
    if jugada_usuario == jugada_pc:
        return "empate"
    
    # Preguntamos: ¿A qué le gana mi jugada? (REGLAS_VICTORIA.get(jugada_usuario))
    # Si la respuesta es exactamente lo que sacó la PC, ¡entonces gané yo!
    elif REGLAS_VICTORIA.get(jugada_usuario) == jugada_pc:
        return "usuario"
    
    # Si no fue empate y no gané yo, entonces por descarte ganó la PC.
    else:
        return "pc"

def obtener_reglas_texto():
    """Solo devuelve una lista con las frases de las reglas para imprimirlas."""
    return [
        "1. Piedra aplasta Tijera.",
        "2. Tijera corta Papel.",
        "3. Papel envuelve Piedra."
    ]

