a = input()                 #вводится слово
words = []                
while a != "стоп":          #пока не встретится строка стоп цикл повторяется
   words.append(a)ё         #добавляет в массив строки ввёденые пользователем
   a = input()
ma, mi = max(words, key=len), min(words, key=len)
if set(ma).issuperset(set(mi)):
   print("ДА")
else:
   print("НЕТ")

