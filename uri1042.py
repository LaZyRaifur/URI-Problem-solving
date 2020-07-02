a, b, c = map(int, input().split())
temp = 0

if a > b and a > c:
    if b > c:
        print("%d\n" % c + "%d\n" % b + "%d\n" % a)

        print("%d\n" % a + "%d\n" % b + "%d" % c)
    elif c > b:
        print("%d\n" % b + "%d\n" % c + "%d\n" % a)

        print("%d\n" % a + "%d\n" % b + "%d" % c)
if b > a and b > c:
    if a > c:
        print("%d\n" % c + "%d\n" % a + "%d\n" % b)

        print("%d\n" % a + "%d\n" % b + "%d" % c)
    elif c > a:
        print("%d\n" % a + "%d\n" % c + "%d\n" % b)

        print("%d\n" % a + "%d\n" % b + "%d" % c)

if c > b and a < c:
    if a > b:
        print("%d\n" % b + "%d\n" % a + "%d\n" % c)

        print("%d\n" % a + "%d\n" % b + "%d" % c)
    elif b > a:
        print("%d\n" % a + "%d\n" % b + "%d\n" % c)

        print("%d\n" % a + "%d\n" % b + "%d" % c)
