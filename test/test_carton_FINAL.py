from prog.validar_columnas import nums_cant_en_columnas
from prog.validar_15 import nums_15
from prog.carton_FINAL import carton_carton
from prog.carton_FINAL import nums_orden
from prog.carton_FINAL import carton_casillas_consecutivas

def test_carton_el_carton1():
    mi_carton=carton_carton()
    assert nums_orden(mi_carton)==1 
 
def test_carton_el_carton2():
    mi_carton=carton_carton()
    assert carton_casillas_consecutivas(mi_carton)==1 

def test_carton_el_carton3():
    mi_carton=carton_carton()
    assert nums_cant_en_columnas(mi_carton)==1 

