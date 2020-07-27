fh, fm, lh, lm = list(map(int, input().split()))
ch = 0
cm = 0
ch = lh - fh
cm = lm - fm

if (ch < 0):
    ch = (24 + lh) - fh
if (cm < 0):
    cm = (lm + 60) - fm
    ch -= 1
if lh == fh and lm == fm:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (ch, cm))
