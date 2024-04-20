#My Method
# num = int(input("Enter the number: "))

# num_digits = 0

# a = []

# while num > 0:
#     a.append(num%10)
#     num = num//10
#     num_digits += 1

# print("List: ", a[:])

# is_palindrome = True

# for j in range(0, len(a)):
#     if(a[len(a) - 1 - j] - a[j] != 0):
#         is_palindrome = False

# print("Palindrome? : ", is_palindrome)

#GFG method - Less space complexity
num = int(input("Enter the number: "))

#variable to hold the reverse of the number
rev_num = 0
temp = num

while temp > 0:
    rightmost_digit = temp%10
    rev_num = rev_num * 10 + rightmost_digit
    temp = temp//10

if rev_num == num:
    print("Palindrome")
else:
    print("Not a palindrome")
