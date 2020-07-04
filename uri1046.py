arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
n = len(arr)
a = int(input())
b = int(input())
temp = 0
count = 0
for i in range(1, n + 1):
    if (a < b):
        temp = a
        a = b
        b = temp
