
n = int(input())
max_values = []
while name := input(""):
#    for _ in range(n):
#        record = list(map(int,input().split()))
        record = list(map(int, name.split()))
#        print(record)
        max_value = max(record)
#        print(max_value)
        max_values.append(max_value)
#        print(max_values)
    #continue
print(";" .join(str(x) for x in sorted(max_values[0:n], reverse=True)))
