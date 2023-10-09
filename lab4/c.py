a = {int(i) for i in input().split()}
b = {int(j) for j in input().split()}

c = a&b
print(' '.join(set(map(str, c))))
 
