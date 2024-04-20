#Demonstration of list comprehensions

def getSmallerThan(l, ele):
    return [x for x in l if x < ele]

def seperateEvenOdd(l):
    return [x for x in l if x%2==0], [x for x in l if x%2!=0]

l = [10, 20, 30, 45, 50]

getSmallerList = getSmallerThan(l, 40)
evenList, oddList = seperateEvenOdd(l)

print("getSmallerList: ", getSmallerList)
print("evenList: ", evenList)
print("oddList: ", oddList)

