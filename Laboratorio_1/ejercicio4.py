print"Este programa determinara los segundos que viajo, por favor introduzca:"
d=int(input("Cuantos dias viajo? "))
h=int(input("Cuantas horas viajo? "))
m=int(input("Cuantos minutos viajo? "))
s=int(input("Cuantos segundos viajo? "))

def funcion(d,h,m,s):
	#Las variables w,x,y son la equivalencias de d,h,m expresadas en segundos
    w=d*86400
    x=h*3600
    y=m*60
    seg=w+x+y+s

    print 'Usted viajo un total de',seg,'segundos'
s=funcion(d,h,m,s) 