a = int(input())
b = int(input())
if a>=b:
    c=b
else:
    c=a
while (c%a)!=(c%b):
    c=c+1
print(c)