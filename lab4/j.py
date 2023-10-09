N, K = [int(i) for i in input().split()]

s = [[int(i) for i in input().split()] for i in range(K)]
d = set()
for i in range(K):
    for j in range(s[i][0], N+1, s[i][1]):
        if j % 7 != 0 and j % 7 != 6:
            d.add(j)
print (len(d))            