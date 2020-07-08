a = 7
b = 5
for i in range(1, 10, 2):

    for j in range(a, b - 1, -1):
        print("I=%d J=%d" % (i, j))
    b = a
    a = j + 4
