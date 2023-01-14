firstCity = input("Выберете город в котором Женя будет в Июле")    #первый город
secondCity = input("Выберете город в котором Женя будет в Августе")   #второй город
if(firstCity == "Пенза" and secondCity == "Тула")or(firstCity == "Тула" and secondCity == "Пенза"):   #если первый город пенза или тула, а второй тула или пенза - то выводит "No"
  print("No")                                                                                         
elif(firstCity == "Пенза" and secondCity != "Пенза")or(firstCity == "Тула" and secondCity != "Тула"): #если первый город пенза или тула, а второй не тула и не пенза - то выводит "yes"
  print("yes")
