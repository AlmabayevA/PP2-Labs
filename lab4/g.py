n= int(input())
a = [k for k in range(n)]
s = set(a)

while True:
    num = input()
    if num == 'HELP':
        break
    answer = input()
    if answer == 'NO':
        s -= set(num.split())
    elif answer == 'YES':
        s &= set(num.split())
print(*s)       