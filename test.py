# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        aniosTrabajo = 3
        capacidadEndeudamiento = 0
        aniosVivienda = 0
        estadoCivil = "divorciado"
        numDependientes = 1
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "A"
        self.assertEquals(esperado, prestamo)

    def test_prueba_2(self):
        aniosTrabajo = 3
        capacidadEndeudamiento = 0
        aniosVivienda = 0
        estadoCivil = "divorciado"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "M"
        self.assertEquals(esperado, prestamo)

    def test_prueba_3(self):
        aniosTrabajo = 3
        capacidadEndeudamiento = 0
        aniosVivienda = 0
        estadoCivil = "soltero"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "D"
        self.assertEquals(esperado, prestamo)

    def test_prueba_4(self):
        aniosTrabajo = 3
        capacidadEndeudamiento = 0
        aniosVivienda = 0
        estadoCivil = "casado"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "A"
        self.assertEquals(esperado, prestamo)

    def test_prueba_5(self):
        aniosTrabajo = 1
        capacidadEndeudamiento = 80
        aniosVivienda = 0
        estadoCivil = "casado"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "M"
        self.assertEquals(esperado, prestamo)

    def test_prueba_6(self):
        aniosTrabajo = 1
        capacidadEndeudamiento = 60
        aniosVivienda = 2
        estadoCivil = "casado"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "A"
        self.assertEquals(esperado, prestamo)

    def test_prueba_7(self):
        aniosTrabajo = 1
        capacidadEndeudamiento = 60
        aniosVivienda = 1
        estadoCivil = "casado"
        numDependientes = 0
        prestamo = funcionalidad.AprobarPrestamo(aniosTrabajo, capacidadEndeudamiento, aniosVivienda, estadoCivil, numDependientes)
        esperado = "D"
        self.assertEquals(esperado, prestamo)



if __name__ == '__main__':
    unittest.main()