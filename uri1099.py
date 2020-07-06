a = int(input())
sum = 0
for i in range(a):
    x, y = list(map(int, input().split()))
    temp = 0
    if x > y:
        temp = x
        x = y
        y = temp
    for j in range(x + 1, y):

        if j % 2 != 0:
            sum += j
    print(sum)
    sum = 0
