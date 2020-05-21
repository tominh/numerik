# Nama : Tomi Nurhidayat
# Prodi : Fisika
# Pendekatan Interpolasi

x0 = 0
x1 = 0.8
x2 = 1.6
x3 = 2.4
x4 = 3.2
x5 = 4
y0 = pow(x0, 3)-4*pow(x0, 2)+5*x0+5
y1 = pow(x1, 3)-4*pow(x1, 2)+5*x1+5
y2 = pow(x2, 3)-4*pow(x2, 2)+5*x2+5
y3 = pow(x3, 3)-4*pow(x3, 2)+5*x3+5
y4 = pow(x4, 3)-4*pow(x4, 2)+5*x4+5
y5 = pow(x5, 3)-4*pow(x5, 2)+5*x5+5
data0 = 0.25
data1 = 0.5
data2 = 0.75
data3 = 1.25
data4 = 1.5
data5 = 1.75


def f(x):
    f = pow(x, 3)-4*pow(x, 2)+5*x+5
    df = 3*pow(x, 2)-8*x+5
    ddf = 6*x-8
    return ddf


print("Data yang akan di interpolasi : 0.25; 0.5; 0.75; 1.25; 1.5; 1.75")
print("Interval : [0, 0.8]")
gdata0 = y0+(data0-x0)*(y1-y0)/(x1-x0)
print("Interpolasi 0.25 : ", gdata0)
gdata1 = y0+(data1-x0)*(y1-y0)/(x1-x0)
print("Interpolasi 0.5 : ", gdata1)
gdata2 = y0+(data2-x0)*(y1-y0)/(x1-x0)
print("Interpolasi 0.75 : ", gdata2)
h = x1 - x0
xm = (x0+x1)/2
ralat = abs(pow(h, 2)*f(xm)/8)
print("Ralatnya : ", ralat)

print("\nInterval : [0.8, 1.6]")
gdata3 = y1+(data3-x1)*(y2-y1)/(x2-x1)
print("Interpolasi 1.25 : ", gdata3)
gdata4 = y1+(data4-x1)*(y2-y1)/(x1-x0)
print("Interpolasi 1.5 : ", gdata4)
h = x2 - x1
xm = (x1+x2)/2
ralat = abs(pow(h, 2)*f(xm)/8)
print("Ralatnya : ", ralat)

print("\nInterval : [1.6, 2.4]")
gdata5 = y2+(data5-x2)*(y3-y2)/(x3-x2)
print("Interpolasi 1.25 : ", gdata5)
h = x3 - x2
xm = (x2+x3)/2
ralat = abs(pow(h, 2)*f(xm)/8)
print("Ralatnya : ", ralat)
