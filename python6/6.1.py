list1 = set()                    #создание 1 листа 
list2 = set()                    #создание 2 листа
words = input()
while words != '':               #пока не попадётся пустая строка будет добавлять в лист значения
   list1.add(words)
   words = input()
list1.add(words)
words1 = input()
while words1 != '':              #пока не попадётся пустая строка будет добавлять в лист значения
   list2.add(words1)
   words1 = input()
intersection = list1 & list2        #ищет пересечения между листами
if not intersection:
   print('EMPTY')
else:
   for i in intersection:
       print(i)

