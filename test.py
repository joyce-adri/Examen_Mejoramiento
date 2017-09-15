# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
	def test_prueba_1(self):
		p = funcionalidad.AprobarPrestamo(1, "Divorced", 0.75, 1, 2)
		self.assertEquals(p, "A")

	def test_prueba_2(self):
		p = funcionalidad.AprobarPrestamo(0, "Divorced", 0.75, 1, 2)
		self.assertEquals(p, "M")

	def test_prueba_3(self):
		p = funcionalidad.AprobarPrestamo(1, "Single", 0.75, 1, 2)
		self.assertEquals(p, "D")

	def test_prueba_4(self):
		p = funcionalidad.AprobarPrestamo(1, "Married", 0.75, 1, 2)
		self.assertEquals(p, "A")

	def test_prueba_5(self):
		p = funcionalidad.AprobarPrestamo(1, "Divorced", 0.5, 1, 1)
		self.assertEquals(p, "D")

            
if __name__ == '__main__':
    unittest.main()