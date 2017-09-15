# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        msg = funcionalidad.aprobarPrestamo(3, 'divorced', 0, 0, 1)
        self.assertEquals(msg, "Calificacion: A")

    def test_prueba_2(self):
        msg = funcionalidad.aprobarPrestamo(3, 'divorced', 0, 0, 0)
        self.assertEquals(msg, "Calificacion: M")

    def test_prueba_3(self):
        msg = funcionalidad.aprobarPrestamo(3, 'single', 0, 0, 0)
        self.assertEquals(msg, "Calificacion: D")

    def test_prueba_4(self):
        msg = funcionalidad.aprobarPrestamo(3, 'Married', 0, 0, 0)
        self.assertEquals(msg, "Calificacion: A")
if __name__ == '__main__':
    unittest.main()