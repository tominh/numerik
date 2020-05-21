# Nma : Tomi Nurhidayat
# Prodi : Fisika
# Integral Nomor 2

# deklarasi
x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,
     5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
h = 0.5


def fungsi(x):                                  # fungsi f(x)
    return 1 + x - pow(x, 2)


def anti_dfungsi(x):                            # hasil integral secara analitik
    return x + pow(x, 2)/2 - pow(x, 3)/3


def ganjil(index):                              # fungsi saat index ganjil
    hasil = (fungsi(x[index-1]) + fungsi(x[index]))*h/3
    return hasil


def genap(index):                               # fungsi saat index genap
    hasil = (3*fungsi(x[index-1]) + fungsi(x[index]))*h/3
    return hasil


# menampilkan plot fungsi dengan metode trapesium
print("="*50)
print("Plot Untuk Metode Trapesium\n")
for i in range(len(x)):
    if i == 0:
        plot = 0
        print("Y saat X", i, x[i], "==>", plot)
    elif i != 0:
        plot = plot + (fungsi(x[i-1]) + fungsi(x[i]))*h/2
        print("Y saat X", i, x[i], "==>", plot)

# menampilkan plot fungsi dengan metode simpson
print("="*50)
print("Plot Untuk Metode Simpson\n")
for j in range(len(x)):
    if j == 0:
        titik = 0
        print("Y saat X", j, "=", x[j], "==>", titik)
    elif j == 1:
        titik = (fungsi(x[j-1]) + fungsi(x[j]))*h/3
        print("Y saat X", j, "=", x[j], "==>", titik)
    elif j == 2:
        titik = titik + genap(j)
        print("Y saat X", j, "=", x[j], "==>", titik)
    elif j == 3:
        titik = titik + ganjil(j)
        print("Y saat X", j, "=", x[j], "==>", titik)
    elif j % 2 == 0:
        titik = titik + genap(j)
        print("Y saat X", j, "=", x[j], "==>", titik)
    elif j % 2 != 0:
        titik = titik + ganjil(j)
        print("Y saat X", j, "=", x[j], "==>", titik)


# menampilkan plot fungsi secara analitik
print("="*50)
print("Plot Untuk Fungsi Analitiknya\n")
for a in range(len(x)):
    y = anti_dfungsi(x[a])
    print("Y saat X", a, "=", x[a], "==>", y)
