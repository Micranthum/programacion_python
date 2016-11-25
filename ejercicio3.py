import math 
r=int(input("Introduce el radio de un circulo: "))
print("Ha escrito", r)
for area in range(0,r):
	area=math.pow(r,2)*math.pi
print area, "es la area del circulo"
