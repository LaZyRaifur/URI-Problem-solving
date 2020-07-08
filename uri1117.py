count = 0.0
sum = 0
while True:
    a = float(input())

    if a >= 0 and a <= 10.0:
        count += a;
        sum += 1
        if sum == 2:
            break
    else:
        print("nota invalida")

print("media = %.2f" % (count / 2))
