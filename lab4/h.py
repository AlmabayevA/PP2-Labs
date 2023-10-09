n = int(input())
all_nums = set(range(1, n+1))

while True:
    possible = input()
    if possible == 'HELP':
        break
    possible = set(int(x) for x in possible.split())
    if len(all_nums & possible) > len(all_nums) / 2:
        print('YES')
        all_nums &= possible
    else: 
        print('NO')
        all_nums &= all_nums - possible

print(sorted(all_nums))