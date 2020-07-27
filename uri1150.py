while True:
    count = 0
    add = 0
    a = int(input())
    b = int(input())

    if b < a:
        b = int(input())
        for i in range(a, b + 1):
            count += i
            if count <= b:
                add += 1
        print(add)
        break
