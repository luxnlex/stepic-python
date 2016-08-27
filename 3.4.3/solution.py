with open('D:/SRC/Stepic/Python/tmp/dataset_3363_4.txt') as f:
    strings = [s.rstrip() for s in f.readlines()]
evaluation = [s.split(';')[1:] for s in strings]
for x in evaluation:
    print(sum(map(int, x))/len(x))
average_math = sum([int(x[0]) for x in evaluation])/len(evaluation)
average_fhyz = sum([int(x[1]) for x in evaluation])/len(evaluation)
average_rus = sum([int(x[2]) for x in evaluation])/len(evaluation)
print(average_math, average_fhyz, average_rus)