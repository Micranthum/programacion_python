print "Si desea conocer la hipotenusa de un triangulo introduzca los siguientes datos:"
a=int(input("Ingresa el cateto a del triangulo: "))
b=int(input("Ingresa el cateto b del triangulo: "))
import math as m
def f(a,b):
	c=m.sqrt((a**2)+(b**2))
	print "la hipotenusa mide:",c,"unidades."
s=f(a,b)

