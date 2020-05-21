import numpy as np
import matplotlib.pyplot as plt


def sinus(amplitudo, frekuensi, tAkhir, theta):                 # fungsi sinusoidal
    t = np.arange(0, tAkhir, 0.001)
    y = amplitudo*np.sin(2*3.14*frekuensi*t + np.deg2rad(theta))
    return t, y


amplitudo = 1
frekuensi = 0.2
waktuAkhir = 20
fase1 = 0
fase2 = 90
fase3 = 180
fase4 = 270

# pemanggilan fungsi
t1, y1 = sinus(amplitudo, frekuensi, waktuAkhir, fase1)
t2, y2 = sinus(amplitudo, frekuensi, waktuAkhir, fase2)
t3, y3 = sinus(amplitudo, frekuensi, waktuAkhir, fase3)
t4, y4 = sinus(amplitudo, frekuensi, waktuAkhir, fase4)

judul = 'Grafik Sinusoidal '
rumus = r'$\mathcal{y} = A sin(\omega t + \theta)$' + '\n'
parameter1 = r'$A = $' + str(amplitudo) + ' cm, '
parameter2 = r'$Frekuensi = $' + str(frekuensi) + ' ' + r'$\mathit{Hz}$' + '\n'
parameter3 = 'Grafik Merah' + ' ' + \
    r'$\theta = $' + str(fase1) + r'$^o$' + ', '
parameter4 = 'Grafik Biru' + ' ' + r'$\theta = $' + str(fase2) + r'$^o$' + ', '
parameter5 = 'Grafik Kuning' + ' ' + \
    r'$\theta = $' + str(fase3) + r'$^o$' + ', '
parameter6 = 'Grafik Hijau' + ' ' + r'$\theta = $' + str(fase4) + r'$^o$'

# data plot
dataPlot1 = plt.plot(t1, y1)
dataPlot2 = plt.plot(t2, y2)
dataPlot3 = plt.plot(t3, y3)
dataPlot4 = plt.plot(t4, y4)

# label
plt.title(judul + rumus + parameter1 + parameter2 +
          parameter3 + parameter4 + parameter5 + parameter6)
plt.xlabel('Waktu(s)')
plt.ylabel('Amplitudo(cm)')

# properties        plt.setp(dataPlot, properties)
plt.setp(dataPlot1, color='r', linestyle='-.', linewidth=0.5)
plt.setp(dataPlot2, color='b', linestyle='dotted', linewidth=1)
plt.setp(dataPlot3, color='y', linestyle='--', linewidth=1.5)
plt.setp(dataPlot4, color='g', linestyle=':', linewidth=2)

# setting axis      plt.axis([xmin,xmax,ymin,ymax])
plt.axis([1, waktuAkhir, -(amplitudo+1), (amplitudo+1)])

# menampilkan plot
plt.show()
