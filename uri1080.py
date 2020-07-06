maxx = 0
p = 0
for i in range(1, 101):
    a = int(input())
    if maxx < a:
        maxx = a
        p = i

print(maxx)
print(p)
