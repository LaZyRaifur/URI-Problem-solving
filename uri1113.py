while (1):
    a, b = list(map(int, input().split()))
    if a > b:
        print("Decrescente")
    elif a < b:
        print("Crescente")
    elif a == b:
        break
