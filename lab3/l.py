a = [int(i) for i in input().split()]

k= int(input())
c = int(input())

b = []
for i in range(len(a)):
    if i == k:
        b.append(c)
    b.append(a[i])

print (' ' .join (str(i) for i in b ))         
