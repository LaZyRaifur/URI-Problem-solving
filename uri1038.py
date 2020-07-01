# code = int(input())
# quantity = int(input())
code, quantity = map(int, input().split())

if code == 1:
    price = (float(quantity * 4.00))
    print("Total: R$ %.2f" % price)
elif code == 2:
    price = (float(quantity * 4.50))
    print("Total: R$ %.2f" % price)
elif code == 3:
    price = (float(quantity * 5.00))
    print("Total: R$ %.2f" % price)
elif code == 4:
    price = (float(quantity * 2.00))
    print("Total: R$ %.2f" % price)
elif code == 5:
    price = (float(quantity * 1.50))
    print("Total: R$ %.2f" % price)
