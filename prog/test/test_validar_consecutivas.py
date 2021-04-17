from prog.validar_consecutivas import carton_casillas_consecutivas

def test_carton_casillas_concecutivas():
    mi_carton=((1,2,0,0,5,0,0,8,9,),(10,11,0,0,14,15,0,16,0,),(0,17,0,18,19,0,0,20,21,))
    mi_carton2=((1,2,0,0,5,0,0,8,9,),(10,11,0,0,14,15,0,16,0,),(0,17,0,18,0,0,0,20,21,))

    assert carton_casillas_consecutivas(mi_carton)==1
    assert carton_casillas_consecutivas(mi_carton2)==0