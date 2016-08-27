a = int(input())
b = int(input())
n = 0
sum=0
for i in range(a,b+1):
    if (i%3==0):
        n+=1
        sum+=i
print(sum/n)