s = []
sum = 0
sqSum = 0

while(True):
    curInput = input()
    sum+=int(curInput)
    if (sum==0):
        s.append(curInput)
        break
    s.append(curInput)

for i in range(len(s)):
    sqSum+=int(s[i]) ** 2
print(sqSum)