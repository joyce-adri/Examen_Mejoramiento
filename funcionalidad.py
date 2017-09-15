# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def prestamos_hipotecarios(dependencia, anios, civil, capacidad, vivienda, trabajo, edad):
    prestamo = "denegado"
    if anios >= 2:
        if civil is "casado":
            prestamo = "aprobado"
        elif civil is "soltero":
            prestamo = "denegado"
        elif civil is "divorciado":
            if dependencia == 0:
                prestamo= "manual"
            elif dependencia > 0:
                prestamo= "aprobado"

    elif anio <= 2:
        if capacidad >=75:
            prestamo= "manual"
        elif capacidad <75:
            if vivienda >=1.5:
                prestamo="aprobado"
            elif vivienda < 1.5:
                prestamo ="denegado"

    return prestamo