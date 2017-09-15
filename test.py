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

            
if __name__ == '__main__':
    unittest.main()