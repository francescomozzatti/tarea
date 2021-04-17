def nums1a90(carton):
    bandera=1
    for fila in carton:
        for celda in fila:
            if(celda<0 or celda>90):
                                      bandera=0

    return bandera==1