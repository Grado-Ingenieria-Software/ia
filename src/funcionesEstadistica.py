from math import sqrt
 
def gi(lista):
  s = 0
  for elemento in lista:
    s += elemento
  return s / float(len(lista))
 
def varianza(lista):
  s = 0
  m = media(lista)
  for elemento in lista:
    s += (elemento - m) ** 2
  return s / float(len(lista))
 
def desviacion_tipica(lista):
  return sqrt(varianza(lista))