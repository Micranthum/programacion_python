print"Este programa le ayudara a conocer cuanto tendra que pagar al taxista por la distancia recorrida(km)"
print"La tarifa en CDMX de los taxis libres es de $8.74 el banderazo y $1.84 por cada 250 metros"
x=int(input("Ingrese la distancia recorrida en kilometros: "))
def f(x):
	
	p=8.74+(float(x/0.25)*1.84)
	print "Le tiene que pagar $",p,"al taxista."
s=f(x)

