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