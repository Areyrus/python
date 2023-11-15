a = input()
o = False
i = True
for n in a:
    if n == "a" or n == "o":
        o = True
    elif n == "i" or n == "e" :
        i = False
print(o and i )
