import random
import math

def carton_bingos():
    contador=0


    carton=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    numerosCarton=0


    while numerosCarton<15:
        contador=contador+1
        if contador==50:
              return carton_bingos()
        numero=random.randint(1,90)


        columna=math.floor(numero/10)
        if columna==9:
                columna=8
        huecos=0
        for i in range(0,3):
            if carton[i][columna]==0:
                huecos=huecos+1
            if carton[i][columna]==numero:
                huecos=0
                break
        if(huecos<2):
            continue


        fila=0
        for j in range(0,3):
            huecos=0
            for i in range(9):
                if carton[fila][i]==0:
                    huecos=huecos+1
            if huecos<5 or carton[fila][columna]!=0:
                fila=fila+1
            else:
                break
        if fila==3:
            continue

        carton[fila][columna]=numero
        numerosCarton=numerosCarton+1
        contador=0
    for x in range(0,9):
        huecos=0
        for y in range(3):
            if carton[y][x]==0:
                huecos=huecos+1
        if huecos==3:
            return carton_bingos()

    return carton