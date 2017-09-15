# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(anios_de_trabajo, cap_de_end, anios_viv_actual, estado_civil, dependientes):
    if anios_de_trabajo >=2 :
        if estado_civil == 'soltero' :
            prestamo = 'D'
        elif estado_civil == 'divorciado' :
            if dependientes == 0 :
                prestamo = 'M'
            else:
                prestamo = 'A'
        else:
            prestamo = 'A'
    else:
        if cap_de_end >= 0.75 :
            prestamo = 'M'
        else:
            if anios_viv_actual >= 1.25 :
                prestamo = 'A'
            else:
                prestamo = 'D'
    return prestamo
