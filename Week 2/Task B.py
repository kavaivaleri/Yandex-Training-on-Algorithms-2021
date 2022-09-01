# B. Определить вид последовательности

a = int(input())

start = a
lst = []

while a != -2000000000:
    a = int(input())
    if a > start:
        lst.append(0)
        start = a
    elif a < start:
        lst.append(1)
        start = a
    else:
        lst.append(2)
        start = a

lst=lst[:-1]

if lst.count(0) == len(lst):
    print('ASCENDING')
elif lst.count(1) == len(lst):
    print('DESCENDING')
elif lst.count(2) == len(lst):
    print('CONSTANT')
elif lst.count(2) == len(lst)-lst.count(1):
    print('WEAKLY DESCENDING')
elif lst.count(2) == len(lst)-lst.count(0):
    print('WEAKLY ASCENDING')
else:
    print('RANDOM')
    
