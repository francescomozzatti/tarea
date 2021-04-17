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