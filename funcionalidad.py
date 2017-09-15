# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def aprobarPrestamo(anios_trabajo, estado_civil, endeudamiento, anios_vivienda, dependientes ):
    if anios_trabajo >=2 : #1
        if estado_civil == 'divorced':
            if dependientes > 0:
                estado = 'A'
            elif dependientes == 0 :
                estado = 'M'
        elif estado_civil == 'single':
            estado = 'D'
        elif estado_civil == 'Married':
            estado = 'A'
    elif anios_trabajo <2: #2
        if endeudamiento >= 75:
            estado = 'M'
        elif endeudamiento < 75:
            if anios_vivienda >= 1.5:
                estado = 'A'
            elif anios_vivienda < 1.5:
                estado = 'D'
    return  "Calificacion: %s" % (estado)