n = set()
name = input("")
for x in name:
  n.add(x.lower())
print(" " .join(str(a) for a in sorted(list(n))))