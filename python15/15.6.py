def print_document(pages):
    f = False
    for i in pages:
        if "Секретно" not in i:
            print(i)
        else:
            f = True
            break
    if not f:
        print("Напечатано без купюр")
    else:
        print('Дальнейшие материалы засекречены')
