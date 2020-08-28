a = []
for i in range(0, 20):
    i = int(input())
    a.append(i)
for i in range(20, 0, -1):
    for j in range(0, 20):
        print(a[j])
