# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(numDependientes, estadoCivil, capEndeudamiento, aVivienda, aTrabajo):
	resp = "D"
	if aTrabajo>=2:
		if estadoCivil == "Divorced":
			if numDependientes>0:
				resp = "A"
			elif numDependientes == 0:
				resp = "M"
		elif estadoCivil == "Single":
			resp = "D"
		elif estadoCivil == "Married":
			resp = "A"
	else:
		if capEndeudamiento < 0.75:
			if aVivienda <1.5:
				resp = "D"
			else:
				resp = "A"
		else:
			resp = "M"
	return resp
	