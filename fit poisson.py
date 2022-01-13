import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.optimize import curve_fit

#genero dati da fittare distribuiti secondo una poissoniana
media = 69
dati = poisson.rvs(media, size=5000)

"""
bin del nostro istogramma, praticamente è un array che contiene
il valore sinistro della barra; i.e. nel grafico la barra del conteggio
di un certo numero k andrà da k-0.5 a k+0.5 in modo che k sia in mezzo
bins è esattamente l'array dei k-0.5.
N deve essere maggiore di media
"""
N = 100
bins = np.arange(N) - 0.5

'''
entrate è il numero di entarte di ogni bin
quindi quanti conteggi ho per singolo k, l'altezza della barra
la sintassi ,_ ,_ sta ad indicare che ignoro gli altri due return
'''
entrate ,_ ,_ = plt.hist(dati, bins=bins, density=True, label='Dati')

'''
se bins è l'array dei k-0.5
centro_bin è l'array dei k
'''
centro_bin = 0.5 * (bins[1:] + bins[:-1])


def f(k, media):
    '''
    pmf è la funzione di massa di probabilità
    dà la probabilità che una variabile discreta assuma
    esattamente un dato valore; una densità di probabilità discreta
    '''
    return poisson.pmf(k, media)

popt, cov = curve_fit(f, centro_bin, entrate)

media = popt[0]
dmedia = np.sqrt(cov[0,0])
print(f"media = {media} +- {dmedia}")

plt.figure(1)
plt.title('fit di una poissoniana', fontsize=15)
plt.plot(centro_bin, f(centro_bin, *popt), linestyle='-', label='Fit result')
plt.legend()
plt.grid()
plt.show()