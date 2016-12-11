a=int(input("A continuacion introduzca un numero de cuatro digitos: "))
def f(a):
    b=str(a)
    s=int(b[0])+int(b[1])+int(b[2])+int(b[3])
    print "La suma de los digitos es:",s
s=f(a)