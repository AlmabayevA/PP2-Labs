a = [int(i) for i in input().split()]

max = a.index(max(a))
min = a.index(min(a))

a[min], a[max] = a[max], a[min]
print(' '.join (str(i) for i in a))