# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Prestamo:
    num_dependientes=0
    estado_civil=""
    capacidad_endeudamiento=0
    ano_viviendaactual=0
    ano_trabajoactual=0
    edad=0
    def __init__(self, num_dependientes, estado_civil, capacidad_endeudamiento, ano_viviendaactual, ano_trabajoactual, edad):
        self.num_dependientes = num_dependientes
        self.estado_civil = estado_civil
        self.capacidad_endeudamiento = capacidad_endeudamiento
        self.ano_viviendaactual = ano_viviendaactual
        self.ano_trabajoactual = ano_trabajoactual
        self.edad = edad

class Programa:
    def AprobarPrestamo(self, prestamo):
        if(prestamo.ano_trabajoactual>=2):
            if(prestamo.estado_civil=="Married"):
                print "A"
            if(prestamo.estado_civil=="Single"):
                print "D"
            if(prestamo.estado_civil=="Divorced"):
                if(prestamo.num_dependientes>0):
                    print "A"
                else:
                    print "M"

        else:
            if(prestamo.capacidad_endeudamiento>=75):
                print "M"
            else:
                if(prestamo.ano_viviendaactual>=1.5):
                    print "A"
                else:
                    print "D"

