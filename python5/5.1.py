
firstNumbers = int(input())                       
secondNumbers = int(input())
for i in range(firstNumbers, secondNumbers + 1):         #перебирает значения от 1 до 2 введённого числа
    if i % 3 == 0 and i % 5 == 0:
        print(i - 1)
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
        print(i + 1)
    elif i % 5 == 0:
        print('Buzz')
        print(i + 1)
