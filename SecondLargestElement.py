def SecondLargestElement(l):
    largest = l[0];
    secondLargest = None;

    if len(l) <= 1:
        return None

    for i in range(1, len(l)):
        if l[i] > largest:
            secondLargest = largest
            largest = l[i]
        elif l[i] != largest:
            if secondLargest == None or secondLargest < l[i]:
                secondLargest = l[i]

    return secondLargest

l = [50, 10, 30, 40, 20]

print(SecondLargestElement(l))