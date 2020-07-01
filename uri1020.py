day = int(input())

year = 0
while day >= 365:
    year += 1
    day -= 365
    if day < 365:
        break

month = 0
while day >= 30:
    month += 1
    day -= 30
    if day < 30:
        break

print("%d ano(s)" % year)
print("%d mes(es)" % month)
print("%d dia(s)" % day)
