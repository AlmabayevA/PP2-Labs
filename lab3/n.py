a = list(map(int, input().split()))
flag = True
b = []
for i in range(len(a)):
    for j in range(i + 1,len(a)):
        if a[i] == a[j]:
            b.append(a[i])

for i in range(len(a)):
    if a[i] not in b:
        print(a[i], end= ' ')
