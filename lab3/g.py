a = [int(i) for i in input().split()]
b = int(input())

for i in range(len(a)):
    if b > a[i]:
        print(i+1)
        break
    elif i == len(a) - 1:
        print (len(a) + 1)