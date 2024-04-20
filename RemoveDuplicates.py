#Removing duplicates from a sorted array.
def RemoveDuplicates(l):
    duplicate_indices = []
    out = []

    if len(l) > 1:
        for i in range(1, len(l)):
            if l[i - 1] == l[i]:
                duplicate_indices.append(i)

        for i in range(0, len(l)):
            if i not in duplicate_indices:
                out.append(l[i])
        
        return out
    else:
        return l
    
l = [10, 20, 20, 30, 40, 50, 50]
print(RemoveDuplicates(l))