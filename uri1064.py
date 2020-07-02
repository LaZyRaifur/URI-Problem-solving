count = 0
summ = 0
for i in range(0, 6):
    a = float(input())
    if a > 0:
        count += 1
        summ += a
print("%d valores positivos\n" % count + "%.1f" % (summ / count))
