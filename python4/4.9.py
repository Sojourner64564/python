n = int(input())  
m = n
k = '*'
pi = '**'
d = ' '
for i in range(n):     #перебирает i от 0 до n-1 
   m = m - 1
   d = d * m
   print(d + k)       #создаётся слой
   k = k + pi         #увеличивается след возможный слой
   d = ' '

