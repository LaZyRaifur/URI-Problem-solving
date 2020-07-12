count = 0
add = 0.0
while True:
    # add = 0
    # count = 0
    a = float(input())
    if a >= 0.0 and a <= 10.0:
        count += 1
        print(count)
        add += a
        if count == 2:
            print("media = %.2f" % (add / count))
            print("novo calculo (1-sim 2-nao)")
            b = int(input())
            if b == 1:
                print("novo calculo (1-sim 2-nao)")
            elif b == 2:
                break

    else:
        print("nota invalida")
