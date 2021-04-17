import random
import math

def nums_orden(carton):
    bandera=1
    max=0
    for columna in range(0,9):
        for fila in range(0,3):
            celda=carton[fila][columna]
            if(celda>max):
                          max=celda
            if(celda>0 and celda<max):
                          bandera=0
                    
    return bandera==1
#esta funcion soluciona todos los probelemas de orden, en cada columna estan ordenados para a bajo, y si aparece un numero, a la izquierda son todos mas chicos. Esto es porque sigue un recorrido bajando por cada columna y avanzando de columna en colmna para la derecha. 








def carton_casillas_consecutivas(carton):
    bandera=1
    for fila in carton:
        bandera=bandera and aux_fila(fila)
                    
    return bandera==1













def aux_fila(fila):
    bandera=1
    conv=0
    conn=0
    for celda in fila:
        if(celda==0): 
            conv=conv+1
            conn=0
        if(celda>0):
           conv=0
           conn=conn+1
        if(conn>2):
           bandera=0 
        if(conv>2):
           bandera=0  
                    
    return bandera==1















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



def carton_carton():	
    while 1:
          mi_carton=carton_bingos()
          if(carton_casillas_consecutivas(mi_carton) and nums_orden(mi_carton)):
	                                                                       return mi_carton

print(carton_carton())                    



