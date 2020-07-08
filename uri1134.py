alcohol = 0
gasoline = 0
diesel = 0
while True:
    a = int(input())

    if a == 4:
        break
    elif a == 1:
        alcohol += 1
    elif a == 2:
        gasoline += 1
    elif a == 3:
        diesel += 1

print("MUITO OBRIGADO")
print("Alcool: %d" % alcohol)
print("Gasolina: %d" % gasoline)
print("Diesel: %d" % diesel)
