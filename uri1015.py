import math

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
line = str(input(""))
split = line.split()

line2 = str(input(""))
split2 = line2.split()

x1 = float(split[0])
y1 = float(split[1])
x2 = float(split2[0])
y2 = float(split2[1])
dis = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
print("%.4f" % dis)
