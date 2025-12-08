# Trabajo_Autonomo
Juego seleccionado: Piedra, Papel o Tijera

¿De qué trata este proyecto?
Este es mi desarrollo del clásico juego "Piedra, Papel o Tijera". Mi objetivo principal fue tomar las estructuras lógicas y los ciclos que hemos aprendido y convertirlos en algo divertido: una experiencia donde el usuario pueda retar a la computadora sin interrupciones.

Mi enfoque: Pensando como el usuario
Para diseñar este juego no quise limitarme a cumplir con "una partida y ya". Analicé que una aplicación necesita mantener al usuario involucrado, manejar posibles errores y dar un sentido de progreso dando puntuaciones de las victorias y derrotas..

Así que planteé las siguientes soluciones:

Sistema de Puntuación 
Para que el juego sea competitivo, es necesario un marcador que vaya sumando las victorias del jugador y de la maquina
con el fin de querer vencer a la PC y con ese objetivo motivarse a seguir jugando
Se implementará mediante dos variables contadoras de tipo entero definidas claramente como `marcador_jugador` y `marcador_pc`. Estas se inicializan a `0` al comenzar una nueva partida. Dentro del bucle de juego, tras determinar el ganador de la ronda, se utilizarán operadores de asignación para actualizar el estado.

Navegación Estructurada (Menú Principal)
Se ha implementado un menú de inicio general mediante una estructura repetitiva principal (`while`).
Control de Flujo: Para controlar este bucle principal, se utiliza una variable booleana descriptiva llamada `juego_corriendo`, que actúa como el "interruptor" de la aplicación. La elección del usuario en el menú se almacena en la variable numérica `menu_principal`, la cual es evaluada por estructuras condicionales (`if/elif`) para dirigir el flujo a la función correspondiente (jugar, reglas o salir).

Juego Continuo (¡Que no se cierre!): Es frustrante que un programa se cierre apenas termina una ronda. Por eso, implementé un bucle principal (un while) que mantiene el juego vivo, permitiendo jugar tantas revanchas como el usuario quiera hasta que decida salir.

A prueba de errores (Validación): Todos nos equivocamos al teclear. Si el usuario escribe una letra en lugar de un número o elige una opción que no existe (como dinamita), el programa no debería colapsar. He diseñado el código con bloques de manejo de errores (try-except e if) para "atrapar" esas equivocaciones y pedirle amablemente al usuario que intente de nuevo.

El factor suerte: Para que sea un juego real, la computadora no puede ser predecible. Usé la librería random de Python para asegurar que la elección de la máquina sea totalmente al azar.

Justificación de Herramientas

Lenguaje y Entorno:
Se eligió Python por su sintaxis clara y legible, ideal para implementar lógica compleja de comparaciones (`if/elif/else`). Además, su manejo de librerías como "random" es ideal para el juego escogido y tambien se utilizara la libreria "time" para darle pausas dramaticas en ciertas partes del juego para que no se vea tan bruscas las transiciones de opciones.

Se utiliza Spyder como Entorno dado que ofrece un excelente entorno para análisis de datos y ejecución paso a paso, lo que facilita la depuración de las estructuras lógicas y la visualización de variables en tiempo real durante el desarrollo del juego.

Eleccion del Diagrama
Se decidio utilizar Diagramas de Flujo para la fase de diseño. 
Dado que el juego es un proceso secuencial con puntos de decisión claros: 

¿Ganó A o B?
 
¿Es válida la entrada?
 
¿Quiere salir el usuario? 

El diagrama de flujo es el más adecuado para visualizar el algoritmo antes de la codificación porque permite identificar claramente dónde se necesitan bucles y dónde se ramifica la lógica condicional.
3. Implementación de la Lógica del Juego (FASE 2 TERMINADA)

En la segunda parte del trabajo autónomo, se completó el núcleo funcional del juego, reemplazando los marcadores de posición por la lógica condicional definitiva. Se implementaron los siguientes puntos:

Elección Aleatoria de la PC: Se utilizó la librería `random.randint(1, 3)` para garantizar que la elección de la computadora sea impredecible en cada ronda.

Motor de Reglas (El Árbitro): Se implementó una estructura condicional compuesta (`if/elif/else`) que evalúa las elecciones del jugador frente a la PC. Esta estructura verifica primero el empate y luego utiliza operadores lógicos (`or`, `and`) para determinar si el jugador ha ganado según las reglas clásicas (Piedra vence Tijera, Tijera vence Papel, Papel vence Piedra). Cualquier otro caso resulta en victoria para la PC.

Actualización Dinámica del Marcador: Dependiendo del resultado determinado por el motor de reglas, se incrementa la variable contadora correspondiente (`marcador_jugador += 1` o `marcador_pc += 1`), reflejando el progreso en tiempo real en la siguiente iteración del bucle.


