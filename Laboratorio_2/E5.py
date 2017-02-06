import matplotlib.pyplot as plt
import numpy as np
d=input("Introduzca la magnitud del lado de una figura geometrica: ")
def juegodelcaos2(x):
    x=d
    y=np.linspace(0,x,100)
    fig=[]
    for i in y:
        fig.append(i**i+i**i)
    plt.plot(y,fig)
    plt.show()
s=juegodelcaos2(d)