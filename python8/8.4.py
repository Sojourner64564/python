n = int(input())
start = ord('A')
for i in range(n)[::-1]:
   print(*[f'{chr(start + j) }{i+1}' for j in range(n)])

