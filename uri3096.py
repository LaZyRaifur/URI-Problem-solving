def DPfact(N):
    arr = {}
    if N in arr:
        return arr[N]
    elif N == 0 or N == 1:
        return 1
        arr[N] = 1
    else:
        factorial = N * DPfact(N - 1)
        arr[N] = factorial
        print(arr[N])
    return factorial


num = 5

print(DPfact(num))

# # a = int(input())
# # sum = 1
# # add = 2
# # for i in range (1,a+1,1):
# #     sum = sum * i
# # print(sum)
# # v = str(sum)
# # l = len(v)
# # print(l)
# import sys
#
# def factorial(n):
#     res = [None] * 500
#
#     res[0] = 1
#     res_size = 1
#
#     x = 2
#     while x <= n:
#         res_size = multiply(x, res, res_size)
#         x = x + 1
#
#     print("Factorial of given number is")
#     i = res_size - 1
#     while i >= 0:
#         sys.stdout.write(str(res[i]))
#         sys.stdout.flush()
#         i = i - 1
#
#
# def multiply(x, res, res_size):
#     carry = 0  # Initialize carry
#
#     i = 0
#     while i < res_size:
#         prod = res[i] * x + carry
#         res[i] = prod % 10;  # Store last digit of
#         carry = prod // 10;  # Put rest in carry
#
#         i = i + 1
#
#     while (carry):
#         res[res_size] = carry % 10
#         carry = carry // 10
#         res_size = res_size + 1
#
#     return res_size
#
#
# # Driver program
# factorial(100)
