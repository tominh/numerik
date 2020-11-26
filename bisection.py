from math import pi, sin, cos, asin, sqrt
import numpy as np
from matplotlib import pyplot as plt


def fung(x):
    fung = pow(x, 2) - 1
    return fung


def bisection(x1, x2):
    iterasi = 0
    eps = 0.0001
    ralat = 0.1
    while (ralat > eps):
        xm = (x1+x2)/2.0
        f1f2 = fung(x1)*fung(xm)
        if (f1f2 < 0.0):
            x2 = xm
        else:
            x1 = xm
        ralat = abs((x2-x1)/x2)
        print("Interval Baru : [", x1, ",", x2, "]")
    return xm


print("x", bisection(0, 4))
