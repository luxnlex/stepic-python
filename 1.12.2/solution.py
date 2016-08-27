a = float(input())
b = float(input())
c = input()
if (((b==0) or (b==0.0)) and ((c=='mod') or (c=='div') or (c=='/'))):
    print("Деление на 0!")
else:
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        print(a/b)
    elif c == 'mod':
        print(a%b)
    elif c == 'div':
        print(a//b)
    elif c == 'pow':
        print(pow(a,b))