a, b = map(int, input().split())
temp = 0

if b < a:
    temp = a
    a = b
    b = temp
if b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
