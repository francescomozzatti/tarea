from prog.ej import cartonfun

def test_cartonfun():
    cartoncito=cartonfun()
    contador=0
    bandera=1
    lista=[0,0,0,0,0,0,0,0,0]
    for fila in cartoncito:
        it=0
        for celda in fila:
            contador=contador+celda
            lista[it]=lista[it]+celda
            it=it+1

    for celda in lista:
        if(celda==0): 
                    bandera=0

    assert contador>14

    assert contador<16

    assert bandera==1