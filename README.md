# Trabajo_Autonomo
Juego seleccionado: Piedra, Papel o Tijera

¿De qué trata este proyecto?
Este es mi desarrollo del clásico juego "Piedra, Papel o Tijera". Mi objetivo principal fue tomar las estructuras lógicas y los ciclos que hemos aprendido y convertirlos en algo divertido: una experiencia donde el usuario pueda retar a la computadora sin interrupciones.

Mi enfoque: Pensando como el usuario
Para diseñar este juego no quise limitarme a cumplir con "una partida y ya". Analicé que una aplicación necesita mantener al usuario involucrado, manejar posibles errores y dar un sentido de progreso dando puntuaciones de las victorias y derrotas..

Así que planteé las siguientes soluciones:

Sistema de Puntuación Para transformar el juego se implementara un contador de victorias
La existencia del bucle principal motiva al usuario a seguir jugando para superar a la máquina.
Se implementará mediante dos variables contadoras de tipo entero definidas en el código como `player_score` y `computer_score`. Estas se inicializarán a `0` *antes* de entrar al bucle principal. Dentro del bucle, tras la lógica condicional que determina el ganador de la ronda, se utilizarán operadores de asignación de suma nativos de Python (ej. `player_score += 1` si gana el usuario, o `computer_score += 1` si gana la PC)

Juego Continuo (¡Que no se cierre!): Es frustrante que un programa se cierre apenas termina una ronda. Por eso, implementé un bucle principal (un while) que mantiene el juego vivo, permitiendo jugar tantas revanchas como el usuario quiera hasta que decida salir.

A prueba de errores (Validación): Todos nos equivocamos al teclear. Si el usuario escribe una letra en lugar de un número o elige una opción que no existe (como dinamita), el programa no debería colapsar. He diseñado el código con bloques de manejo de errores (try-except e if) para "atrapar" esas equivocaciones y pedirle amablemente al usuario que intente de nuevo.

El factor suerte: Para que sea un juego real, la computadora no puede ser predecible. Usé la librería random de Python para asegurar que la elección de la máquina sea totalmente al azar.

Justificación de Herramientas

Lenguaje y Entorno:
Se eligió Python por su sintaxis clara y legible, ideal para implementar lógica compleja de comparaciones (`if/elif/else`). Además, su manejo de librerías como `random` es ideal para el juego escogido.

Se utiliza Spyder como Entorno dado que ofrece un excelente entorno para análisis de datos y ejecución paso a paso, lo que facilita la depuración de las estructuras lógicas y la visualización de variables en tiempo real durante el desarrollo del juego.

Eleccion del Diagrama
Se decidio utilizar Diagramas de Flujo para la fase de diseño. 
Dado que el juego es un proceso secuencial con puntos de decisión claros: 

¿Ganó A o B?
 
¿Es válida la entrada?
 
¿Quiere salir el usuario? 

El diagrama de flujo es el más adecuado para visualizar el algoritmo antes de la codificación porque permite identificar claramente dónde se necesitan bucles y dónde se ramifica la lógica condicional.


