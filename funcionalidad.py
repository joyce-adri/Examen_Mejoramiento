# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(at,estadoCivil, dependientes,capacidadEndeudamiento, aniosVivienda):# aT años de Trabajo

    if at >= 2 :
        if estadoCivil == "casado" :
            return "A"
        elif estadoCivil == "soltero" :
            return "D"
        elif estadoCivil == "divorciado" :
            if dependientes > 0 :
                return "A"
            else :
                return "M"
    elif capacidadEndeudamiento >= 75 :
        return "M"
    elif aniosVivienda >= 1.5 :
        return "A"
    else:
        return "D"

