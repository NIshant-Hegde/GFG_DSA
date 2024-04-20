def LeftRotate(l, n):
    temp = []

    for j in range(0, n):
        temp.append(l[j])
    
    for i in range(n, len(l)):
        l[i - n] = l[i]

    loop_counter = 0
    for k in range(len(l) - n, len(l)):
        l[k] = temp[loop_counter]
        loop_counter += 1
    
    return l

l = [1, 2, 3, 4, 5]
print(LeftRotate(l, 3)) #Left rotate by 3