import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


N = 50
ex, ey = 0.01, 0.05
dy = np.array(N*[ey])
dx = np.array(N*[ex])
x = np.linspace(-5, 15, N)

#y = 1 + 0.5 * x + 0.2 * x**2 + 0.05 * x**3
y = 2*np.exp(-x**2) + np.exp( -((x - 7)/5)**2)
k = np.random.uniform(0, ey, N)
l = np.random.uniform(0, ex, N)
y = y + k #aggiungo errore
x = x + l

def f(x, *pars):
    '''
    Fit function.
    This function is designed to conveniently fit data
    whose model is a sum of the same function but with
    various parameters e.g. :

    A polynomial is the sum of monomials i.e. :
    a0 + a1*x + ... + an*x**n = \sum_i ai * x**i

    Or more in general we can fit:
    F = \sum_{\theta} f(x, {\theta})

    So what you do is loop on the single monomial or
    single function build the final function.
    In practice, we loop over the parameters by taking
    them one at a time or by taking a subset of them.
    To ensure that the code works it is therefore necessary
    to pass an array of inits to cruve_fit as in principle
    *pars are infinite parameters.
    Indeed, the length of init corresponds
    to how many parameters we are using.
    '''
    F = 0
    # For a polynomial it's okay to take one parameter at a time
    #for i, p in enumerate(pars):
    #    F += x**i * p

    # For a Gaussian we must take for each addend three parameters
    for p0, p1, p2 in zip(pars[0::3], pars[1::3], pars[2::3]):
        F += p0 * np.exp( -((x - p1)/p2)**2 )

    return F

init = np.array([1]*1)
init = np.array([1.5, 1, 1, 1, 6.5, 1])

#Eseguiamo il fit e stampiamo i risultati:
pars, covm = curve_fit(f, x, y, init, sigma=dy, absolute_sigma=False)
for i, p, dp in zip(range(len(pars)), pars, np.sqrt(covm.diagonal())):
    print(f'p{i} = {p:.5f} +- {dp:.5f}')

#Calcoliamo il chi quadro,indice ,per quanto possibile, della bontà del fit:
chisq = sum(((y - f(x, *pars))/dy)**2.)
ndof = len(y) - len(pars)
print(f'chi quadro = {chisq:.3f} ({ndof:d} dof)')


#Definiamo un matrice di zeri che divverà la matrice di correlazione:
c=np.zeros((len(pars),len(pars)))
#Calcoliamo le correlazioni e le inseriamo nella matrice:
for i in range(0, len(pars)):
    for j in range(0, len(pars)):
       c[i][j] = (covm[i][j])/(np.sqrt(covm.diagonal()[i])*np.sqrt(covm.diagonal()[j]))
print(c) #matrice di correlazione


#Grafichiamo il risultato
fig1 = plt.figure(1)
#Parte superiore contenetnte il fit:
frame1=fig1.add_axes((.1,.35,.8,.6))
#frame1=fig1.add_axes((trasla lateralmente, trasla verticamente, larghezza, altezza))
frame1.set_title('Fit dati simulati',fontsize=20)
plt.ylabel('ampiezza [u.a.]',fontsize=10)
#plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (0,0))#notazione scientifica sugliassi
plt.grid()


plt.errorbar(x, y, dy, dx, fmt='.', color='black', label='dati') #grafico i punti
t = np.linspace(np.min(x),np.max(x), 10000)
s = f(t, *pars)
plt.plot(t,s, color='blue', alpha=0.5, label='best fit') #grafico del best fit
plt.legend(loc='best')#inserisce la legenda nel posto migliorte


#Parte inferiore contenente i residui
frame2=fig1.add_axes((.1,.1,.8,.2))

#Calcolo i residui normalizzari
ff = (y-f(x, *pars))/dy
frame2.set_ylabel('Residui Normalizzati')
plt.xlabel('tempo [u.a.]',fontsize=10)
#plt.ticklabel_format(axis = 'both', style = 'sci', scilimits = (0,0))


plt.plot(t, 0*t, color='red', linestyle='--', alpha=0.5) #grafico la retta costantemente zero
plt.plot(x, ff, '.', color='black') #grafico i residui normalizzati
plt.grid()

plt.show()