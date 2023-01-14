chars = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

nik_name = list(input())

for i in nik_name:
   if i != i.upper() or i in chars:
       pass
   else:
       print('Неверный символ:', i)
       break
else:
   print('Ok')

