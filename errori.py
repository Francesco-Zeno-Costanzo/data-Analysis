import numpy as np
import sympy as sp
'''
Il codice è povero di commenti perché è abbastanza autoesplicativo, si precisa però che:
I) sp.Symbol  difinisce i simboli da utilizzare;
II) sp.diff fa la derivata di una funzione (primo argomento) rispetto ad una variabile (secondo argomento);
III) .subs sostituisce al simbolo (primo argomento) il valore numerico (secondo argomento).
'''
##somma

def summa(x, dx, y, dy):
    f=x+y
    df=np.sqrt(dx**2+dy**2)
    return f, df

##sottrazione
def diff(x, dx, y, dy):
    f=x-y
    df=np.sqrt(dx**2+dy**2)
    return f, df

##prodotto

def prod(x, dx, y, dy):
    f=x*y
    df=np.sqrt((dx/x)**2+(dy/y)**2)*f
    return f, df

##divisione

def rapp(x, dx, y, dy):
    f=x/y
    df=np.sqrt((dx/x)**2+(dy/y)**2)*f
    return f, df

##parallelo
x = sp.Symbol('x')
y = sp.Symbol('y')

def par(x1, dx1, y1, dy1):
    f1=((1/x)+(1/y))**(-1)
    f=f1.subs(x,x1).subs(y,y1)

    a=sp.diff(f1, x).subs(x,x1).subs(y,y1)
    b=sp.diff(f1, y).subs(x,x1).subs(y,y1)
    df1=((a*dx1)**2 + (b*dy1)**2)
    df=np.sqrt(float(df1))
    return f, df

##boh ma capita spesso
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
t = sp.Symbol('t')

def B(x1, dx1, y1, dy1, z1, dz1, t1, dt1):
    f1=((x-y)/(z+t))
    f=f1.subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    a=sp.diff(f1, x).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    b=sp.diff(f1, y).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    c=sp.diff(f1, z).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    d=sp.diff(f1, t).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    df1=((a*dx1)**2 + (b*dy1)**2+ (c*dz1)**2 + (d*dt1)**2 )
    df=np.sqrt(float(df1))
    return f, df


## f di taglio dal fit
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
t = sp.Symbol('t')

def H(x1, dx1, y1, dy1, z1, dz1, t1, dt1):

    f1=10**(((x-y)/(z-t))/20)
    f=f1.subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    a=sp.diff(f1, x).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    b=sp.diff(f1, y).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    c=sp.diff(f1, z).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    d=sp.diff(f1, t).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    df1=((a*dx1)**2 + (b*dy1)**2+ (c*dz1)**2 + (d*dt1)**2 )
    df=np.sqrt(float(df1))
    return f, df

##
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')
t = sp.Symbol('t')

def G(x1, dx1, y1, dy1, z1, dz1, t1, dt1):

    f1=(x*y)*sp.log((1+(4.1/3.5)*(t/(t+z)))/(1-(t/(t+z))))
    f=f1.subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    a=sp.diff(f1, x).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    b=sp.diff(f1, y).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    c=sp.diff(f1, z).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)
    d=sp.diff(f1, t).subs(x,x1).subs(y,y1).subs(z,z1).subs(t,t1)

    df1=((a*dx1)**2 + (b*dy1)**2+ (c*dz1)**2 + (d*dt1)**2 )
    df=np.sqrt(float(df1))
    return f, df