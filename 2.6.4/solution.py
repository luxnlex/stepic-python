string = m = []
while string != 'end':
    string = input()
    m.append(list(map(int, string.split(' ')))) if string != 'end' else None
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
[print(' '.join(map(str, row))) for row in new]