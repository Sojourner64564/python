list1 = set()       #создание 1 листа
list2 = set()       #создание 2 листа

n = int(input())          #группы языков
n += int(input())          #группы языков
n += int(input())          #группы языков

for i in range(n):     #переборка до n-1
   name = input()           #ввод фамилий
   if not name in list1:    #проверка на присутвие однофамильцев
       list11.add(name)
   else:
       if not name in list2: #проверка на присутвие однофамильцев
           list2.add(name)
       else:
           list2.remove(name)
print(len(list2) if list2 else 'NO')        #Вывод кол-во людей изующих 2 языка или no в случае их отсутвия

