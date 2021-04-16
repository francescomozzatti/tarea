def nums_cant_en_columnas(carton):
    tot=0 
    c1=0
    c2=0
    for columna in range(0,9):
        if(tot==2):
             c2=c2+1
        if(tot==1):
             c1=c1+1
        tot=0
        for fila in range(0,3):
            celda=carton[fila][columna]
            if(celda>0):
                          tot=tot+1
    if(tot==2):
                 c2=c2+1 
    if(tot==1):
                 c1=c1+1
                
    return c2==6 and c1==3
