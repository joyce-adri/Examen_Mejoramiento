# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad
from funcionalidad import *

#from Prestamo import prestamo
#from Programa import programa


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
    
    def test_1(self):
        prestamo= Prestamo(0,"Married",0,0,2,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "A")

    def test_2(self):
        prestamo= Prestamo(0,"Single",0,0,2,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "D")

    def test_3(self):
        prestamo= Prestamo(1,"Divorced",0,0,2,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "A")

    def test_4(self):
        prestamo= Prestamo(0,"Divorced",0,0,2,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "M")

    def test_5(self):
        prestamo= Prestamo(0,"",75,0,1,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "M")

    def test_6(self):
        prestamo= Prestamo(0,"",74,1,1,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "D")

    def test_7(self):
        prestamo= Prestamo(0,"",74,2,1,0)
        programa = Programa()
        msg = programa.AprobarPrestamo(prestamo1)
        self.assertEquals(msg, "A")


if __name__ == '__main__':
    unittest.main()
