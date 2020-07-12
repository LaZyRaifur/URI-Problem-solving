a = int(input())
b = int(input())
temp = 0
if b > a:
    temp = b
    b = a
    a = temp

print((a % b))
