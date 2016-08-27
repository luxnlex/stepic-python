a = int(input())
b = int(input())
c = int(input())
d = int(input())
for t in range(c,d+1):
    if(t!=c):
        print(t,end='\t')
    else:
        print(end='\t')
        print(t,end='\t')
    
print(end='\n')

for i in range(a, b+1):
    print(i,end='\t')
    for j in range(c, d+1):
        if (j==d+1):
            print(i*j,end='\t\n')
        else:
            print(i*j,end='\t')
    print(end='\n')