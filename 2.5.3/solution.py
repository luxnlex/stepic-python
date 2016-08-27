s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
c = 0
ns = []
for j in range(len(s)):
    if (s.count(s[j])>1):
        if ((s[j] in ns) == 0):
            ns.append(s[j])
for k in ns:
    print(k,end=' ')