# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def AprobarPrestamo(NumDependientes,EstadoCivil,CapacidadDeEndudamiento,AniosViviendaActual,AniosTrabajo, edad):
	if(edad>=18):
		if (AniosTrabajo >= 2):
			if (EstadoCivil=="Married"):
				prestamo="Aprobado"
			elif(EstadoCivil=="Single"):
				prestamo="Denegado"
			elif(EstadoCivil=="Divorced"):
				if(NumDependientes==0):
					prestamo="Manual"
				elif(NumDependientes>0):
					prestamo="Aprobado"
		elif(AniosTrabajo < 2):
			if (CapacidadDeEndudamiento>75):
				prestamo="Manual"
			elif(CapacidadDeEndudamiento<75):
				if(AniosViviendaActual >=1.5):
					prestamo="Aprobado"
				elif(AniosViviendaActual < 1.5):
					prestamo="Denegado"
	else:
		prestamo="Denegado"
	return prestamo 