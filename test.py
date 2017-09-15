# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from funcionalidad import *
class Test(unittest.TestCase):
	def test_prueba_1(self):
		msg=AprobarPrestamo(0,"Single",0,0,4)
		self.assertEquals(msg,"Denegado")
	
if __name__ == '__main__':
    unittest.main()