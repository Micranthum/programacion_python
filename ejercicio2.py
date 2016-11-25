n=int(input("Introduce saldo inicial con dos digitos despues del punto decimal: "))
print("Ha escrito", n)
for x in range(0,n):
	x=n*.04
print x, "es tu interes"
saldo1=n+x
print saldo1,"es tu saldo en el primer anho"
saldo2=saldo1+(saldo1*0.04)
print saldo2,"es tu saldo en el segundo anho"
saldo3=saldo2+(saldo2*0.04)
print saldo3,"es tu saldo en el tercer anho"
