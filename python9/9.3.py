n = list()
for i in range(int(input())):
   n.append(input())
num = int(input())
for text in n:
   if num <= len(text):
       print(text[num - 1], end='')

