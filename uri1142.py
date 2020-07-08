a = int(input())
b = 1
add = 0
list = []
for i in range(b, a + 1, 1):
    for j in range(3):
        add += b
        list.append(add)
        res = " ".join(map(str, list))

    print(res, "PUM")
    list = []
    add += 1
