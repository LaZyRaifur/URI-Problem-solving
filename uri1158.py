n = int(input())
while n > 0:
    count = 0
    a, b = map(int, input().split())
    for i in range(a, (b * 2) + a):
        if i % 2 != 0:
            count += i
    print(count)
    n = n - 1
