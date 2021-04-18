def nums_irrepetibles(carton):
    bandera=1
    cont=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] #lista de aparaciones para cada numero entre 1 y 90, hay de mas pero no importa.
    for fila in carton:
        for celda in fila:
            if(cont[celda]==1): #si ya aparecio y volvio a aparecer... FALSE
                           bandera=0  
            if(celda>0 and cont[celda]==0): #si aparece lo pongo en la lista de apariciones 
                           cont[celda]=1 
                    

    return bandera==1