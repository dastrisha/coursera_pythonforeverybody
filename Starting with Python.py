# # Program 1: Printing numbers from 1 to 598
# for i in range(1, 599):
#     print(i)
# print(i)
# print(i+2)
# # print within the scope and outside the scope of for loop
# # the last value of i is intact. Refer line 4 and 5


# # Program 2: Printing even numbers between 1 and 10
# for i in range(2, 11, 2):
#     print(i)

# # Program 2: Printing even numbers between 1 and 10
# for i in range(10, 2, -2):
#     # print(i)

# # Program 3: Sum of numbers in a list
# numbers = [1, 2, 3, 4, 5]
# sum_of_numbers = 0
# for num in numbers:
#     sum_of_numbers += num
# print("Sum of numbers:", sum_of_numbers)

# Program 5: Printing multiplication table of a number
# num = 2
# print("Multiplication table of", num)
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # Program 4: Printing characters in a string
# word = "Python"
# for char in word:
#     print(char)
# # Program 4: Printing characters in a string
# word = "P y t h o n"
# for char in word:
#     print(char, end="\n") 
# num = 7
# print("Multiplication table of", num, end="\n")
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)
# word = "P y t h o n"
# for char in word:
#     if char != " ":  # If the character is not a a space, print a newline
#         print(char, end= "\n")
#     else:
#         print(char, end=" ")  # Print the character not followed by a space
# new_word = "Anaconda"
# print (new_word)

# for char in new_word:
#     print (char, end= " ")

# new_word = "Python"
# spaced_word = ""
# for char in new_word:
#     spaced_word += char + " "
# print(spaced_word)

# fruits = ["apple", "banana", "cherry"]
# str = ""
# for fruit in fruits:
#     str += fruit + " "
# print(str)

 #Python practice problems involving input, type conversion, and basic operators:

#Addition of Two Numbers:

# number1 = int(input("add first number: "))
# number2 = int(input("add second number here: "))
# sum = number1 + number2
# print("addition of two number is: ", sum)

#area of a rectangle - calculated directly in print
# length = int(input("length(cm):"))
# width = int(input("width(cm):"))
# print("area of a rectangle is", length*width)

# Prompting for input and splitting into two numbers
# nums = input("Enter two numbers separated by space: ").split()
# # print (nums)
# num1 = float(nums[0])
# num2 = float(nums[1])
# # print("The sum is:", num1 + num2)
# print("The sum is:", float(nums[0])+float(nums[1]))

#BMI calculator
# weight = float(input("weight: "))
# height = float(input("height: "))
# print ("Your BMI is:", weight/height**2)

hrs =float(input("Enter Hours:"))
rpr = float(input("rate per hour:"))
print ("Pay:", hrs*rpr)


