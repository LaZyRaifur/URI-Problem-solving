while 1:
    a, b = map(int, input().split())
    list = []
    temp = 0

    if a > b:
        temp = a
        a = b
        b = temp

    if a <= 0 or b <= 0:
        break
    for i in range(a, b + 1):
        list.append(i)
        res = " ".join(map(str, list))
        summ = sum(list)

    print(res, "Sum=%d" % summ)
    list = []
