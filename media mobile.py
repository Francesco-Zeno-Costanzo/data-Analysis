import numpy as np
import matplotlib.pyplot as plt

file = 'DSO00002'
path = r'c:\Users\franc\Desktop\DatiL\%s.csv'%(file)
tt, aa, bb = np.loadtxt(path,usecols=[0,1,2],skiprows=2,delimiter=',',unpack=True)

t=np.ones(len(bb))#array degli eventuali pesi

def mm(v,q, t):
    vm=np.array([])
    n = len(v)
    for i in range(n):
        if i<q:
            a=sum(t[i]*v[i:i+q])/(q)
            vm=np.insert(vm, len(vm), a)
        if i>=q and i<n-q:
            b=sum(t[i]*v[i-q:i+q])/(2*q)
            vm=np.insert(vm, len(vm), b)
        if i>=n-q:
            c=sum(t[i]*v[i-q:i])/(q)
            vm=np.insert(vm, len(vm), c)
    return vm

m=mm(bb, 20, t)

plt.figure(1)
plt.errorbar(tt, bb, fmt='.')
plt.grid()
plt.errorbar(tt, m, fmt='.', color='red')
plt.show()