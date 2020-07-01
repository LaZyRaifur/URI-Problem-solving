A = float(input())
N = A
hundred = N / 100
N %= 100
fifty = N / 50
N %= 50
twenty = N / 20
N %= 20
ten = N / 10
N %= 10
five = N / 5
N %= 5
two = N / 2
N %= 2

E = N * 100
B = (int(E))
f_hundred = B / 100
B %= 100
f_fifty = B / 50
B %= 50
f_twenty = B / 25
B %= 25
f_ten = B / 10
B %= 10
f_five = B / 5
B %= 5
f_one = B / 1

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(hundred)))
print("{} nota(s) de R$ 50.00".format(int(fifty)))
print("{} nota(s) de R$ 20.00".format(int(twenty)))
print("{} nota(s) de R$ 10.00".format(int(ten)))
print("{} nota(s) de R$ 5.00".format(int(five)))
print("{} nota(s) de R$ 2.00".format(int(two)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(f_hundred)))
print("{} moeda(s) de R$ 0.50".format(int(f_fifty)))
print("{} moeda(s) de R$ 0.25".format(int(f_twenty)))
print("{} moeda(s) de R$ 0.10".format(int(f_ten)))
print("{} moeda(s) de R$ 0.05".format(int(f_five)))
print("{} moeda(s) de R$ 0.01".format(int(f_one)))
