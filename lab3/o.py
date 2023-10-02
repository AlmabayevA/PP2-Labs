a = [i for i in range(1, int(input() ) + 1)]
k = int(input())
c = []
for i in range(k):
    x = int(input())
    y = int(input())
    for j in range(x, y + 1):
        c.append(j)

for i in range(len(a)):
    if a[i] in c:
        print('.', end='')
    else:
        print('I', end='')