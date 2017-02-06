a=raw_input("Introduce tu nombre: ")
def f(x):
    z,b,c=a[0],a[1:],'bfm'
    if b[0] in c:b=b[1:]
    d="X,X,bo-@\nBanana-fana fo-@\nFee-fi-mo-@\nX!".replace('X',z)
    for y in c:d=d.replace('@',y+b,1)
    print d
s=f(a)