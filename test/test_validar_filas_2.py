from prog.validar_filas import nums_cant_en_filas

def test_nums_cant_en_columnas_2():
    mi_carton=((1,2,3,4,5,90,0,0,0,),(10,11,12,13,14,0,0,0,0,),(1,2,3,4,5,0,0,0,0,))
    
    assert nums_cant_en_filas(mi_carton)==0
