s = str(input())
c = 1
p = 1
ns = s[p:p+1]
for i in s:
    if i in ns:
        c += 1
    else:
        print(i, end='')
        print(c, end='')
        c = 1
    p += 1
    ns = s[p:p+1]