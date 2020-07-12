res1 = 0.0
res2 = 0.0
res3 = 0.0
d = 0.0
c = 0.0
b = 0.0
a = float(input())

b = a - 2000.00
if b >= 1000.00:
    res1 = (1000 * 8) / 100
    c = b - 1000.00
else:
    res1 = (b * 8) / 100
if c > 1500.00:
    res2 = (1500 * 18) / 100
    d = c - 1500
else:
    res2 = (c * 18) / 100

res3 = (d * 28) / 100
if a > 2000.00:
    print("R$ %.2f" % (res1 + res2 + res3))

if a >= 0.0 and a <= 2000.00:
    print("Isento")
