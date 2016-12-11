print "Este programa le ayudara a encontrar la distancia (km) entre dos puntos del planeta, dados por su latitud y longitud, por favor ingrese:"
import math as m
a=int(input("Latitud del punto inicial: "))
b=int(input("Longitud del punto inicial: "))
c=int(input("Latitud del punto final: "))
d=int(input("Longitud del punto final: "))
def f(a,b,c,d):
    t1=(a*m.pi/180)
    g1=(b*m.pi/180)
    t2=(c*m.pi/180)
    g2=(d*m.pi/180)
    x=m.sin(t1)*m.sin(t2)+m.cos(t1)*m.cos(t2)*m.cos(g1-g2)
    y=6371.01*m.acos(x)
    print "La distancia entre los dos puntos es de",y,"kilometros."

s=f(a,b,c,d)
