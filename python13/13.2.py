nomera = {}

for i in range(int(input())):
   noomer = input().split()
   if noomer[1] not in nomera:
       nomera[noomer[1]] = []
   nomera[noomer[1]].append(noomer[0])

for i in range(int(input())):
   name = input()
   if name in nomera:
       print(*nomera[name])
   else:
       print('Нет в телефонной книге')


