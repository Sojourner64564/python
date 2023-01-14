def letter(name, pl, d, email):
    return f'''To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {pl}е, которая пройдет {d}.'''


place = 'Neftekamsk'
name = 'Ildar'
date = '28.12.22'
email = 'VenomFeed@mail.ru'
print(letter(name, place, date, email))
name = 'Aibulat'
email = 'medmeFord@mail.ru'
print(letter(name, place, date, email))