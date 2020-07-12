inter = 0
gre = 0
draw = 0
title = 0
while True:
    a, b = list(map(int, input().split()))
    title += 1

    if (a > b):
        inter += 1
    elif (b > a):
        gre += 1
    elif (a == b):
        draw += 1
    c = int(input())
    if c == 2:
        break

for i in range(title):
    print("Novo grenal (1-sim 2-nao)")
print("%d grenais" % title)
print("Inter:%d" % inter)
print("Gremio:%d" % gre)
print("Empates:%d" % draw)
if inter > gre:
    print("Inter venceu mais")
elif gre > inter:
    print("Gremio venceu mais")

elif inter == gre:
    print("Nao houve vencedor")
#
# resp=1
# soma=0
# somaE=0
# somaI=0
# somaG=0
# while resp==1:
#     a,b=map(int, input().split())
#     soma+=1
#     if (a>b):
#         somaI+=1
#     elif(b>a):
#         somaG+=1
#     elif(a==b):
#         somaE+=1
#     resp=int(input("Novo grenal (1-sim 2-nao)"))
# print("%d grenais"%soma)
# print("Inter:%d" %somaI)
# print("Gremio:%d"%somaG)
# print("Empates:%d"%somaE)
# if (somaI>somaG):
#     print("Inter venceu mais")
# elif (somaG>somaI):
#     print("Gremio venceu mais")
# elif (somaI==somaG):
#     print("Nao houve vencedor")
