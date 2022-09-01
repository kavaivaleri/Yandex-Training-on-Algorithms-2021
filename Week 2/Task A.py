# A. Возрастает ли список?

lst = list(map(int, input().split(" ")))

max1 = lst[0]
cnt = 0

for i in lst[1:]:
    while i > max1:
        max1 = i
        cnt += 1

if cnt == len(lst)-1:
    print('YES')
else:
    print('NO')
