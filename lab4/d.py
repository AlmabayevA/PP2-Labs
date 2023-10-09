a = [int(i) for i in input().split()]
##b = set()
for i in range (len(a)):
    if a[i] in a[:i]:
        print('YES')
    else:
        print('NO')
       