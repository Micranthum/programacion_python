print "Este programa calculara su Indice de Masa Corporal, por favor escriba los datos que se le piden:"
p=int(input("Introduzca su peso en kg: "))
e=int(input("introduzca su estatura en cm: "))
print "Usted ha escrito que su peso es de:",p,"kg y su estatura es de:",e,"cm."

def f(p,e):
	eM=e/float(100)
	IMC=p/(float(eM))**2
	if IMC<16:
		print "Su indice de masa corporal es de:",IMC,"usted padece de delgadez severa."
	elif IMC<16.99 and IMC>16.00:
		print "Su indice de masa corporal es de:",IMC,"usted padece de delgadez moderada."
	elif IMC<18.49 and IMC>17.00:
	 	print "Su indice de masa corporal es de:",IMC,"usted padece de delgadez leve."
	elif IMC<24.99 and IMC>18.5:
		print "Su indice de masa corporal es de:",IMC,"se le considera normal."
	elif IMC>=25 and IMC<30:
		print "Su indice de masa corporal es de:",IMC,"usted padece de sobrepeso, salga a correr."
	elif IMC>=30 and IMC<40:
		print "Su indice de masa corporal es de:",IMC,"usted padece de obesidad, ya no coma tanto."
	else:
		print "Su indice de masa corporal es de:",IMC,"usted padece de obesidad morbida, por favor cuidese mas y vaya al doctor."
sal=f(p,e)	
		