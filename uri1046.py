x, y = map(int, input().split())
temp = y
if x >= y:
    temp += 24
    print("O JOGO DUROU %d HORA(S)" % (temp - x))
else:
    print("O JOGO DUROU %d HORA(S)" % (y - x))
