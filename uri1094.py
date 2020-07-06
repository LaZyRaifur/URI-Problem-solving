a = int(input())
rabbit = 0
rat = 0
frog = 0
total = 0
for i in range(a):
    num, strR = list(map(str, input().split()))
    num = int(num)
    total += num
    if strR == 'C':
        rabbit += num
    if strR == 'R':
        rat += num
    if strR == 'S':
        frog += num
print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % rabbit)
print("Total de ratos: %d" % rat)
print("Total de sapos: %d" % frog)
rab_per = (rabbit * 100) / total
rat_per = (rat * 100) / total
fro_per = (frog * 100) / total
print("Percentual de coelhos: " + "%.2f" % rab_per + " %")
print("Percentual de ratos: " + "%.2f" % rat_per + " %")
print("Percentual de sapos: " + "%.2f" % fro_per + " %")
