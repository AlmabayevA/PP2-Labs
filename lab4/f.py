a = int(input())
b = set()

for i in range(a):
    b|= set(input().split())

print (len(b))    