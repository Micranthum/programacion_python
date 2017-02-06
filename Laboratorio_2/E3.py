import matplotlib.pyplot as plt
d=input("Introduzca la magnitud del lado de un triangulo rectangulo: ")
def juegodelcaos(x):
    x=d
    t=[[0,0],[0,x],[x/2,x],[0,0]]
    plt.plot(t)
    plt.show()
s=juegodelcaos(d)