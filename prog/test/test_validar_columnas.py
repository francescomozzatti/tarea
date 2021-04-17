from prog.validar_columnas import nums_cant_en_columnas

def test_nums_cant_en_columnas():
    mi_carton=((1,2,3,4,5,6,7,8,9,),(10,11,0,0,14,15,0,16,90,),(0,0,0,0,0,0,0,0,0,))
    
    assert nums_cant_en_columnas(mi_carton)==1
