# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba


    def test_prueba_1(self):
        años_trab = 1
        cap_end = 0.40
        años_viv = 1
        prestamo = funcionalidad.aprobar_prestamo(años_trab, cap_end, años_viv, 'soltero', 1)
        self.assertEquals(prestamo, 'D')
    '''
    def test_prueba_2(self):
        años_trab = 1
        cap_end = 0.40
        años_viv = 3
        prestamo = funcionalidad.aprobar_prestamo(años_trab, cap_end, años_viv, 'soltero', 1)
        print ('funcion--> ', prestamo)
        self.assertEquals(prestamo, 'A')


    def test_prueba_3(self):
        años_trab = 1
        cap_end = 0.80
        prestamo = funcionalidad.aprobar_prestamo(años_trab, cap_end, 1, 'soltero', 1)
        self.assertEquals(prestamo, 'M')

    def test_prueba_4(self):

        self.assertEquals(prestamo, 'D')

    def test_prueba_5(self):

        self.assertEquals(prestamo, 'D')

    def test_prueba_6(self):

        self.assertEquals(prestamo, 'D')

    def test_prueba_7(self):
        self.assertEquals(prestamo, 'D')
    '''

if __name__ == '__main__':
    unittest.main()
