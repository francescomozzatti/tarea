from prog.nums_orden import nums_orden
from prog.carton_casillas_consecutivas import carton_casillas_consecutivas
from prog.nums_cant_en_columnas import nums_cant_en_columnas
from prog.nums_cant_en_filas import nums_cant_en_filas
from prog.nums_irrepetibles import nums_irrepetibles
from prog.nums1a90 import nums1a90
from prog.nums_15 import nums_15
from prog.carton_el_carton import carton_carton


def test_carton_el_carton():
    mi_carton=carton_carton()

    assert nums_orden(mi_carton) and carton_casillas_consecutivas(mi_carton) and nums_15(mi_carton) and nums_cant_en_columnas(mi_carton) and nums_cant_en_filas(mi_carton) and nums_irrepetibles(mi_carton) and nums1a90(mi_carton) == 1