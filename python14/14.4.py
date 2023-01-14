def who_are_you_and_hello():
    name = input()
    while not name.isalpha() or not name.istitle():             #если первая буква не заглавная и есть какие либо символы, программа не выведет его как name
        name = input()
    print(f'Привет, {name}!')
