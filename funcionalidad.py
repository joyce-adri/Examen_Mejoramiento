# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda):
    if yearsTrabajo >= 2:
        if estCivil == "Single":
            return "D"
        elif estCivil == "Married":
            return "A"
        elif estCivil == "Divorced":
            if dep > 0:
                return "A"
            elif dep == 0:
                return "M"
    elif yearsTrabajo < 2:
        if end >= 75:
            return "M"
        elif end < 75:
            if yearsVivienda < 1.5:
                return "D"
            elif yearsVivienda >= 1.5:
                return "A"