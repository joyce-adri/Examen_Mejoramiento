# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(anios_t, capac_end, anios_viv, est_civil,dependientes):
    if anios_t < 2:
        if capac_end <75:
            if anios_viv < 1.5:
                return "denegado"
            else:
                return "aprobado"
        else:
            return "manual"
    else:
        if est_civil == "single":
            return "denegado"
        elif est_civil == "married":
            return "aprobado"
        else:
            if dependientes > 0:
                return "aprobado"
            else:
                return "manual"