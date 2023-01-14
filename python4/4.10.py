for i in range(0, 17):        #перебирает числа от 0 до 16
   a = int(input())
   if i % a == 0:             #проверяет на остаток от деления 
       print('ДА')
   else:
       print('НЕТ')

