def space_game(name):
   space = name.count(' ')
   if space %2 == 0:
       print('u win')
   else:
       print('u losse')


s = input()
space_game(s)
