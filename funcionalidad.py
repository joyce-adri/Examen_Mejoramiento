# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(dependientes, estado, capacidaddeuda, tiempovivienda, tiempotrabajo, edad):
    if(edad>=18):
        if(tiempotrabajo>=2):
            if(estado == "divorciado"):
                if(dependientes ==0):
                    return "M"
                elif(dependientes >0):
                    return "A"
            elif(estado == "soltero"):
                return "D"
            elif(estado == "casado"):
                return "A"
        else:
            if(capacidaddeuda >= 75):
                return "M"
            else:
                if(tiempovivienda >=1.5):
                    return "A"
                else:
                    return "D"
    else:
        return "D"