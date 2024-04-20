def ReverseList(l):
    if len(l) > 1:
        for i in range(len(l)//2):  #Only traverse till len/2, otherwise it'll return the same list
            temp = l[i]
            l[i] = l[len(l) - 1 - i]
            l[len(l) - 1 - i] = temp
        return l
    else:
        return l
    
#l = [1, 2, 3, 4, 5]
#l = []
l = [1, 2, 3, 4]
print(ReverseList(l))