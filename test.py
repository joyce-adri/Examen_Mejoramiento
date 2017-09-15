# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
	def test_prueba_1(self):
        aniosTrabajo = 3
        cEndeudamiento = 75
        aniosVivienda = 1.5
        dependientes = 0
        estadoC = "soltero"
        resp = funcionalidad.aprobarPrestamo(aniosTrabajo, cEndeudamiento, aniosVivienda, dependientes, estadoC)
        self.assertEquals("D", resp)

    def test_prueba_2(self):
        aniosTrabajo = 3
        cEndeudamiento = 75
        aniosVivienda = 1.5
        dependientes = 0
        estadoC = "casado"
        resp = funcionalidad.aprobarPrestamo(aniosTrabajo, cEndeudamiento, aniosVivienda, dependientes, estadoC)
        self.assertEquals("A", resp)

    def test_prueba_3(self):
        aniosTrabajo = 3
        cEndeudamiento = 75
        aniosVivienda = 1.5
        dependientes = 0
        estadoC = "divorciado"
        resp = funcionalidad.aprobarPrestamo(aniosTrabajo, cEndeudamiento, aniosVivienda, dependientes, estadoC)
        self.assertEquals("M", resp)


    def test_prueba_4(self):
        aniosTrabajo = 3
        cEndeudamiento = 75
        aniosVivienda = 1.5
        dependientes = 3
        estadoC = "divorciado"
        resp = funcionalidad.aprobarPrestamo(aniosTrabajo, cEndeudamiento, aniosVivienda, dependientes, estadoC)
        self.assertEquals("A", resp)


            
if __name__ == '__main__':
    unittest.main()