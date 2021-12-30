import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#x, y= np.loadtxt(r'C:\Users\franc\Desktop\datiL\DatiL3\....txt', unpack = True)

N=50
xc, yc, r1 = 5, -2, 10
ex, ey= 0.5, 0.5
dy = np.array(N*[ey])
dx = np.array(N*[ex])
dr = np.sqrt(dx**2 + dy**2)

phi = 2*np.pi*np.random.uniform(0, 1, N)
x = xc + r1*np.cos(phi)
y = yc + r1*np.sin(phi)
k = np.random.uniform(0, ex, N)
l = np.random.uniform(0, ey, N)
x = x + k #aggiungo errore
y = y + l

a=np.array([x, y])

def fitcerchio(pt):
    '''
    fit di un cerchio con metodo di coope
    Parameters
    ----------
    pt : 2Darray
        contiene le coordinate del cerchio

    Returns
    -----------
    c : 1Darray
        array con le coordinate del centro del cerchio
    r : float
        raggio del cerchio
    d : 1Darray
        array con gli errori associati a c ed r
    A1 : 2Darray
        matrice di covarianza
    '''
    npt = len(pt[0])
    S = np.column_stack((pt.T, np.ones(npt)))
    y = (pt**2).sum(axis=0)

    A = S.T @ S #@ è il prodotto matriciale
    b = S.T @ y
    sol = np.linalg.solve(A, b)

    c = 0.5*sol[:-1]
    r = np.sqrt(sol[-1] + c.T @ c)

    d = np.zeros(3)
    A1 = np.linalg.inv(A)

    for i in range(3):
        d[i] = np.sqrt(A1[i,i])
    return c, r, d, A1

c, r, d , A= fitcerchio(a)

print('x_c = %.5f +- %.5f ' % (c[0], d[0]))
print('y_c = %.5f +- %.5f ' % (c[1], d[1]))
print('r   = %.5f +- %.5f ' % (r,    d[2]))

chisq = sum(((np.sqrt((x-c[0])**2 + (y-c[1])**2) - r)/dr)**2.)
ndof = N - 3
print(f'chi quadro = {chisq:.3f} ({ndof:d} dof)')

corr=np.zeros((3,3))
for i in range(0, 3):
    for j in range(0, 3):
       corr[i][j]=(A[i][j])/(np.sqrt(A.diagonal()[i])*np.sqrt(A.diagonal()[j]))
print(corr)

fig1 = plt.figure(1, figsize=(7.5,9.3))
frame1=fig1.add_axes((.1,.35,.8,.6))
#frame1=fig1.add_axes((trasla lateralmente, trasla verticamente, larghezza, altezza))
frame1.set_title('Fit dati simulati',fontsize=20)
plt.ylabel('y [a.u]',fontsize=10)
plt.grid()

tt=np.linspace(0, 2*np.pi, 10000)
plt.errorbar(x, y, dy, dx, fmt='.', color='black', label='dati')
xx = c[0] + r*np.cos(tt)
yy = c[1] + r*np.sin(tt)
plt.plot(xx, yy, color='blue', alpha=0.5, label='best fit')
plt.legend(loc='best')


frame2=fig1.add_axes((.1,.1,.8,.2))
frame2.set_ylabel('Residui Normalizzati')
plt.xlabel('x [a.u.]',fontsize=10)

ff=(np.sqrt((x-c[0])**2 + (y-c[1])**2) - r)/dr
x1=np.linspace(np.min(x),np.max(x), 1000)
plt.plot(x1, 0*x1, color='red', linestyle='--', alpha=0.5)
plt.plot(x, ff, '.', color='black')
plt.grid()

plt.show()
