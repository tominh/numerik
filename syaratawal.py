import matplotlib.pyplot as plt
from math import sin, pi, radians

m = 1
l = 10
g = 9.8
v0 = 0.05
x0 = 0.05
t0 = 0
delta_t = 0.01
n = 1000

v = []
x = []
E = []
t = []

v.append(v0)
x.append(x0)
t.append(t0)
E.append(0.5*m*pow(l, 2)*(pow(v[0], 2)+(g/l)*pow(x[0], 2)))

for i in range(n):
    t.append(t[i] + delta_t)
    x.append(x[i] + v[i]*delta_t)
    v.append(v[i] - (g/l)*delta_t*sin(radians(x[i])))
    E.append(0.5*m*pow(l, 2)*(pow(v[i], 2)+(g/l)*pow(x[i], 2)))

# print('omega = ', v)
# print('theta = ', x)
# print('energi = ', E)

plt.title(r'$v$ vs $t$ dan $x$ vs $t$')
plt.xlabel('t (s)')
plt.ylabel('v dan x')

plotKecepatan = plt.plot(t, v)
plotJarak = plt.plot(t, x)
# plotTenaga = plt.plot(t, E)

plt.setp(plotKecepatan, color='r')
plt.setp(plotJarak, color='b')
# plt.setp(plotTenaga, color='g')
plt.legend(["Kecepatan", "Jarak", "Tenaga"])
plt.show()
