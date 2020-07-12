# list = []
# while True:
#     a = int(input())
#     if a == 0:
#         break
#
#     for i in range(1,a+1,1):
#         list.append(i)
#         res = "".join(map(str,list))
#     print(res)
#     list = []
while True:
    v = int(input())
    if (v == 0):
        break
    r = ""
    for i in range(1, v + 1):
        r += str(i) + " "
    print(r[:-1])
