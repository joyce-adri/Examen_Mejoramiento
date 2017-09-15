# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        años_de_trabajo = 3
        estado_civil = "divorciado"
        num_dependientes = 1
        capacidad_endeudamiento = 0.75
        años_vivienda = 2
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("A", res)

    def test_prueba_2(self):
        años_de_trabajo = 3
        estado_civil = "divorciado"
        num_dependientes = 0
        capacidad_endeudamiento = 0.75
        años_vivienda = 2
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("M", res)

    def test_prueba_3(self):
        años_de_trabajo = 3
        estado_civil = "soltero"
        num_dependientes = 1
        capacidad_endeudamiento = 0.75
        años_vivienda = 2
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("D", res)

    def test_prueba_4(self):
        años_de_trabajo = 3
        estado_civil = "casado"
        num_dependientes = 1
        capacidad_endeudamiento = 0.75
        años_vivienda = 2
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("A", res)

    def test_prueba_5(self):
        años_de_trabajo = 1
        estado_civil = "divorciado"
        num_dependientes = 1
        capacidad_endeudamiento = 0.8
        años_vivienda = 1
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("M", res)

    def test_prueba_6(self):
        años_de_trabajo = 1
        estado_civil = "divorciado"
        num_dependientes = 1
        capacidad_endeudamiento = 0.55
        años_vivienda = 1
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("D", res)

    def test_prueba_7(self):
        años_de_trabajo = 1
        estado_civil = "divorciado"
        num_dependientes = 1
        capacidad_endeudamiento = 0.55
        años_vivienda = 2
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("A", res)

    def test_prueba_8(self):
        años_de_trabajo = 3
        estado_civil = "otros"
        num_dependientes = 1
        capacidad_endeudamiento = 0.55
        años_vivienda = 1
        res = funcionalidad.AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda)
        self.assertEquals("D", res)

            
if __name__ == '__main__':
    unittest.main()