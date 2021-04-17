from validar_consecutivas_primitiva import aux_fila

def carton_casillas_consecutivas(carton):
    bandera=1
    for fila in carton:
        bandera=bandera and aux_fila(fila)
                    
    return bandera==1

