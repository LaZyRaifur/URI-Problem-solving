import math

while 1:
    tw = 12
    try:
        d, vf, vg = map(int, input().split())
        x = math.sqrt((tw * tw) + (d * d))
        tf = tw / vf
        tg = x / vg

        if tg > tf:
            print("N")
        else:
            print("S")
    except EOFError:
        break
