from prog.carton_primitivo import cartonfun

def test_cartonfun():
    cartoncito=cartonfun()
    bandera=1
    lista=[0,0,0,0,0,0,0,0,0]
    for fila in cartoncito:
        it=0
        for celda in fila:
            lista[it]=lista[it]+celda
            it=it+1

    for celda in lista:
        if(celda==0): 
                    bandera=0

    assert bandera==1

#veo si hay columnas totalmente vacias, ya que si en lista al final hay algun 0, es que los tres numeros de esa columna suman 0,, y por tanto son 3 ceros. 