lst = [int(i) for i in input().split()]
x = int(input())
c = 0
for i in range(len(lst)):
  if lst[i]==x:
    print(i)
    c+=1
if c<1:
  print("Отсутствует")