sum = 0
count = 0
a = int(input())
while a != 0:           #цикл пока пользователь не введёт 0
  sum += a
  if sum <= 10:         #если сумма меньше или равна 10 
    count += 1          #первое соприкосновение
   a = int(input())
 print(count)
