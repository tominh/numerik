'''
TIDAK UNTUK INTEGRAL FUNGSI SINUS COSINUS
'''

import numpy as np

x = [np.radians(90), np.radians(0)]  # Diisi dengan [batasBawah, batasAtas]
g = 9.8
l = 1
v_0 = 2

n = pow(x[1]-x[0], 10)
h = (np.amax(x)-np.amin(x))/n


def fungsi(x):
    fungsi = 1.0 / \
        np.sqrt(((np.cos(x)-np.cos(np.radians(10)))*2*g/l) + pow(v_0/l, 2))
    return fungsi


def trapesium(x):
    trapesium = (fungsi(x)+fungsi(x+h))*h/2
    return trapesium


integral = 0
bawah = x[0]
for i in range(10):
    integral += trapesium(bawah)
    bawah += h
    print("Hasil :", integral)

if x[0] > x[1]:
    integral *= -1
