# C. Ближайшее число

n = int(input())
lst = list(map(int, input().split(" ")))
x = int(input())

diff = {}

for i in range(len(lst)):
    if i not in diff:
        diff[i] = 0
    
    if lst[i]-x<0:
        diff[i] = -(lst[i]-x)
    else:
        diff[i] = lst[i]-x

ans = i

for key in diff:
    if diff[key]<diff[ans]:
        ans = key
print(lst[ans])
