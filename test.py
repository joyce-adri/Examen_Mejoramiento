# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import funcionalidad


class Test(unittest.TestCase):
	
# >>>>>> Estructura para la codificacion de los casos de prueba <<<<<<
# Reemplazar EL ID por el numero correspondiente del caso de prueba
	
	def test_prueba_1(self):
		aniosTrabajo = 2
		estadoCivil = "soltero"
		dependientes = 0
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "D")

	def test_prueba_2(self):
		aniosTrabajo = 2
		estadoCivil = "casado"
		dependientes = 0
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "A")

	def test_prueba_3(self):
		aniosTrabajo = 2
		estadoCivil = "viudo"
		dependientes = 0
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "D")

	def test_prueba_4(self):
		aniosTrabajo = 2
		estadoCivil = "divorciado"
		dependientes = 1
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "A")

	def test_prueba_5(self):
		aniosTrabajo = 2
		estadoCivil = "divorciado"
		dependientes = 0
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "M")

	def test_prueba_6(self):
		aniosTrabajo = 2
		estadoCivil = "divorciado"
		dependientes = -1
		capacidadEndeudamiento = 0
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "D")

	def test_prueba_7(self):
		aniosTrabajo = 1
		estadoCivil = "divorciado"
		dependientes = 0
		capacidadEndeudamiento = 76
		aniosVivienda = 0
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "M")

	def test_prueba_8(self):
		aniosTrabajo = 1
		estadoCivil = "divorciado"
		dependientes = 0
		capacidadEndeudamiento = 74
		aniosVivienda = 1.5
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "A")

	def test_prueba_9(self):
		aniosTrabajo = 1
		estadoCivil = "divorciado"
		dependientes = 0
		capacidadEndeudamiento = 74
		aniosVivienda = 1
		resultado = funcionalidad.aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda)
		self.assertEqual(resultado, "D")
			
if __name__ == '__main__':
	unittest.main()