# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(dep, ec, ce, ava, at, edad):
    if(edad>=18):
        if(at>=2):
            if(ec == "divorciado"):
                if(dep ==0):
                    return "M"
                elif(dep >0):
                    return "A"
            elif(ec == "soltero"):
                return "D"
            elif(ec == "casado"):
                return "A"
        else:
            if(ce >= 75):
                return "M"
            else:
                if(ava >=1.5):
                    return "A"
                else:
                    return "D"
    else:
        return "D"