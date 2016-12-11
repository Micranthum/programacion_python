print "Este programa te da las coordenadas de un poligono regular con el numero de lados que usted elija"
a=int(input(" Por favor ingrese el numero de lados de su poligono regular: "))
lista=[]
for i in range(a):
    x1=[0,i]
    y1=[i,0]
    lista.append(x1+y1)
print lista
