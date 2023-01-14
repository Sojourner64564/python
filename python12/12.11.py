a = int(input())
s = []
for i in range(a):
   b = input().split()
   for j in range(len(b)):
       c = int(b[0])
       d = int(b[-1])
       if c > d:
           s.append(c)
           b.pop(0)
       else:
           s.append(d)
           b.pop(-1)
   w = s[:]
   w.sort(reverse=True)
   if s == w:
       print(*s)
   else:
       print('НЕТ')
   s = []
   w = []
