
print "Este programa ordena tres digitos de menor a mayor de un numero de tres cifras que debe ser ingresado"
x=input("Introduzca un numero entero de 3 digitos: ")
def f(x):
	b=str(x)
	if b[0]<=b[1]<=b[2]:
		c=b[0],b[1],b[2]
		print c
	elif b[1]<=b[0]<=b[2]:
		d=b[1],b[0],b[2]
		print d
	elif b[2]<=b[1]<=b[0]:
		e=b[2],b[1],b[0]
		print e
	elif b[2]<b[0]<b[1]:
		g=b[2],b[0],b[1]
		print g
	elif b[0]<=b[2]<=b[1]:
		h=b[0],b[2],b[1]
		print h
	elif b[1]<=b[2]<=b[0]:
		i=b[1],b[2],b[0]
		print i
s=f(x)