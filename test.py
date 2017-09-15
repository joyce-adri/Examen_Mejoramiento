# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_prueba_1(self):
        prestamo = funcionalidad.aprobar_prestamo(1, 0.40, 1, 'soltero', 1)
        self.assertEquals(prestamo, 'D')

if __name__ == '__main__':
    unittest.main()
