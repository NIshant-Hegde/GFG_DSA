num = int(input("Enter the number: "))
digits = 0

while num > 0:
    num = num//10
    print(num)
    digits += 1

print("Number of digits: ", digits)