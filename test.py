# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import funcionalidad

class Test(unittest.TestCase):
    def test_prueba_1(self):
        result = funcionalidad.aprobar_prestamo(3,80,1.5,"single",20)
        self.assertEqual(result,"denegado")
    def test_prueba_2(self):
        result = funcionalidad.aprobar_prestamo(3,80,1.5,"married",20)
        self.assertEqual(result,"aprobado")
    '''def test_prueba_3(self):
        result = funcionalidad.aprobar_prestamo(3,80,1.5,"divorced",1)
        self.assertEqual(result,"aprobado")
    def test_prueba_4(self):
        result = funcionalidad.aprobar_prestamo(3,80,1.5,"divorced",0)
        self.assertEqual(result,"manual")
    def test_prueba_5(self):
        result = funcionalidad.aprobar_prestamo(1,80,1.5,"divorced",0)
        self.assertEqual(result,"manual")
    def test_prueba_6(self):
        result = funcionalidad.aprobar_prestamo(1,74,1.5,"divorced",0)
        self.assertEqual(result,"aprobado")
    def test_prueba_7(self):
        result = funcionalidad.aprobar_prestamo(1,74,1.4,"divorced",0)
        self.assertEqual(result,"denegado")'''
if __name__ == '__main__':
    unittest.main()