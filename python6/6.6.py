M = int(input())        #книга на лето
N = int(input())        #книга в наличии
bookForSummer = []           #книга на лето
haveInLibrary = []               #книга в наличии
for i in range(N):
  book = input()
  bookForSummer.append(book)       #добавляются название книг на лето указанные пользователем 
for i in range(M):
  book = input()
  haveInLibrary.append(book)         #добавляются название книг в библеотеке указанные пользователем 

if book in haveInLibrary:
        print('YES')
    else:
        print('NO')

