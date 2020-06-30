line = str(input(""))
split = line.split()
a = int(split[0])
b = int(split[1])
c = int(split[2])

if a > c and b > c:
    if a > b:
        print("%d eh o maior" % a)
    else:
        print("%d eh o maior" % b)

elif b > a and c > a:
    if b > c:
        print("%d eh o maior" % b)
    else:
        print("%d eh o maior" % c)

elif b < a and c > b:
    if a > c:
        print("%d eh o maior" % a)
    else:
        print("%d eh o maior" % c)
