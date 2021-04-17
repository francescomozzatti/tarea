from prog.validar_orden_DOWNRIGHT import nums_orden
from prog.validar_consecutivas import carton_casillas_consecutivas
from prog.validar_columnas import nums_cant_en_columnas
from prog.validar_filas import nums_cant_en_filas
from prog.validar_irrepeticion import nums_irrepetibles
from prog.validar_1a90 import nums1a90
from prog.validar_15 import nums_15
from prog.carton_FINAL import carton_carton


def test_carton_el_carton():
    mi_carton=carton_carton()

    assert nums_orden(mi_carton) and carton_casillas_consecutivas(mi_carton) and nums_15(mi_carton) and nums_cant_en_columnas(mi_carton) and nums_cant_en_filas(mi_carton) and nums_irrepetibles(mi_carton) and nums1a90(mi_carton) == 1