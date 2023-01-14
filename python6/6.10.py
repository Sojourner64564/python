menu = set()             #создвние листа мненю
use_menu = set()             #создание листа меню
menu_not_use = set()             #создание листа меню
menu_N = int(input())           #число блюд которые может приготовить столовая
for i in range(menu_N):
   menu.add(input())
day_menu_true = int(input())
for i in range(day_menu_true):
   menu_in_day_N = int(input())
   for j in range(menu_in_day_N):
       use_menu.add(input())
menu_not_use = menu - use_menu
print(*menu_not_use, sep='\n')
