# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        yearsTrabajo = 5
        estCivil = "Single"
        dep = 0
        end = 75
        yearsVivienda = 4

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "D"
        self.assertEquals(resultado, esperado)

    def test_prueba_2(self):
        yearsTrabajo = 5
        estCivil = "Married"
        dep = 0
        end = 60
        yearsVivienda = 6

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "A"
        self.assertEquals(resultado, esperado)

    def test_prueba_3(self):
        yearsTrabajo = 6
        estCivil = "Divorced"
        dep = 0
        end = 10
        yearsVivienda = 10

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "M"
        self.assertEquals(resultado, esperado)

    def test_prueba_4(self):
        yearsTrabajo = 6
        estCivil = "Divorced"
        dep = 3
        end = 15
        yearsVivienda = 5

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "A"
        self.assertEquals(resultado, esperado)

    def test_prueba_5(self):
        yearsTrabajo = 1
        estCivil = "Married"
        dep = 1
        end = 75
        yearsVivienda = 1

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "M"
        self.assertEquals(resultado, esperado)

    def test_prueba_6(self):
        yearsTrabajo = 1
        estCivil = "Single"
        dep = 2
        end = 60
        yearsVivienda = 3

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "A"
        self.assertEquals(resultado, esperado)

    def test_prueba_7(self):
        yearsTrabajo = 1
        estCivil = "Divorced"
        dep = 0
        end = 50
        yearsVivienda = 1

        resultado = funcionalidad.aprobar_prestamo(yearsTrabajo, end, estCivil, dep, yearsVivienda)
        esperado = "D"
        self.assertEquals(resultado, esperado)

            
if __name__ == '__main__':
    unittest.main()