# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_1(self):
        msg = funcionalidad.aprobarPrestamo(2,"casado",0,0,0)
        print msg
        self.assertEquals(msg,"A")

    def test_2(self):
        msg = funcionalidad.aprobarPrestamo(2, "soltero", 0, 0, 0)
        print msg
        self.assertEquals(msg, "D")

    def test_3(self):
        msg = funcionalidad.aprobarPrestamo(2, "divorciado", 1, 0, 0)
        print msg
        self.assertEquals(msg, "A")

    def test_4(self):
        msg = funcionalidad.aprobarPrestamo(2, "divorciado", 0, 0, 0)
        print msg
        self.assertEquals(msg, "M")

    def test_5(self):
        msg = funcionalidad.aprobarPrestamo(1, "soltero", 0, 75, 0)
        print msg
        self.assertEquals(msg, "M")

    def test_6(self):
        msg = funcionalidad.aprobarPrestamo(1, "soltero", 0, 74, 1.5)
        print msg
        self.assertEquals(msg, "A")

    def test_7(self):
        msg = funcionalidad.aprobarPrestamo(2, "soltero", 0, 74, 1)
        print msg
        self.assertEquals(msg, "D")



if __name__ == '__main__':
    unittest.main()