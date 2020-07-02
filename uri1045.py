a, b, c = map(float, input().split())
temp = 0

if b > a and c > a:
    temp = c
    c = b
    b = temp
if b > a and a > c:
    temp = a
    a = b
    b = temp
if b < a and a < c:
    temp = a
    a = c
    c = temp
print(a)
print(b)
print(c)

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
if a ** 2 == (b ** 2) + (c ** 2):
    print(" TRIANGULO RETANGULO")
if a ** 2 > (b ** 2 + c ** 2):
    print("TRIANGULO OBTUSANGULO")
if a ** 2 < (b ** 2 + c ** 2):
    print("TRIANGULO ACUTANGULO")
if a == b == c:
    print("TRIANGULO EQUILATERO")
if a == b:
    if b != c or a != c:
        print("TRIANGULO ISOSCELES")
if c == b:
    if c != a or b != a:
        print("TRIANGULO ISOSCELES")
if a == c:
    if c != b or a != b:
        print("TRIANGULO ISOSCELES")
