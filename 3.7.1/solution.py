s=str(input())
a=[]
for i in range(len(s)):
    si=s[i]
    a.append(si)
b=[]
n=str(input())
for j in range(len(n)):
    sj=n[j]
    b.append(sj)
p={}
for pi in range(len(s)):
    key=s[pi]
    p[key]=0
j1=0
for i in range(0,len(a)):
    key=a[i]
    while j1<len(b):
        bj=b[0]
        if key in p:
            p[key]=bj
        b.remove(bj)
        break
c=[]
si=str(input())

for si1 in range(0,len(si)):
    ci=si[si1]
    c.append(ci)

co=[]

for ci in range(0,len(c)):
    if c[ci] in p:
        cco=c[ci]
        pco=p[cco]
        co.append(pco)

d=[]

di=str(input())

for sj1 in range(0,len(di)):
    dj=di[sj1]
    d.append(dj)

do=[]

for di in range(0,len(d)):
    for key in p:
        pkey=key
        if p.get(key) == d[di]:
            ddo=pkey
            do.append(ddo)

for i in range (0,len(co)):
    print(co[i],end='')
print()

for j in range (0,len(do)):
    print(do[j],end='')