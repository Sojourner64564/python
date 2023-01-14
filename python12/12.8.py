string = input()
letter = []
letterM = []
big = 0
let = ''
for i in string:
   if i != ' ':
       letter.append(i.lower())
       letterM.append(i.lower())
letterM.sort()
for i in letterM:
   if letter.count(i) > big:
       big = letter.count(i)
       let = i
print(let)


