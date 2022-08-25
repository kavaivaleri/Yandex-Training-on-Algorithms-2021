# Solution 1
input_Vasya_taskC = input()
input_1_taskC = input()
input_2_taskC = input()
input_3_taskC = input()

dct = {}
dct['Vasya'] = input_Vasya_taskC
dct['num1'] = input_1_taskC
dct['num2'] = input_2_taskC
dct['num3'] = input_3_taskC

dct2 = {}
dct2['Vasya'] = []
dct2['num1'] = []
dct2['num2'] = []
dct2['num3'] = []

for key in dct.keys():
  for i in dct[key]:
    if i != '-' and i != '(' and i != ')':
      dct2[key].append(i) 

for key in dct2.keys():
  if dct2[key][0] == '8' and len(dct2[key]) > 7:
    dct2[key] = dct2[key][1:]
  if dct2[key][0] == '+' and dct2[key][1] == '7' and len(dct2[key]) > 7:
    dct2[key] = dct2[key][2:] 
  if len(dct2[key]) == 7:
    dct2[key].insert(0,'5')
    dct2[key].insert(0,'9')
    dct2[key].insert(0,'4')

new_num1 = []
for i in range(len(dct2['Vasya'])):
  if dct2['Vasya'][i] == dct2['num1'][i]:
    new_num1.append(i)

if len(new_num1) < len(dct2['Vasya']):
  print('NO')
else:
  print('YES')

new_num2 = []
for i in range(len(dct2['Vasya'])):
  if dct2['Vasya'][i] == dct2['num2'][i]:
    new_num2.append(i)

if len(new_num2) < len(dct2['Vasya']):
  print('NO')
else:
  print('YES')

new_num3 = []
for i in range(len(dct2['Vasya'])):
  if dct2['Vasya'][i] == dct2['num3'][i]:
    new_num3.append(i)

if len(new_num3) < len(dct2['Vasya']):
  print('NO')
else:
  print('YES')
