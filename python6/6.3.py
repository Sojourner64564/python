a = int(input())                  # кол-во людей изучающие англ
b = int(input())                  # кол-во людей изучающие немец
list1 = set()                     #создание листа 1
list2 = set()                     #создание листа 2
c = 0
for v in range(a):                     #вводится ученики изучающие анг
   c = input()
   list1.add(c)                        #добавляют в лист значения
for n in range(b):                     #вводится ученики изучающие немец
   s = input()
   list2.add(s)                        #добавляют в лист значения
count = len(list1 ^ list2)             #проверка на повторение учеников
print(count if count > 0 else 'NO')

