def nums_cant_en_filas(carton):
    contador=0
    bandera=1
    for fila in range(0,3):
        for columna in range(0,9):
            celda=carton[fila][columna]
            if(celda>0):
                   contador=contador+1
        if(contador!=5):
                   bandera=0
        contador=0
    
    return bandera==1
