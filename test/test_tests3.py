#esto es para que tenga diferencia el test de la escuala con el de mi casa para poder hacer merge
from prog.ej import cartonfun

def test_cartonfun():
    cartoncito=cartonfun()
    bandera=1
    lista=(0,0,0,0,0,0,0,0,0)
    for fila in cartoncito:
            if(fila==lista):
                             bandera=0

    assert bandera==1