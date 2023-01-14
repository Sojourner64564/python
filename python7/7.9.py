s = input('')               #ввод слова     
n = int(input(''))          #ввод цифр
if (0 < n <= len(s)):       
   print(s[n-1])
else:
   print('ОШИБКА')

