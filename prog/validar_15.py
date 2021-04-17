def nums_15(carton):
    contador=0
    for fila in carton:
        for celda in fila:
            if(celda>0):
                contador=contador+1
                   
    return contador==15