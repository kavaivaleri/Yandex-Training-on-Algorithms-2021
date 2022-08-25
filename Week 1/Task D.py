a = int(input())
b = int(input())
c = int(input())

if a == 0 and (b ** 0.5) != c:
  print('NO SOLUTION')

elif c < 0:
  print('NO SOLUTION')

elif a == 0 and (b ** 0.5) == c:
  print('MANY SOLUTIONS')

elif a == 0 and b == 0 and c == 0:
  print('MANY SOLUTIONS')

elif (((c**2) - b) / a) % 1 == 0:
  print(int(((c**2) - b) / a))

elif (((c**2) - b) / a) % 1 != 0:
  print('NO SOLUTION')
  
