print "Este programa le pide su nombre y le dice si la inicial es vocal o consonante"
x=raw_input("Introduzca su nombre: ")
def f(x):
    a=str(x)
    if a[0]=="A" or a[0]=="E" or a[0]=="I" or a[0]=="O" or a[0]=="U":
        print "La inicial de su nombre es vocal"
    else:
        print "La inicial de su nombre es consontante"
s=f(x)