import sys

s = ''
for i in range(1,len(sys.argv)):
    s+=sys.argv[i]+' '
print(s,end=' ')