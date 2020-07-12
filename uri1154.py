count = 0
add = 0
while True:
    a = int(input())

    if a < 0:
        break
    else:
        add += a
        count += 1
res = (add / count)
print("%.2f" % res)
