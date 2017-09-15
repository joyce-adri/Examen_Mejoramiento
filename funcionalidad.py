# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Banco():
    def aprobarPrestamo(self, endeudamiento, estadocivil, aniosvivienda, aniostrabajo, dependientes):
        if aniostrabajo < 2:

            if endeudamiento < 75:

                if aniosvivienda < 1.5:
                    return 'D'
                else:
                    return 'A'

            else:
                return 'M'
        else:

            if estadocivil == 'CASADO':
                return 'A'
            elif estadocivil == 'SOLTERO':
                return 'D'
            elif estadocivil == 'DIVORCIADO':

                if dependientes == 0:
                    return 'M'
                else:
                    return 'A'
            else:
                return 'D'
