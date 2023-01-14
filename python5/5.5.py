strings = [input()]                   #создание массива
i = 0
while strings[i] != 'СТОП':           #цикл будет продолжаться пока не встретится стоп
  strings.append(input())             #добовляет значения в массив
  i += 1
  for n in range(len(strings)):       #переборка значений в диапозоне длинны массива
    if 'кот' in strings[n]:
      print(n + 1)
      break
    else:
      print(-1)
