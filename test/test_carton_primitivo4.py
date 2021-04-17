#esto es para que tenga diferencia el test de la escuala con el de mi casa para poder hacer merge. "MODIFICACION".
from prog.carton_primitivo import cartonfun

def test_cartonfun():
    cartoncito=cartonfun()
    bandera=1
    lista=(0,0,0,0,0,0,0,0,0)
    for fila in cartoncito:
            if(fila==lista):
                             bandera=0

    assert bandera==1
#esto es para que tenga diferencia el test de mi casa con el de la escuela para poder hacer merge