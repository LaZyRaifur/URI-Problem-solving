while True:
    try:
        a, min, max = [int(i) for i in input().split()]
        t = 0
        while a:
            a -= 1
            m = int(input())
            if m >= min and m <= max:
                t += 1
        print(t)
    except EOFError:
        break
