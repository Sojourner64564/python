temp = float(input())
days = 0
while temp <22:  #пока температура ниже 22 цикл будет постоянно повторяться
  days +=1
  temp = float(input())
print(days // 7)    # показывает какой день в недели температура была <=22
