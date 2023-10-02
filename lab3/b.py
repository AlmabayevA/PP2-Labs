a = input()
j = [int(a) for a in a.split()]
for i in j:
    if int(i)%2 == 0:
        print(i)