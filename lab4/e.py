a, b = ([int(i) for i in input().split()])

c, d = set(), set()
for i in range (a):
    c.add(int(input()))
for i in range(b):
    d.add(int(input()))

print (len(c&d))
print(*sorted(c&d))
print (len(c-d))
print(*sorted(c-d))
print (len(d-c))
print(*sorted(d-c))
