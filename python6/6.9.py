n = int(input())                      #вводится кол-во продуктов
prods = set([input() for _ in range(n)])      #вводится продукты в кол-ве указанные пользователем
n = int(input())            #число рецептов

recs = []
for _ in range(n):
   dct = {}
   key, kol = input().split()
   dct[key] = [input() for _ in range(int(kol))]
   recs.append(dct)

print()

for rec in recs:
   [print(key) for key, value in rec.items() if set(value).issubset(prods)]

