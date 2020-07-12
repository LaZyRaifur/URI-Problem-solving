def fact(n):
    factorial = 1
    while (n > 1):
        factorial = factorial * n
        n = n - 1
    return factorial


a = int(input())
print(fact(a))
