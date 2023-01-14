firstQuestion = input("Любите ли вы котиков")   #первый вопрос
if(firstQuestion == "да"):    
  print("я тоже!")                              
elif(firstQuestion == "нет"):
  print("а я люблю")
else:
  print("ERROR, нужно ответить да или нет")     #выводит ошибку и просит пользователя ввести нужные данные
secondQuestion = input("Умеете ли вы программировать") #второй вопрос
if(secondQuestion == "да"):
  print("это прекрасно!")
elif(secondQuestion == "нет"):
  print("Как жаль!, но у вас ещё есть время научиться!")
else:
  print("ERROR, нужно ответить да или нет")
 
