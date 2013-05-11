#!/usr/bin/python
import math
from time import time


a=1
b=6

integral=float((b-a)*(1/(1+math.e**a)+1/(1+math.e**b))/2)

n=float(raw_input('Introduce el numero minimo de particiones ')) # Float por problema de decimales
m=float(raw_input('Introduce el numero maximo de particiones ')) # Idem
intervalos=float(raw_input('Introduce el intervalo de las particiones ')) # Idem



while n<=m:
   h=float((b-a)/n)
   i=1.0
   sumatorio=0
   while i<=n:
      sumatorio+=float(2*(1/(1+(math.e)**(a+i*h)))) #sumatorio de la regla del trapecio por partes
      i+=1

   sumatorio=(h/2*(1/(1+math.e**a)+sumatorio+(1/(1+math.e**b))))  #regla del trapecio por partes

   print 'Particion:', int(n), 'Resultado:', sumatorio
   n+=intervalos   
