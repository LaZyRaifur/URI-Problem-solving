x = int(input())
y = int(input())
temp = 0
sum = 0
if y < x:
    temp = x
    x = y
    y = temp
for j in range(x, y + 1):
    if (j % 13 != 0):
        sum += j

print(sum)
