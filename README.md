[![Build Status](https://travis-ci.com/francescomozzatti/tarea.svg?branch=master)](https://travis-ci.com/francescomozzatti/tarea)
[![Coverage Status](https://coveralls.io/repos/github/francescomozzatti/tarea/badge.svg)](https://coveralls.io/github/francescomozzatti/tarea)

# Bingo
En este reopisitorio se encuentra un programa en Python, que genera (al azar) e imprime un carton de Bingo siguiendo las reglas necesarias. Tambien hay adjuntos en la carpeta `test` varios test automatizados que validan el programa principal y tambien que testean los programas de validacion.

## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:
* Cada carton es una matrix de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.


## El programa
El programa esta en el archivo `prog/carton_FINAL.py`, especificamente la funcion `carton_carton()` es la que retorna un dato del tipo `carton=[[...],[...],[...]]` que luego es mostrada en pantalla. El codigo esta basado en un algoritmo escrito en `PHP` traducido a `Python` que genera tambien un carton, pero, al este no cumplir con todas las reglas no es valido (este algoritmo esta en la funcion `carton_bingos()` del archivo). Para solucionar esto, la funcion `carton_carton()` ejecuta la funcion `carton_bingos()` tantas veces como sea necesario para que retorne un carton valido (esto lo corrobora con las funciones de validacion en  el mismo archivo).

Se puede correr el codigo con el comando `python prog/carton_FINAL.py` desde la carpeta `tarea` y nos mostara en pantalla algo como: 

`[[4, 0, 25, 0, 46, 52, 0, 0, 84], [7, 12, 0, 33, 0, 57, 0, 73, 0], [0, 15, 27, 0, 48, 0, 64, 78, 0]]`
