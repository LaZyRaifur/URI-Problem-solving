x = int(input())

if x % 2 == 0:
    for i in range(x + 1, x + 12):
        if i % 2 != 0:
            print(i)
else:
    for i in range(x, x + 12):
        if i % 2 != 0:
            print(i)
