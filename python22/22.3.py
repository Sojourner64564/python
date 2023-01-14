import string
from random import choices

letters = list(string.ascii_letters)
del (letters[letters.index('O')], letters[letters.index('o')], letters[letters.index('l')],
     letters[letters.index('I')])
numbers = list(string.digits)
del (numbers[numbers.index('0')], numbers[numbers.index('1')])
all_lists = letters + numbers


def main(n, m):
    list1 = []
    for _ in range(n):
        a = generate_password(m)
        if a in list1:
            while a in list1:
                a = generate_password(m)
        list1.append(a)
    return list1


def generate_password(m):
    return ''.join(choices(all_lists, k=m))


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")