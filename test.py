# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    #def aprobarPrestamo(self, endeudamiento, estadocivil, aniosvivienda, aniostrabajo, dependientes):

    def test_prueba_1(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'SOLTERO', 1.0, 1, 0)
        self.assertEqual(tipo, 'D')

    def test_prueba_2(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'SOLTERO', 2.0, 1, 0)
        self.assertEqual(tipo, 'A')

    def test_prueba_3(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(80, 'SOLTERO', 2.0, 1, 0)
        self.assertEqual(tipo, 'M')

    def test_prueba_4(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'CASADO', 1.0, 5, 0)
        self.assertEqual(tipo, 'A')

    def test_prueba_5(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'SOLTERO', 1.0, 5, 0)
        self.assertEqual(tipo, 'D')

    def test_prueba_6(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'DIVORCIADO', 1.0, 5, 2)
        self.assertEqual(tipo, 'A')

    def test_prueba_7(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'DIVORCIADO', 1.0, 5, 0)
        self.assertEqual(tipo, 'M')

    def test_prueba_8(self):
        tipo = funcionalidad.Banco().aprobarPrestamo(50, 'VIUDO', 1.0, 5, 0)
        self.assertEqual(tipo, 'D')
            
if __name__ == '__main__':
    unittest.main()
