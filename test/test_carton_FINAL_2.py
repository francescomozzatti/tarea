from prog.validar_filas import nums_cant_en_filas
from prog.validar_irrepeticion import nums_irrepetibles
from prog.validar_1a90 import nums1a90
from prog.validar_15 import nums_15
from prog.carton_FINAL import carton_carton

  

def test_carton_el_carton4():
    mi_carton=carton_carton()
    assert nums_cant_en_filas(mi_carton)==1 

def test_carton_el_carton5():
    mi_carton=carton_carton()
    assert nums_irrepetibles(mi_carton)==1

def test_carton_el_carton6():
    mi_carton=carton_carton()
    assert nums1a90(mi_carton)==1

