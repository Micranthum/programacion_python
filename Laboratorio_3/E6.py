#!/usrbin/env python
# _*_ coding: utf-8 _*_
print "Este programa le muestra la equivalencia de años de un perro con la edad de usted"
x=input("Introduzca su edad: ")
def f(x):
	
    if 0<x<2:
        print "Si usted fuera un perro tendria",x*10.5,"años."
    else:
        print "Si usted fuera un perro tendria",x*4,"años."
s=f(x)