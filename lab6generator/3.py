def generator(n):
    i = 0
    while i<=n:
        if i%3 == 0 and i%4 ==0:
            yield i
        i+=1


n = int(input())
values = []
for i in generator(n):
    values.append(str(i))

print (','.join(values))