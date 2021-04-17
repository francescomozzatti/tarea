from prog.validar_15 import nums_15

def test_nums_15_2():
    mi_carton=((1,2,3,4,5,6,7,8,9,),(10,11,12,13,14,15,0,9,0,),(0,0,0,0,0,0,0,0,0,))     

    assert nums_15(mi_carton)==0