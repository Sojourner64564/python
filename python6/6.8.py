men = int(input())              #кол-во м сотрудников
men_works = [input() for _ in range(men)]         #переборка кол-ва м и запись их фамилий
result = 0
for example in set(men_works):        
   cout = 0
   for name in men_works:                         
       if example == name:      #проверка на повторение
           cout += 1
   if cout > 1:
       result += cout         #вывод кол-во повторяющихся фамилий 
print(result)

