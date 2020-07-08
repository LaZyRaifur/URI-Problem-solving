a = 1
b = int(input())
add = 1
list = []
for i in range(a, b + 1, 1):
    for i in range(3):
        add *= a
        list.append(add)

        # print(add)
    res = " ".join(map(str, list))
    print(res)
    list = []
    a += 1
    add = 1
