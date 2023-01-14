last = ''
counter = 0
n = int(input())
flag = False
for i in range(n):          #переборка от 0 до n-1
   words = input().lower()        #вводится слова
   if 'кот' in words:         #если слово кот присутсвует в словах выводит true
       flag = True
   if 'пёс' in words:         #если найден ещё и пес то значени возвращается в false
       flag = False
if flag:
   print('МЯУ')
else:
   print('НЕТ')

