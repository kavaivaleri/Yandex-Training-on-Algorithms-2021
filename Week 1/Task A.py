input_task = list(map(int, input().split(" ")))
t_room = input_task[0]
t_cond = input_task[1]
input_task2 = input()

if input_task2 == 'freeze':
  if t_room <= t_cond:
    print(t_room)
  else:
    print(t_cond)

if input_task2 == 'heat':
  if t_room >= t_cond:
    print(t_room)
  else:
    print(t_cond)

if input_task2 == 'auto':
  if t_room == t_cond:
    print(t_room)
  else:
    print(t_cond)

if input_task2 == 'fan':
    print(t_room)

