n = int(input())
while n:
    n -= 1
    value = input().split()
    a = value[0]
    b = value[1]
    lenA = len(a)
    lenB = len(b)

    if lenA >= lenB:
        if a[lenA - lenB:lenA] == b:
            res = a[lenA - lenB:lenA]
            # print(res)
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
