word = ''
n = 0
cat = -1
i = 1
while word != 'СТОП':      #переборка пока не встретится стоп
   word = input().lower()
   if 'кот' in word:              #если встретится ... увеличивает число n на 1
       n += 1
   if ('кот' in word) and cat == -1:    #если существует слово с котом выводит первое соприкосновение
       cat = i
   i += 1
print(n, cat)
