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

    def test_prueba_2(self):
        años_trab = 1
        cap_end = 0.40
        años_viv = 3
        prestamo = funcionalidad.aprobar_prestamo(años_trab, cap_end, años_viv, 'soltero', 1)
        self.assertEquals(prestamo, 'A')

    def test_prueba_3(self):
        años_trab = 1
        cap_end = 0.80
        prestamo = funcionalidad.aprobar_prestamo(años_trab, cap_end, 1, 'soltero', 1)
        self.assertEquals(prestamo, 'M')

    def test_prueba_4(self):
        años_trab = 3
        estado_civil = 'casado'
        prestamo = funcionalidad.aprobar_prestamo(años_trab, 0.5, 1, estado_civil, 1)
        self.assertEquals(prestamo, 'A')

    def test_prueba_5(self):
        años_trab = 3
        estado_civil = 'soltero'
        prestamo = funcionalidad.aprobar_prestamo(años_trab, 0.5, 1, estado_civil, 1)
        self.assertEquals(prestamo, 'D')


    def test_prueba_6(self):
        años_trab = 3
        estado_civil = 'divorciado'
        dep = 0
        prestamo = funcionalidad.aprobar_prestamo(años_trab, 0.5, 1, estado_civil, dep)
        self.assertEquals(prestamo, 'M')


    def test_prueba_7(self):
        años_trab = 3
        estado_civil = 'divorciado'
        dep = 2
        prestamo = funcionalidad.aprobar_prestamo(años_trab, 0.5, 1, estado_civil, dep)
        self.assertEquals(prestamo, 'A')


if __name__ == '__main__':
    unittest.main()
