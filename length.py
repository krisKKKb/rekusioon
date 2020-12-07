def length(l):
    if not l:
        return 0
    else:
        return length(l[1: ]) + 1
print(length("Ametikool"))
