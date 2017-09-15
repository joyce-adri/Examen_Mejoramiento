# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Solicitante:
    num_dependientes = 0
    estado_civil = ""
    capacidad_endeudamiento = 0
    anio_vivienda = 0
    anio_trabajo = 0
    edad = 0
    email = ""
    monto = 0

    def __init__(self, dependientes, estado, cap_endeu, a_vivienda, a_trabajo, edad, email):
        self.num_dependientes = dependientes
        self.estado_civil = estado
        self.capacidad_endeudamiento = cap_endeu
        self.anio_vivienda = a_vivienda
        self.anio_trabajo = a_trabajo
        self.edad = edad
        self.email = email
        

    def AprobarPrestamo(self):
        if self.anio_trabajo >= 2:  #1
            if self.estado_civil == "Married":   #2
                return "A"  #3
            elif self.estado_civil == "Single":  #4
                return "D"  #5
            else:   #6
                if self.num_dependientes > 0:   #7
                    return "A"  #8
                else:   #9
                    return "M"  #10
        else:   #11
            if self.capacidad_endeudamiento >= 75:  #12
                return "M"  #13
            else:   #14
                if self.anio_vivienda >= 1.5:   #15
                    return "A"  #16
                else:   #17
                    return "D"  #18

    def CalcularMontoPrestamo(self):
        if self.AprobarPrestamo() == "A":
            if self.edad < 18:
                self.monto = 0
            elif self.edad < 35 or self.edad > 65:
                self.monto = 80000
            elif self.edad >=35 and self.edad <= 50:
                self.monto = 20000
            elif self.edad >=51 and self.edad <= 65:
                self.monto = 120000

    def EnviarEmail(self):
        print("Monto %s" % (self.monto))

    