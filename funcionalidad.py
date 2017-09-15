# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#Divorceado=1 , Soltero =2, casado=3  


probar_Prestamo(aniosTrabajo,capacidadEndeudamiento,aniosViviendaActual,estadoCivil,dependientes):
    estado = "D"  #denegado
    if aniosTrabajo<2:
       if capacidadEndeudamiento <75:
          if aniosViviendaActual<1.5:
             estado="D"
          elif aniosViviendaActual>=1.5:
               estado="A"
       elif capacidadEndeudamiento>=75:
            estado="M"
    elif aniosTrabajo>=2:
         if estadoCivil==1:
            if dependientes >0:
               estado="A"
            elif dependientes==0:
                 estado="M"
         elif estadoCivil==2:
              estado="D"
         elif estadoCivil==3: 
              estado="A"
       
    return "Estado del prestamo:%s" % (estado)
