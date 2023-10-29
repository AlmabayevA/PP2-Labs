def generator(n):
    
 for i in range(m, n):
            yield i * i
    

m = int(input())
n = int(input())
values = []
for i in generator(n):
    values.append(str(i))

print (','.join(values))

