f = []
for i in range(0, 10):
    i = int(input())
    f.append(i)
for i in range(0, 10):
    if f[i] <= 0:
        f[i] = 1
    print("X[%d" % i + "] = %d" % f[i])
