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
            
if __name__ == '__main__':
    unittest.main()