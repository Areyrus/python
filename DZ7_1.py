n = input()
i = (n.split(" "))
print(f"{sum([len(a) for a in i])/len([len(a) for a in i])}")
