# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(at,estadoCivil, dependientes,capacidadEndeudamiento, aniosVivienda):# aT años de Trabajo

    if at >= 2 :
        if estadoCivil == "casado" :
            return "A Aprobado"
        elif estadoCivil == "soltero" :
            return "D Denegado"
        elif estadoCivil == "divorciado" :
            if dependientes > 0 :
                return "A Aprobado"
            else :
                return "M Revision Manual"
    elif capacidadEndeudamiento >= 75 :
        return "M Revision Manual"
    elif aniosVivienda >= 1.5 :
        return "A Aprobado"
    else:
        return "D Denegado"
    