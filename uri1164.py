n = int(input())
while n > 0:
    count = 0
    a = int(input())
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            count += i
    if count == a:
        print("%d eh perfeito" % a)
    else:
        print("%d nao eh perfeito" % a)
    n -= 1
