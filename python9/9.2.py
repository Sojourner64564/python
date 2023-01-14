n = list()
for i in range(int(input())):
   n.append(input())
search = input()
for text in n:
   if search in text:
       print(text)

