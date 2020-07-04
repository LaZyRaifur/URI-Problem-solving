a = float(input())
tem = 0.0
if a > 0 and a <= 400.00:
    tem = (a * 15) / 100
    print("Novo salario: %.2f" % (a + tem))
    print("Reajuste ganho: %.2f" % tem)
    print("Em percentual: 15 %")
elif a >= 400.01 and a <= 800.00:
    tem = (a * 12) / 100
    print("Novo salario: %.2f" % (a + tem))
    print("Reajuste ganho: %.2f" % tem)
    print("Em percentual: 12 %")
elif a >= 800.01 and a <= 1200.00:
    tem = (a * 10) / 100
    print("Novo salario: %.2f" % (a + tem))
    print("Reajuste ganho: %.2f" % tem)
    print("Em percentual: 10 %")
elif a >= 1200.01 and a <= 2000.00:
    tem = (a * 7) / 100
    print("Novo salario: %.2f" % (a + tem))
    print("Reajuste ganho: %.2f" % tem)
    print("Em percentual: 7 %")
elif a > 2000.00:
    tem = (a * 4) / 100
    print("Novo salario: %.2f" % (a + tem))
    print("Reajuste ganho: %.2f" % tem)
    print("Em percentual: 4 %")
