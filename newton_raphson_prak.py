def fungsi(a):
    fungsi = 9*pow(10, 9)*(3/pow(5-a, 2) + 6/pow(8-a, 2) -
                           5/pow(a, 2) - 2/pow(1+a, 2))
    return fungsi


def turunan(a):
    turunan = 9*pow(10, 9)*(6/pow(5-a, 3) + 12/pow(8-a, 3) +
                            10/pow(a, 3) + 4/pow(1+a, 3))
    return turunan


x = 2.
eps = 0.00001
delta = 1
print("x tebakan = ", x)
print("toleransi = ", eps)
while delta > eps:
    h = fungsi(x)/turunan(x)
    delta = abs(1-x/(x-h))
    x = x - h
print("x = ", x)
print("f(x) = ", fungsi(x))
