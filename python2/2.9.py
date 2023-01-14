firstHight = str(input())    #1
secondHight = str(input())   #2
thirdHight = str(input())    #3

 

if firstHight > secondHight and secondHight > thirdHight:   #если 1>2 и 2>3 выведет в последовательности 123
print(firstHight)
print(secondHight)
print(thiraaignt)

elif firstHight > thirdHight and thirdHight > secondHight:  #если 1>3 и 3>2 выведет в последовательности 132
print(firstHight)
print(thirdHight)
print(secondHight)

elif secondHight > firstHight and firstHight > thirdHight:  #если 2>1 и 1>3 выведет в последовательности 213
print(secondHight)
print(firstHight)
print(thirdHight)

elif secondHight > thirdHight and thirdHight > firstHight:  #если 2>3 и 3>1 выведет в последовательности 231
print(secondHight}
print(thirdHight)
print(firstHight)

elif thirdHight > secondHight and secondHight > firstHight: #если 3>2 и 2>1 выведет в последовательности 321
print(thirdHight)
print(secondHight)
print(firstHight)

elif thirdHight > firstHight and firstHight > secondHight:  #если 3>1 и 1>2 выведет в последовательности 312
print(thirdHight)
print(firstHight)
print(secondHight)
