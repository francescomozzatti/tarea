from prog.carton_primitivo import cartonfun

def test_cartonfun():
    cartoncito=cartonfun()
    contador=0
    for fila in cartoncito:
        for celda in fila:
            contador=contador+celda

    assert contador>14

