# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def aprobarPrestamo(aniosTrabajo, estadoCivil, dependientes, capacidadEndeudamiento, aniosVivienda):
	resultado = "D"
	if aniosTrabajo >= 2:
		if estadoCivil == "divorciado":
			if dependientes > 0:
				resultado = "A"
			elif dependientes == 0:
				resultado = "M"
		elif estadoCivil == "soltero":
			resultado = "D"
		elif estadoCivil == "casado":
			resultado = "A"
	else:
		if capacidadEndeudamiento >= 75:
			resultado = "M"
		else:
			if aniosVivienda >= 1.5:
				resultado = "A"
			else:
				resultado = "D"
	return resultado