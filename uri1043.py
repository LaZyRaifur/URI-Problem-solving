a, b, c = list(map(float, input().split()))
mod1 = 0
mod2 = 0
mod3 = 0

if b - c < 0:
    mod1 = c - b
else:
    mod1 = b - c
if b - a < 0:
    mod2 = a - b
else:
    mod2 = a - b
if c - a < 0:
    mod3 = a - c
else:
    mod3 = c - a

if a > mod1 and a < (b + c) and b > mod3 and b < (a + c) and c > mod2 and c < (a + b):
    per = a + b + c
    print("Perimetro = %.1f" % per)
else:
    area = ((a + b) * c) / 2
    print("Area = %.1f" % area)
