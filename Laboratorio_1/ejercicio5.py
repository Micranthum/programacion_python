a=int(input("Escribe la cantidad de segundos que quieras convertir a dias horas, minutos y segundos" ))
print "ha escrito",a,"segundos"
def funcion(a):
    d=a/(86400)
    d1=a/float(86400)
    r=abs(d1)-abs(int(d1))
    h=r*10**6/3600
    r1=abs(r/float(3600))-abs(int(r/float(3600)))
    m=r1*10**6/60
    s=abs(m/float(60))-abs(int(m/float(60)))
    print "El equivalente es:",d,"dias",h,"horas",m,"minutos",s,"segundos"
sal=funcion(a)