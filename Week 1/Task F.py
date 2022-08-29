input_F = list(map(int, input().split(" ")))

a_1 = input_F[0]
b_1 = input_F[1]

a_2 = input_F[2]
b_2 = input_F[3]

dct = {}
dct['comb_1'] = [(a_1+a_2) , max(b_1, b_2)]
dct['comb_2'] = [(a_1 + b_2) , max(a_2, b_1)]
dct['comb_3'] = [(b_1 + a_2) , max(b_2, a_1)]
dct['comb_4'] = [(b_1+b_2) , max(a_2, a_1)]

for key in dct.keys():
  result = 1
  for i in dct[key]:
    result = result * i
  dct[key].append(result)

min = dct['comb_1'][2]
ideal_params = [dct['comb_1'][0], dct['comb_1'][1]]
for key in dct.keys():
  if dct[key][2] < min:
    min = dct[key][2]
    ideal_params = [dct[key][0], dct[key][1]]

print(ideal_params[0], ideal_params[1])
