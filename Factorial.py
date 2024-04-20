num = int(input("Enter the number: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
print("Factorial: ", factorial(num))