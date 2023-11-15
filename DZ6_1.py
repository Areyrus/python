a = input()
i = 0
for n in a:
    if n == "!" or n == "%" or n == "#" or n == "@":
        i +=1
        a=a.replace(n,"")
print(i)
print(a.lower())