n = int(input())
ar = [[0 for i in range(n)] for j in range(n)]
cnt=2
i=0
j=0
ar[0][0]=1
while cnt<=n**2:
    if (j+1)<=(n-1) and ar[i][j+1]==0:
        j+=1
        ar[i][j]=cnt
        cnt+=1
    elif (i+1)<=(n-1) and ar[i+1][j]==0:
        i+=1
        ar[i][j]=cnt
        cnt+=1
    elif (j-1)>=0 and ar[i][j-1]==0:
        j-=1
        ar[i][j]=cnt
        cnt+=1
    else:
        while ar[i-1][j]==0:
            i-=1
            ar[i][j]=cnt
            cnt+=1
s=''
for i in range(n):
    for j in range(n):
        s+=str(ar[i][j])+' '
    s+='\n'
print(s)