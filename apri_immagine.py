import matplotlib as mp
import matplotlib.pyplot as plt

'''
nel primo path ci vogliono i \\ perchè lo chiede la funzione per aprire il file.
il file txt su cui scrivere se non esiste lo crea lui
'''

path_dati =r"C:\\Users\\franc\\Desktop\\dati0.txt"
path_img = r"C:\Users\franc\Desktop\DatiL\datiL3\FIS2\eOverm\DSC_0005.jpg"

fig, ax = plt.subplots()

img = mp.image.imread(path_img)

ax.imshow(img)


def onclick(event):
    file= open(path_dati, "a") #apre file, il permesso è a altrimenti sovrascriverebbe i dati

    x=event.xdata
    y=event.ydata
    print('x=%f, y=%f' %(x, y)) #stampa i dati sulla shell

    file.write(str(x)) #scrive i dati sul file belli pronti per essere letti da codice del fit
    file.write('\t')
    file.write(str(y))
    file.write('\n')
    file.close() #chiude il file


fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
