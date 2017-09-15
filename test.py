# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from funcionalidad import *


class Test(unittest.TestCase):
    
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
    
    def test_prueba_1(self):
        anio_trabajo = 3
        estado = "Married"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 2
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("A", solicitante.AprobarPrestamo())

    def test_prueba_2(self):
        anio_trabajo = 3
        estado = "Single"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 2
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("D", solicitante.AprobarPrestamo())

    def test_prueba_3(self):
        anio_trabajo = 3
        estado = "Single"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 2
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("A", solicitante.AprobarPrestamo())

    def test_prueba_4(self):
        anio_trabajo = 1
        estado = "Single"
        dependientes = 2
        capacidad_endeudamiento = 80
        anio_vivienda = 2
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("M", solicitante.AprobarPrestamo())

    def test_prueba_5(self):
        anio_trabajo = 3
        estado = "Married"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 2
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("M", solicitante.AprobarPrestamo())

    def test_prueba_6(self):
        anio_trabajo = 3
        estado = "Married"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 1.5
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("A", solicitante.AprobarPrestamo())

    def test_prueba_7(self):
        anio_trabajo = 3
        estado = "Married"
        dependientes = 2
        capacidad_endeudamiento = 2
        anio_vivienda = 1
        edad = 40
        email = "solicitante@mail.com"
        solicitante = Solicitante(dependientes, estado, capacidad_endeudamiento, anio_vivienda, anio_trabajo, edad,email)

        self.assertEquals("D", solicitante.AprobarPrestamo())

if __name__ == '__main__':
    unittest.main()