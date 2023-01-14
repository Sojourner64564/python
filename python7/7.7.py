word = input()
s=''
for i in word:
   s=s+str(ord(i))+', '
print(s[:-2])

