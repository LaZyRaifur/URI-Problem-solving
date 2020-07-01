a = float(input())
n = a / 100
m = a % 100
print(a)
print("%d nota(s) de R$ 100,00" % n)
n = m / 50
x = m % 50
print("%d nota(s) de R$ 50,00" % n)
n = x / 20
o = x % 20
print("%d nota(s) de R$ 20,00" % n)
n = o / 10
p = o % 10
print("%d nota(s) de R$ 10,00" % n)
n = p / 5
q = p % 5
print("%d nota(s) de R$ 5,00" % n)
n = q / 2
r = q % 2
print("%d nota(s) de R$ 2,00" % n)
n = r / 1
s = r % 1
print("%d nota(s) de R$ 1,00" % n)
