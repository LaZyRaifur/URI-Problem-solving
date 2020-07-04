array = []
temp = 0
count = 0
for i in range(0, 10):
    i = int(input())
    array.append(i)
for i in range(10):
    for j in range(i + 1, 10):
        if (array[i] > array[j]):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            count += 1
        print("%d" % array[j])
        print(j)
