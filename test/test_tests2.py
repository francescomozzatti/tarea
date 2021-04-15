from prog.ej import cartonfun

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