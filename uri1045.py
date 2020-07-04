# arr = [1,3,4,2]
# arr.sort(reverse = True)
# print(arr)
# def bubbleSort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(n,0):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# arr = [64,34,25,12,22,11,90]
# bubbleSort(arr)
# print("sorted array is:")
# for i in range(len(arr)):
#     print("%d"%arr[i])

# arr = list()
# temp = 0
# for i in range(int(3)):
#     n = float(input())
#     arr.append(float(n))
#     arr.sort(reverse=True)
# a = arr[0]
# b = arr[1]
# c = arr[2]

# a,b,c = list(map(float,input().split()))
# temp = 0
# if a<b:
#     temp = a
#     a = b
#     b = temp
# if b < c:
#     temp = b
#     b = c
#     c = temp
# if a < b:
#     temp = a
#     a = b
#     b = temp
#
#
# if a >= (b + c):
#     print("NAO FORMA TRIANGULO")
# elif a ** 2 == (b ** 2) + (c ** 2):
#     print("TRIANGULO RETANGULO")
# elif a ** 2 > (b ** 2 + c ** 2):
#     print("TRIANGULO OBTUSANGULO")
# elif a ** 2 < (b ** 2 + c ** 2):
#     print("TRIANGULO ACUTANGULO")
# if a == b and b== c:
#     print("TRIANGULO EQUILATERO")
# elif (a == b or b == c):
#     print("TRIANGULO ISOSCELES")
#
a, b, c = list(map(float, input().split()))
if (a < b):
    temp = a
    a = b
    b = temp
if (b < c):
    temp = b
    b = c
    c = temp
if (a < b):
    temp = a
    a = b
    b = temp
if (a >= (b + c)):
    print("NAO FORMA TRIANGULO")
elif (a * a == (b * b + c * c)):
    print("TRIANGULO RETANGULO")
elif (a * a > (b * b + c * c)):
    print("TRIANGULO OBTUSANGULO")
elif (a * a < (b * b + c * c)):
    print("TRIANGULO ACUTANGULO")
if (a == b and b == c):
    print("TRIANGULO EQUILATERO")
elif (a == b or b == c):
    print("TRIANGULO ISOSCELES")
