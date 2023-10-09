n = int(input())

lang = []
for _ in range(n):
    k = int(input())
    buff = set()
    for _ in range(k):
        buff.add(input())
        lang.append(buff)

unic = set.union(*lang)
intersec = set.intersection(*lang)
sep = '\n'
print(len(intersec))
print('\n'.join (sorted(intersec)))
print (len(unic))
print ('\n'.join(sorted(unic)))