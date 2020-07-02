a = int(input())
for i in range(1, a + 1):
    if i % 2 == 0:
        print("%d^2" % i + " = %d" % (i * i))
    i += 1
