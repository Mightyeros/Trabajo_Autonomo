# Proyecto Final: Nuestro juego de Piedra, Papel o Tijera (Versión 2.0)

Para el proyecto final, decidí tomar el juego clásico de "Piedra, Papel o Tijera" y programarlo no solo para que funcione, sino para que esté bien hecho por dentro, siguiendo las reglas aprendidas en clase.

Quiero mostrar cómo un programa puede tomar decisiones "inteligentes" (saber quién gana) usando reglas claras. Además, quise dar el salto de hacer un código básico a uno más profesional, dividiéndolo en partes (módulos), tal como se aprendió en clase.

¿Cómo mejoré mi código?
Mi primer intento del juego funcionaba, pero el código era un poco desordenado, con muchísimas condiciones `if` una dentro de otra para decidir quién ganaba.
Para esta versión final, aplique lo que aprendimos en las últimas clases:

- Creé mi propia "Librería"
En lugar de tener todo el código amontonado en un solo archivo, lo separé en dos:
1.  `main.py`: Es la "cara" del programa. Se encarga de mostrar el menú, pedirte tu jugada y llevar el marcador.
2.  `libreria_juego.py`: Es el "cerebro". Aquí están guardadas las reglas y es donde se decide quién gana la ronda.

Hacer esto es muy útil porque si mañana quiero cambiar las reglas, solo editaria el archivo de la librería sin dañar el resto del programa.

- Usé un "Diccionario" en vez de muchos "ifs"
Esta fue la mejora más grande. Antes, para saber si Piedra le ganaba a Tijera, teníamos que escribir un `if` específico para eso.

Ahora, usé un diccionario de Python que funciona como una tabla de reglas. Es algo así:
* Si tienes Piedra (1), le ganas a Tijera (3).
* Si tienes Papel (2), le ganas a Piedra (1).
* Si tienes Tijera (3), le ganas a Papel (2).

Cuando juegas, el programa solo mira esta tabla para decidir el ganador. Esto hace que el código sea mucho más corto y fácil de entender, aplicando ideas de la "Programación Funcional".

Características del juego
* Puedes jugar todas las rondas que quieras y el programa lleva la cuenta del marcador.
* La computadora juega al azar, así que nunca sabes qué va a sacar gracias a la libreria random.
* Si te equivocas y escribes una letra en vez de un número, el programa no se rompe; te avisa del error y te deja intentar de nuevo (usé `try/except`).

Importante
- Descarga los dos archivos (`main.py` y `libreria_juego.py`) y guárdalos juntos en la misma carpeta.
- Ejecuta el archivo principal:
   "main.py"
- Sigue las instrucciones en pantalla usando los números del teclado. ¡Que te diviertas!

