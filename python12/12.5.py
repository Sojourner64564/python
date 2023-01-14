a = []
c = int(input()[1:])
for i in range(c):
   b = str(input())
   if '#' in b:
       f = b.index('#')
       b = ''.join(b[:f])
   a.append(b)
for i in range(len(a)):
   print(a[i].rstrip())

