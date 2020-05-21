# Nama : Tomi Nurhdayat
# Prodi : Fisika
# Integral Nomor 1

# Deklarasi
x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,
     5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
h = 0.5


def fungsi(x):                          # fungsi f(x)
    return 1 + x - pow(x, 2)


def fung_trapesium(x):                  # fungsi integral untuk metode trapesium
    return (fungsi(x)+fungsi(x+h))*h/2


def fung_analitik(x):                   # fungsi hasil integral analitik
    return x + (pow(x, 2)/2) - pow(x, 3)/3


# Untuk menampilkan nilai dengan metode trapesium
y_trapesium = 0
for i in range(len(x)-1):
    y_trapesiumPerindex = fung_trapesium(x[i])
    y_trapesium = y_trapesium + y_trapesiumPerindex
    print("Index ke", i, "\nX", i, "=",
          x[i], "\nNilainya :", y_trapesiumPerindex)
print("Jumlah Nilainya :", y_trapesium, "\n")


# Untuk menampilkan nilai dengan metode simpson
y_simpson = 0
for j in range(len(x)):
    if j == 0:
        awal = x[j]
        y_simpsonPerindex = (fungsi(awal)*h/3)
        print("Index ke", j, "\nX", j, "=",
              x[j], "\nNilainya :", y_simpsonPerindex)
        y_simpson += y_simpsonPerindex
    elif j % 2 != 0:
        ganjil = x[j]
        y_simpsonPerindex = (4*fungsi(ganjil)*h/3)
        print("Index ke", j, "\nX", j, "=",
              x[j], "\nNilainya :", y_simpsonPerindex)
        y_simpson += y_simpsonPerindex
    elif j != 0 and j % 2 == 0 and j < (len(x)-1):
        genap = x[j]
        y_simpsonPerindex = (2*fungsi(genap)*h/3)
        print("Index ke", j, "\nX", j, "=",
              x[j], "\nNilainya :", y_simpsonPerindex)
        y_simpson += y_simpsonPerindex
    else:
        akhir = x[j]
        y_simpsonPerindex = fungsi(akhir)*h/3
        print("Index ke", j, "\nX", j, "=",
              x[j], "\nNilainya :", y_simpsonPerindex)
        y_simpson += y_simpsonPerindex
print("Jumlah Nilainya :", y_simpson)

# Hasil akhir untuk membandingkan
print("\nNilai Integral Dengan Metode Trapesium :", y_trapesium)
print("Nilai Integral Dengan Metode Simpson :", y_simpson)
print("Nilai Integral Dari Fungsi Analitik :",
      fung_analitik(x[20])-fung_analitik(x[0]))
