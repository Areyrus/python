
n = int( input())
max_values = []
while name := input(""):
        record = list(map(int, name.split()))
        max_value = max(record)
        max_values.append(max_value)
print(";" .join(str(x) for x in sorted(max_values[0:n], reverse=True)))
