# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(años_de_trabajo, estado_civil, num_dependientes, capacidad_endeudamiento, años_vivienda):
	res = "D"
	if(años_de_trabajo >= 2):
		if(estado_civil=="divorciado"):
			if(num_dependientes>0):
				res = "A"
			elif(num_dependientes==0):
				res = "M"
		elif(estado_civil=="soltero"):
			res="D"
		elif(estado_civil=="casado"):
			res="A"
	elif(años_de_trabajo<2):
		if(capacidad_endeudamiento>=0.75):
			res = "M"
		elif(capacidad_endeudamiento<0.75):
			if(años_vivienda<1.5):
				res="D"
			else:
				res="A"
	return res

