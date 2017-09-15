# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from funcionalidad import *
class Test(unittest.TestCase):
	def test_prueba_1(self):
		msg=AprobarPrestamo(0,"Married",0,0,4,19)
		self.assertEquals(msg,"Aprobado")
	def test_prueba_2(self):
		msg=AprobarPrestamo(0,"Single",0,0,4,19)
		self.assertEquals(msg,"Denegado")
	def test_prueba_3(self):
		msg=AprobarPrestamo(0,"Divorced",0,0,4,19)
		self.assertEquals(msg,"Manual")
	def test_prueba_4(self):
		msg=AprobarPrestamo(5,"Divorced",0,0,4,19)
		self.assertEquals(msg,"Aprobado")
	def test_prueba_5(self):
		msg=AprobarPrestamo(0,"Divorced",80,0,1,19)
		self.assertEquals(msg,"Manual")
	def test_prueba_6(self):
		msg=AprobarPrestamo(0,"Divorced",60,1,1,19)
		self.assertEquals(msg,"Denegado")
	def test_prueba_7(self):
		msg=AprobarPrestamo(0,"Divorced",60,2,1,19)
		self.assertEquals(msg,"Aprobado")
	def test_prueba_8(self):
		msg=AprobarPrestamo(0,"Divorced",60,2,1,15)
		self.assertEquals(msg,"Denegado")
	
if __name__ == '__main__':
    unittest.main()
   