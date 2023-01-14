
a = input().lower()
z = []
for char in set(a):
   z.append(a.count(char))
print(max(z))
