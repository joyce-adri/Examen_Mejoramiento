# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
   def test1(self):
        estado = funcionalidad.Aprobar_Prestamo(1,70,1.0,1,3)
        esperado = "Estado del prestamo:D"
        self.assertEquals(estado, esperado)
           
    def test2(self):
        estado = funcionalidad.Aprobar_Prestamo(1,70,1.0,1,3)
        esperado = "Estado del prestamo:D"
        self.assertEquals(estado, esperado)

    def test3(self):
        estado = funcionalidad.Aprobar_Prestamo(1,70,1.6,1,3)
        esperado = "Estado del prestamo:A"
        self.assertEquals(estado, esperado)
        
    def test3(self):
        estado = funcionalidad.Aprobar_Prestamo(1,76,1.0,1,3)
        esperado = "Estado del prestamo:M"
        self.assertEquals(estado, esperado)

    def test4(self):
        estado = funcionalidad.Aprobar_Prestamo(3,70,1.0,1,3)
        esperado = "Estado del prestamo:A"
        self.assertEquals(estado, esperado)

    def test5(self):
        estado = funcionalidad.Aprobar_Prestamo(3,70,1.0,1,0)
        esperado = "Estado del prestamo:M"
        self.assertEquals(estado, esperado)

    def test6(self):
        estado = funcionalidad.Aprobar_Prestamo(3,70,1.0,2,3)
        esperado = "Estado del prestamo:D"
        self.assertEquals(estado, esperado)

    def test7(self):
        estado = funcionalidad.Aprobar_Prestamo(3,70,1.0,3,3)
        esperado = "Estado del prestamo:A"
        self.assertEquals(estado, esperado)

if __name__ == '__main__':
    unittest.main()
