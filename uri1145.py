a, b = list(map(int, input().split()))
lisst = []
add = 0
for i in range(1, b + 1, 1):
    for j in range(1, a + 1, 1):
        add += 1
        lisst.append(add)
        res = " ".join(map(str, lisst))
    if add > b:
        break
    print(res)
    lisst = []
