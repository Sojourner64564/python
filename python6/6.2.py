n = int(input())                    #вводится число городов
s = set()                           #вводится города
c = 0
k = 0
while k == 0:
   if c == n:
       d = input()              #новый город
       break
   else:
       a = input()               #новый города
   c = c + 1            
   s.add(a)                       #добавляет внутрь листа новый город
if d not in s:                   #если нового города нет в списке выводит ok
   print('OK')
else:
   print('TRY ANOTHER')
