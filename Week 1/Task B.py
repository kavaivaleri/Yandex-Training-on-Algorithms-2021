a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < b + a:
  print('YES')

else:
  print('NO')
  
