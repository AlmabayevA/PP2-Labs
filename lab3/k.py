a = [int(i) for i in input().split()]

k = int(input())

a.pop(k)
print (' '.join(list(map(str, a))))