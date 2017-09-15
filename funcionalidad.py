# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, dependientes, estadoC):
    solicitud = "D"
    if aniosTrabajo > 2:
        if estadoC == "soltero":
            solicitud = "D"
        elif estadoC == "casado":
        	solicitud = "A"
        elif estadoC == "divorciado":
        	if dependientes == 0:
        		solicitud = "M"
    		elif dependientes > 0:
    			solicitud = "A"
    else:
    	if capacidadEndeudamiento >= 75:
            solicitud = "M"
        else:
        	if aniosVivienda >= 1.5:
        		solicitud = "A"
    		else:
    			solicitud = "D"
   
    return solicitud
