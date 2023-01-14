n = list()
for _ in range(int(input())):
   n.append(int(input()))
r = int(input())
r_action = False
for i in n:
   b = r // i
   if b in n:
       if not b == i:
           r_action = True
           break
if r_action is True:
   print('Да')
else:
   print('Нет')

