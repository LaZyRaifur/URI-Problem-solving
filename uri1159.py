while True:
    n = int(input())
    count = 0
    if n == 0:
        break
    for i in range(n, n + 10):
        if i % 2 == 0:
            count += i
    print(count)
