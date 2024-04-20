def isSorted(l):
    #Note -  Return sorted if the length is 1 or 0

    if len(l) > 1:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                return "Unsorted"
        return "Sorted"
    else:
        return "Sorted"
    
l = [1, 5, 5, 2, 8]

print(isSorted(l))