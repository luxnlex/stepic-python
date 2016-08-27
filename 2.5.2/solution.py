s = input().split()
ns = []
for i in range(0,len(s)):
    if (len(s)==1):
        ns.append(int(s[i]))
    elif (i==0):
        ns.append(int(s[len(s)-1])+int(s[i+1]))
    elif (i==len(s)-1):
        ns.append(int(s[i-1])+int(s[0]))
    else:
        ns.append(int(s[i-1])+int(s[i+1]))
for j in ns:
    print(j,end=' ')