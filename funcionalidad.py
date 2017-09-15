# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes):
    prestamo = "D"
    if aniosTrabajo >= 2:
        if estadoCivil == "divorciado":
            if numDependientes > 0:
                prestamo = "A"
            elif numDependientes == 0:
                prestamo = "M"
        elif estadoCivil == "soltero":
            prestamo = "D"
        elif estadoCivil == "casado":
            prestamo = "A"
    else:
        if capacidadEndeudamiento >= 75:
            prestamo = "M"
        else:
            if aniosVivienda >= 1.5:
                prestamo = "A"
            else:
                prestamo = "D"
    return prestamo


