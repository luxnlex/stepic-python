num = int(input())
i = 1
j = 1
n = 0
br = 0
while i <= num:
    j = 1
    n += 1
    while j <= n:
        if (br == num):
            break
        print(n, end=' ')
        br+=1
        j+=1
    i+=1