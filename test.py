# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):

        #dependientes, estado, capacidaddeuda, tiempovivienda, tiempotrabajo, edad
        result_val = funcionalidad.aprobarPrestamo(1, "soltero", 20, 3, 1, 17)
        expected_val = "D"
        self.assertEquals(result_val, expected_val)

    def test_prueba_2(self):

        #dependientes, estado, capacidaddeuda, tiempovivienda, tiempotrabajo, edad
        result_val = funcionalidad.aprobarPrestamo(1, "soltero", 20, 1, 1, 18)
        expected_val = "D"
        self.assertEquals(result_val, expected_val)


            
if __name__ == '__main__':
    unittest.main()