a = input().split()
b = input().split()
m = int(b[0])
k = int(b[1])
x = 0
for i in range(m, k + 1):
   x += int(a[i])
print(x)

