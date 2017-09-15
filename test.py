# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):

# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba

    def test_prueba_1(self):
        anios_trab = 1
        cap_end = 0.40
        anios_viv = 1
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, cap_end, anios_viv, 'soltero', 1)
        self.assertEqual(prestamo, 'D')

    def test_prueba_2(self):
        anios_trab = 1
        cap_end = 0.40
        anios_viv = 3
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, cap_end, anios_viv, 'soltero', 1)
        self.assertEqual(prestamo, 'A')

    '''
    def test_prueba_3(self):
        anios_trab = 1
        cap_end = 0.80
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, cap_end, 1, 'soltero', 1)
        self.assertEqual(prestamo, 'M')

    def test_prueba_4(self):
        anios_trab = 3
        estado_civil = 'casado'
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, 0.5, 1, estado_civil, 1)
        self.assertEqual(prestamo, 'A')

    def test_prueba_5(self):
        anios_trab = 3
        estado_civil = 'soltero'
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, 0.5, 1, estado_civil, 1)
        self.assertEqual(prestamo, 'D')


    def test_prueba_6(self):
        anios_trab = 3
        estado_civil = 'divorciado'
        dep = 0
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, 0.5, 1, estado_civil, dep)
        self.assertEqual(prestamo, 'M')


    def test_prueba_7(self):
        anios_trab = 3
        estado_civil = 'divorciado'
        dep = 2
        prestamo = funcionalidad.aprobar_prestamo(anios_trab, 0.5, 1, estado_civil, dep)
        self.assertEqual(prestamo, 'A')
    '''

if __name__ == '__main__':
    unittest.main()
