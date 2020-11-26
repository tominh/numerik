import matplotlib.pyplot as plt

batas_bawah = int(input("Batas bawah : "))
batas_atas = int(input("Batas atas : "))
N = 10
h = (batas_atas - batas_bawah)/N

x = []
for i in range(N+1):
    x.append(batas_bawah + i*h)


def fungsi(x):
    fungsi = pow(x, x) - x
    return fungsi


fung_ganjil = 0
fung_genap = 0
for i in range(len(x)-1):
    if i == 0:
        pass
    elif i % 2 == 0:
        fung_genap += fungsi(x[i])
    elif i % 2 == 1:
        fung_ganjil += fungsi(x[i])
    else:
        pass

simpson = (fungsi(x[0]) + 4*fung_ganjil + 2*fung_genap + fungsi(x[-1]))*h/3
print('N :', N)
print('Integral x^x - x = Hasil Approximation :', simpson)

y = []
for i in range(len(x)):
    y.append(fungsi(x[i]))

plt.title(r'$F(x) = x^x - x$')
plt.xlabel('x (meter)')
plt.ylabel('F(x) (meter)')

plt.plot(x, y)
plt.axis([x[0], x[-1], y[0], y[-1]])
plt.show()
