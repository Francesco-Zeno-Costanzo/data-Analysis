import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
x, y= np.loadtxt(r'C:\Users\franc\Desktop\datiL\datiL2\datilpf2\dls.txt', unpack = True)



T=x[len(x)-1]*1e-6 #ultimo valore di tempi in secondi, per far venire le frequenze in Hz

sp1 = np.fft.rfft(y) #fft per imput a valori reali
freq1 = np.fft.rfftfreq(len(y), T/len(y)) # resituisce array di frequenze equispaziate
#freq= np.fft.rfftfreq(lunghezza array che trasformi, spaziatura dell'array che trasformi)
f=40
def S(xx):
    return np.sin(2*np.pi*f*xx)
xx=np.linspace(0, 10, 2**11)

T=xx[len(xx)-1]

sp2 = np.fft.rfft(S(xx)) #fft per imput a valori reali
freq2 = np.fft.rfftfreq(len(xx), T/len(xx))

freq=np.delete(freq1,0)#tolgo componente continua
sp=np.delete(sp1, 0)

freq1=np.delete(freq2,0)
sp1=np.delete(sp2, 0)

plt.figure(1)
plt.subplot(221)
plt.title("Spettro segnale sinusoidale", fontsize=20)
plt.xlabel("f [Hz]", fontsize=10)
plt.ylabel(" $V_{out}$ [a.u.]", fontsize=10)
plt.plot(freq, abs(sp))
plt.grid()

plt.subplot(222)
plt.title("Spettro segnale sinusoidale simulato", fontsize=20)
plt.xlabel("f [Hz]", fontsize=10)
plt.ylabel(" $V_{out}$ [a.u.]", fontsize=10)
plt.grid()
plt.plot(freq1, abs(sp1))

plt.subplot(223)

plt.xlabel("f [Hz]", fontsize=10)
plt.ylabel(" $V_{out}$ [a.u.]", fontsize=10)
plt.plot(freq, abs(sp))
plt.yscale('log')
plt.grid()

plt.subplot(224)

plt.xlabel("f [Hz]", fontsize=10)
plt.ylabel(" $V_{out}$ [a.u.]", fontsize=10)
plt.grid()
plt.yscale('log')
plt.plot(freq1, abs(sp1))

plt.show()
