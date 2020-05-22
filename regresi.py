# Program Rumus Regresi
# By : Tomi Nurhidayat

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Variabel kosong bertipe array untuk menyimpan data x dan y
x = []
y = []

garis = '='*50
print(garis, '\nUntuk Menghitung Regresi Diperlukan Data > 2')
print(garis)

# Untuk meminta jumlah data yang akan dihitung
banyakData = int(input('Jumlah pasangan data (x,y) : '))

# Jika data > 2 maka akan dieksekusi
if banyakData > 2:
    # Untuk meminta input data
    for j in range(banyakData):
        dataX = float(input('X : '))
        x.append(dataX)
        dataY = float(input('Y : '))
        y.append(dataY)

    # gradien, titik potong sb y, faktor korelasi, dsb jangan tertukar urutan
    slope, intercept, r, p, std_err = stats.linregress(x, y)

    # fungsi untuk regresinya
    def fungsi(x):
        return slope*x + intercept

    # pemodelan
    pemodelan = list(map(fungsi, x))

    # Untuk mencacri Sy
    def Sy(a, b, c, d, e, f):
        syKuadrat = (a - ((b*c)-2*d+(banyakData*e)) /
                     ((banyakData*b)-f))/(banyakData-2)
        sy = np.sqrt(syKuadrat)
        return sy

    # Untuk mencari gradien

    def gradien(a, b, c, d, e):
        m = ((banyakData*a)-(b*c))/((banyakData*d)-e)
        return m

    # Untuk mencari ralat gradien

    def ralatGradien(a, b, c):
        ralatGradien = a*np.sqrt(banyakData/((banyakData*b)-c))
        return ralatGradien

    # Untuk mencari titik potong

    def titikPotong(a, b, c, d, e):
        titikPotong = ((a*b)-(c*d))/((banyakData*a)-e)
        return titikPotong

    # Untuk mencari ralat titik potong

    def ralatTitikpotong(a, b, c):
        ralatTitikpotong = a*np.sqrt(b/((banyakData*b)-c))
        return ralatTitikpotong

    # Untuk mencari sigma X dan sigma Y
    sigmaX = 0
    sigmaY = 0
    for i in range(banyakData):
        sigmaX = sigmaX + x[i]
        sigmaY = sigmaY + y[i]

    # Untuk mencari (sigma X) kuadrat dan (sigma Y) kuadrat
    sigmaXkuadrat = pow(sigmaX, 2)
    sigmaYkuadrat = pow(sigmaY, 2)

    # Untuk mencari sigma(X dikuadratkan) dan sigma(Y dikuadratkan)
    sigmaXdikuadrat = 0
    sigmaYdikuadrat = 0
    for k in range(banyakData):
        sigmaXdikuadrat = sigmaXdikuadrat + pow(x[k], 2)
        sigmaYdikuadrat = sigmaYdikuadrat + pow(y[k], 2)

    # Untuk mencari xy
    sigmaxy = 0
    for a in range(banyakData):
        sigmaxy = sigmaxy + x[a]*y[a]

    # Untuk (sigmaXY) dikuadratkan
    sigmaXYkuadrat = pow(sigmaxy, 2)

    # Untuk mencari sigmaX.sigmaY.sigmaXY
    sigmaXsigmaYsigmaXY = sigmaX*sigmaY*sigmaxy

    # Nilai Sy
    sY = Sy(sigmaYdikuadrat, sigmaXdikuadrat, sigmaYkuadrat,
            sigmaXsigmaYsigmaXY, sigmaXYkuadrat, sigmaXkuadrat)
    # Nilai gradien
    gradien = gradien(sigmaxy, sigmaX, sigmaY, sigmaXdikuadrat, sigmaXkuadrat)
    # Nilai ralat gradien
    ralatGradien = ralatGradien(sY, sigmaXdikuadrat, sigmaXkuadrat)
    # Nilai titik potong
    titikPotong = titikPotong(sigmaXdikuadrat, sigmaY,
                              sigmaX, sigmaxy, sigmaXkuadrat)
    # Nilai ralat titik potong
    ralatTitikpotong = ralatTitikpotong(sY, sigmaXdikuadrat, sigmaXkuadrat)

    # Titik potong sb X
    titikPotongX = -(titikPotong)/gradien

    print('sigmaX :', sigmaX)
    print('(sigmaX)^2 :', sigmaXkuadrat)
    print('sigma(X^2) :', sigmaXdikuadrat)
    print('sigmaY :', sigmaY)
    print('(sigmaY)^2 :', sigmaYkuadrat)
    print('sigma(Y^2) :', sigmaYdikuadrat)
    print('sigmaXY :', sigmaxy)
    print('sigmaXsigmaYsigmaXY :', sigmaXsigmaYsigmaXY)
    print('(sigmaXY)^2 :', sigmaXYkuadrat, '\n')

    # Untuk menampilkan Sy, gradien, titik potong
    print('Sy :', sY)
    print('gradien :', gradien)
    print('ralat gradien :', ralatGradien)
    print('titik potong sumbu Y :', titikPotong)
    print('ralat titik potong sumbu Y :', ralatTitikpotong)
    print('titik potong sumbu X :', titikPotongX)
    print('faktor korelasi :', r)
    print('Y =', gradien, 'X + (', titikPotong, ')')

    # Untuk membuat grafik
    plt.scatter(x, y)
    plt.plot(x, pemodelan)
    plt.grid(True)
    plt.show()

# Jika data <= 2 tidak akan dieksekusi
else:
    print('Jumlah data yang anda masukkan tidak memenuhi rumus regresi !!')
