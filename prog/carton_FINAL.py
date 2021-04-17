from prog.validar_consecutivas import carton_casillas_consecutivas
from prog.validar_orden_DOWNRIGHT import nums_orden
from prog.carton_posible import carton_bingos

def carton_carton():	
    contador=0
    while 1:
          contador=contador+1
          mi_carton=carton_bingos()
          if(carton_casillas_consecutivas(mi_carton) and nums_orden(mi_carton)):
	                                                                        return mi_carton
                    

