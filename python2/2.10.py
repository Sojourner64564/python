firstStr = float(input("Введите число"))      #1 строка
secondStr = float(input("Введите число"))     #2 строка
thirdStr = str(input("Введите строку"))       #3 строка
if "-" in thirdStr:                  #если в строке встречается "-" - 1 строка - 2 строка
  firstStr -= secondStr
  print(firstStr)
elif("+" in thirdStr):               #если в строке встречается "+" - 1 строка + 2 строка 
  firstStr += secondStr
  print(firstStr)
elif("*" in thirdStr):               #если в строке встречается "*" - 1 строка * 2 строка
  firstStr *= secondStr
  print(firstStr)
elif("/" in thirdStr):               #если в строке встречается "*" - 1 строка / 2 строка
  firstStr /= secondStr
  print(firstStr)
else:
  print("888888888")
