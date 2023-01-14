numbers = int(input())
n = 0
flag = False
for i in range(numbers + 1):          #перебирает в диапозоне 0-n
  words = input()                     #вводится слова
  if "кот" or "Кот" in words:         #если они есть внутри вводимого слова цикл останавливается
    flag = True   
    break           
if flag == 1:
  print("МяУ")
else:
  print("не мяу")
