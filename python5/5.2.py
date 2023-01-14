numbers = int(input())
flag = False
for i in range(numbers + 1):        #переборка с диапозоном 0-numbers
words = input()                 #текст
if "кот" in words:            #поиск слова в тексте
flag = True                   
break
if flag == 1:                 #проверка если в слове присутвовало слово кот выведет мяу 
print("Мяу")
else:
print("Не мяу")
