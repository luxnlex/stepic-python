A = int(input())
B = int(input())
H = int(input())
if ((H>=A) and (B>=H)):
    print("Это нормально")
elif (A>H):
    print("Недосып")
else:
    print("Пересып")