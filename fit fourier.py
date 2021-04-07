import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Importiamo i dati (va inserito il path assoluto per permettere di trovare) e definiamo la funzione di fit:
x, y= np.loadtxt(r'C:\Users\franc\Desktop\DatiL\datiL2\datilpf2\datiardu3.txt', unpack = True)

dy=np.array(len(y)*[1])
def f(x, a, c, f1, w_t):
    def ps(x, k,f,A, phi):
        return A*(2/(k*np.pi))*(np.sin((2*np.pi*f1*k*x+phi)))
    xx=np.linspace(np.min(x)-676, np.max(x), len(x))
    B=np.zeros(len(xx))
    for i in range (0,20000):
        k=2*i+1
        A=1/(np.sqrt(1+((2*np.pi*f1*k)/w_t)**2))
        phi=np.arctan(-(2*np.pi*f1*k)/w_t)
        B=B+ps(xx,k,f,A,phi)
    return a*B+c

#definiamo un array di parametri iniziali contenente i volori numerici che ci si aspetta il fit restituisca, per aiutare la convergenza dello stesso:
#init=np.array([a, c, f1, w_t])
init=np.array([800, 520, 0.0001, 0.000628318 ])

#Eseguiamo il fit e stampiamo i risultati:
pars, covm = curve_fit(f, x, y, init, sigma=dy, absolute_sigma=False)
print('a  = %.5f +- %.5f ' % (pars[0], np.sqrt(covm.diagonal()[0])))
print('c  = %.5f +- %.5f ' % (pars[1], np.sqrt(covm.diagonal()[1])))
print('f  = %.9f +- %.9f ' % (pars[2], np.sqrt(covm.diagonal()[2])))
print('w_t  = %.7f +- %.7f ' % (pars[3], np.sqrt(covm.diagonal()[3])))

#Calcoliamo il chi quadro,indice ,per quanto possibile, della bontà del fit:
chisq = sum(((y - f(x, *pars))/dy)**2.)
ndof = len(y) - len(pars)
print('chi quadro = %.3f (%d dof)' % (chisq, ndof))


#Definiamo un matrice di zeri che divverà la matrice di correlazione:
c=np.zeros((len(pars),len(pars)))
#Calcoliamo le correlazioni e le inseriamo nella matrice:
for i in range(0, len(pars)):
    for j in range(0, len(pars)):
       c[i][j]=(covm[i][j])/(np.sqrt(covm.diagonal()[i])*np.sqrt(covm.diagonal()[j]))
print(c) #matrice di correlazione


#Grafichiamo il risultato
fig1 = plt.figure(1)
#Parte superiore contenetnte il fit:
frame1=fig1.add_axes((.1,.35,.8,.6))
#frame1=fig1.add_axes((.trasla lateralmente,.trasla verticamente,.larghezza,.altezza))
frame1.set_title('Fit pinna di squalo',fontsize=20)
plt.ylabel('d.d.p [digit]',fontsize=10)
plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (0,0))#notazione scientifica sugliassi
plt.grid()


plt.errorbar(x, y, dy, fmt='.', color='black', label='dati') #grafico i punti
t=np.linspace(np.min(x),np.max(x), 1000)
s=f(t, *pars)
plt.plot(t,s, color='blue', alpha=0.5, label='best fit') #grafico la retta di best fit
plt.legend(loc='best')#inserisce la legenda nel posto migliorte



#Parte inferiore contenente i residui
frame2=fig1.add_axes((.1,.1,.8,.2))

#Calcolo i residui normalizzari
ff=(y-f(x, *pars))/dy
frame2.set_ylabel('Residui Normalizzati')
plt.xlabel('"tempo [$\mu$s]"',fontsize=10)
plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (0,0))

x1=np.linspace(np.min(x),np.max(x), 1000)
plt.plot(x1, 0*x1, color='red', linestyle='--', alpha=0.5) #grafico la retta costantemente zero
plt.plot(x, ff, '.', color='black') #grafico i residui normalizzati
plt.grid()

plt.show()
