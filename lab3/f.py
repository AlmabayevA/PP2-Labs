a = [int(i) for i in input().split()]
max = a[0]
index= 0
for i in range(1, len(a)):
    if (a[i] > max):
        max = a[i]
        index = i
print(a[i], index)