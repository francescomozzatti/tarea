from validar_consecutivas import carton_casillas_consecutivas
from validar_orden_DOWNRIGHT import nums_orden
from carton_posible import carton_bingos

def carton_carton():	
    while 1:
          mi_carton=carton_bingos()
          if(carton_casillas_consecutivas(mi_carton) and nums_orden(mi_carton)):
	                                                                       return mi_carton

print(carton_carton())                    

