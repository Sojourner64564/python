strings = [input()]            #создание массива
i = 0
while strings[i] != 'СТОП':       #пока не появится СТОП цикл будет запускаться  
  strings.append(input())           #добавляет в массив слово
  i += 1
  for n in range(len(strings)):    #перебирает подсчитывает длинну массива
    if 'кот' in strings[n]:        #если попадается кот
      print(n + 1)                 #указать место нахождения
      break
    else:
     print(-1)
