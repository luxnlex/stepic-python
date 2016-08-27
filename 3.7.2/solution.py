known = set()
unknown = set()

for _ in range(int(input())):
    known.add(input().strip().lower())

for _ in range(int(input())):
    for word in input().strip().lower().split():
        if word not in known:
            unknown.add(word)

for word in unknown:
    print(word)