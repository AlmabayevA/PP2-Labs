
def generator(n):
    for i in range(n):
        yield i * i
n = int(input())
for item in generator(n):
    print(item)