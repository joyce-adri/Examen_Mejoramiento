# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad
from funcionalidad import prestamos_hipotecarios

class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_funcionalidad_prueba1(self):
        # inserte su codigo de prueba

        msg = prestamos_hipotecarios(0, 3, "casado", 76, 1.5)
        self.assertEquals(msg, "aprobado")

    def test_funcionalidad_prueba2(self):
        # inserte su codigo de prueba

        msg = prestamos_hipotecarios(0, 3, "soltero", 76, 1.5)
        self.assertEquals(msg, "denegado")

    def test_funcionalidad_prueba3(self):
        # inserte su codigo de prueba

        msg = prestamos_hipotecarios(0, 3, "divorciado", 76, 1.5)
        self.assertEquals(msg, "manual")

    def test_funcionalidad_prueba4(self):
        # inserte su codigo de prueba

        msg = prestamos_hipotecarios(3, 3, "divorciado", 76, 1.5)
        self.assertEquals(msg, "aprobado")
if __name__ == '__main__':
    unittest.main()