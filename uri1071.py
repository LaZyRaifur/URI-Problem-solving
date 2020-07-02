x = int(input())
y = int(input())
res = 0

for i in range((y + 1), x):
    if i % 2 != 0:
        res += i
print(res)
