a = int(input())            #кол-во людей
mean = int(input())         #iq 1
print(0)
for n in range(1, a + 1):         #перебирает n от 1 до а
   b = int(input())         #iq 2
   if b > mean:
       print('>')
   elif b < mean:
       print('<')
   else:
       print(0)
   mean = (mean * n + b) / (n + 1)   


