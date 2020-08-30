n = int(input())

while n:
    n -= 1
    name = input()
    a = float(input())
    res = [float(x) for x in input().split()]
    res = sum(sorted(res)[1:6]) * a
    print(name, "%.2f" % res)

# def largest(b):
#     max = b[0]
#     for i in range(0,7):
#         if b[i] > max:
#             max = b[i]
#     return max
#
# def minimum(b):
#     min = b[0]
#     for i in range(0,7):
#         if b[i]<min:
#             min = b[i]
#     return min
#
# n = int(input())
# while n:
#     n -= 1
#     name = str(input())
#     a = float(input())
#     b = []
#     count = 0
#     res = 0
#     for i in range (0,7):
#         i = float(input())
#         b.append(i)
#         count += i
#     m_max  = largest(b)
#     m_min = minimum(b)
#     res = count - (m_min + m_max)
#     print(name ,"%.2f"%(res*a))
