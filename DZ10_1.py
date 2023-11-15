name = input().split()
#names = name.lowersplit(" ")
d = {}
for x1 in name:
    n = 0
    for x2 in name:
        if x1.lower() == x2.lower() :
            n += 1
            d[x1.lower()] = n
#print(d)
#print(max(d.values()))
max = max(d.values())
for a, b in d.items():
    if d[a] == max:
        print(a,b)


