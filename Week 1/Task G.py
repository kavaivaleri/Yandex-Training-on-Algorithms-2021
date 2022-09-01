# G. Детали

lst = [int(i) for i in input().split()]
n, k, m = lst[0], lst[1], lst[2]

if n%k == 0:
    print((n//k)*(k//m))
else:
    result = (n//k)*(k//m)
    n = n%k + (k%m)*(n//k)
    
    while n >= k:
        result += (n//k)*(k//m)
        n = n%k + (k%m)*(n//k)
    print(result)
