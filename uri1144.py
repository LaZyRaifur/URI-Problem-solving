a = 1
b = int(input())
add = 1
list = []
for i in range(a, b + 1, 1):
    for j in range(1, 4, 1):
        add *= a
        list.append(add)
        res = " ".join(map(str, list))
        m = add + 1
        n = a * a + 1
    print(res)
    print("%d %d %d" % (a, n, m))
    list = []
    a += 1
    add = 1
