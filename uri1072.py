a = int(input())

count = 0
other = 0
while a > 0:
    a -= 1
    b = int(input())
    if b > 9 and b < 21:
        count += 1

    else:
        other += 1

print("%d in" % count)
print("%d out" % other)
