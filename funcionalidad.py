# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(dep, ec, ce, ava, at, edad):
    if(edad>=18):
        if(at>=2):
            if(ec == "divorciado"):
                if(dep ==0):
                    return "MM"
                elif(dep >0):
                    return "Aprobado"
            elif(ec == "soltero"):
                return "Denegado"
            elif(ec == "casado"):
                return "Aprobado"
        else:
            if(ce >= 75):
                return "MM"
            else:
                if(ava >=1.5):
                    return "Aprobado"
                else:
                    return "Denegado"
    else:
        return "Denegado"