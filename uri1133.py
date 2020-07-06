a = int(input())
b = int(input())
temp = 0
if a > b:
    temp = a
    a = b
    b = temp
for i in range(a + 1, b):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
