from prog.validar_orden_DOWNRIGHT import nums_orden

def test_nums_orden():
    mi_carton=((1,4,7,10,13,0,0,0,0,),(2,5,8,11,14,0,0,0,0,),(3,6,9,12,15,70,0,0,0,))     

    assert nums_orden(mi_carton)==1