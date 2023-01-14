a = int(input())              #кол-во людей изучающих анг
b = int(input())              #кол-во людей изучающих немец
c = set()              #создание лист 1
d = set()              #создание лист 2
for i in range(a + b):  #переборка от а до b-1
    name = input()      #вводятся фама
    if name in c:
        d.add(name)
    else:
        c.add(name)
difference = c - d      #вывдит кол-во учеников изучающих один язык
if not difference:
    print('NO')
else:
    print(len(difference))
