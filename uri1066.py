pos = 0
neg = 0
odd = 0
even = 0

for i in range(0, 5):
    a = int(input())
    if a % 2 == 0:
        even += 1

    if a % 2 != 0:
        odd += 1
    if a > 0:
        pos += 1
    if a < 0:
        neg += 1
print(
    "%d valor(es) par(es)\n" % even + "%d valor(es) impar(es)\n" % odd + "%d valor(es) positivo(s)\n" % pos + "%d valor(es) negativo(s)" % neg)
