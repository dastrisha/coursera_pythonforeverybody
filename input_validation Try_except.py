"""Examples using input validation, conditional statement and error handling 
    """
# number = int(input("type number: "))
# if number%2==0 : 
#     print ("number is even")
# elif number >=5 :      #double nested condition
#     #print ("number is greater than 5")
#     if number >5 :
#         print ("number is greater than 5")
#     else :
#         print("number is equal to 5")
# else:
#     print("number is odd")

#try /exception examples:


# try: 

#     number = int(input("type number: "))
# if number%2==0 : 
#      print ("number is even")
# elif number >=5 :      #double nested condition
#     #print ("number is greater than 5")
#         if number >5 :
#  print ("number is greater than 5")
#         else :
#         print("number is equal to 5")
#     else:
#     print("number is odd")

# except ValueError:
# print ("Error: enter integer")

"""Rewrite your pay computation to give the employee 1.5 times thehourly rate for hours worked above 40 hours"""

# hours = float(input("Enter Hours: "))
# rate = float(input("Enter Rate: "))

# if hours <= 40:
#     pay = hours * rate
# else:
#     normal_hours = 40
#     overtime_hours = hours - 40
#     pay = (normal_hours * rate) + (overtime_hours * rate * 1.5)

# """Other way of using writing this code"""
# hours = float(input("Hours: "))  # Using float to allow decimal values
# rate = float(input("Rate: "))    # Using float to allow decimal values
# pay = float(input("Pay: "))      # Using float to allow decimal values

# if hours > 40:
#     overtime_hours = hours - 40
#     overtime_pay = overtime_hours * rate * 1.5
#     new_pay = pay + overtime_pay
#     print("New Pay is", new_pay)
# else:
#     print("No overtime, Pay remains", pay)

"""Use try and except to end this code gracefully incase we are using non numberic value as input by the user """
# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))

#     if hours <= 40:
#         pay = hours * rate
#     else:
#         normal_hours = 40
#         overtime_hours = hours - 40
#         pay = (normal_hours * rate) + (overtime_hours * rate * 1.5)
# except ValueError: 
#     print("Error: Enter numberic value")

# """Below code is incorrect. The input() function doesn't accept a range() argument. The range() function is used to generate a sequence of numbers, not to specify the range of valid input values for input(). Instead, you should handle the validation manually after receiving the input.
# The range() function expects integer arguments, but you're providing float arguments"""
# try:
#     score = float(input("score:", range(0.0,1.0)))
#     if score >=0.9 :
#         print("A")
#     elif score >=0.8:
#         print("B")
#     elif score >=0.7:
#         print("C")
#     elif score >=0.6:
#         print("D")
#     elif score <0.6:
#         print("bad score")
#     elif score == str(score):
#         print ("bad score")
# except ValueError:
#     print("Out of range")

# """corrected code is below. Validate Input Range:
# The program checks if the entered score is within the valid range of 0.0 to 1.0 using an if statement and the comparison operators >= and <=.
# If the score is within the range, the program proceeds to determine the corresponding grade. If it's outside the range, the program prints "Out of range"."""


#assignment question

"""Other way of writing this code"""
# hours = float(input("Hours: "))  
# rate = input("Rate: ")
# rate=float(rate) 
# normal_pay= 40*10.5
# if hours > 40:
#     overtime_hours = hours - 40
#     overtime_pay = overtime_hours * rate * 1.5
#     new_pay = normal_pay + overtime_pay
#     print(new_pay)

"""Write a Python program that prompts the user to enter their weight (in kilograms) and height (in meters). 
    The program should then calculate the Body Mass Index (BMI) using the formula: BMI = weight / (height * height). 
    After calculating the BMI, the program should categorize the BMI into one of the following categories based on the BMI value:

# BMI < 18.5: Underweight
# 18.5 <= BMI < 25: Normal weight
# 25 <= BMI < 30: Overweight
# BMI >= 30: Obese"""

# try:
#     weight = float(input("Weight: "))
#     height = float(input("Height: "))
#     bmi= int(weight/(height*height))
#     print ("BMI is ", bmi)

#     if bmi < 18.5 :
#         print ("Underweight")
#     elif 18.5 <= bmi < 25 :
#         print ("normal weight")
#     elif 25 <= bmi < 30:
#         print ("overweight")
#     else :
#         print ("Obese")

# except ValueError:
#     print ("Error: Enter numberic value")

# """above example is re-written using while loop to repeatedly prompt the user for input until valid input is entered"""
# while True:
#     try:
#         weight = float(input("Enter weight (in kilograms): "))
#         height = float(input("Enter height (in meters): "))
#         if weight <= 0 or height <= 0:
#             print("Error: Weight and height must be positive numbers. Please try again.")
#             continue
#         bmi = weight / (height * height)
#         if bmi < 18.5:
#             print("BMI Category: Underweight")
#         elif 18.5 <= bmi < 25:
#             print("BMI Category: Normal weight")
#         elif 25 <= bmi < 30:
#             print("BMI Category: Overweight")
#         else:
#             print("BMI Category: Obese")
#         break  # Exit the loop if valid input and calculation are successful
#     except ValueError:
#         print("Error: Invalid input. Please enter numeric values for weight and height.")

"""Password Validation: Write a Python program that prompts the user to enter a password. 
The program should validate the password to ensure it contains at least 8 characters. 
If the password is valid, print "Password set successfully!" 
Otherwise, display an error message and prompt the user to enter the password again."""

# while True:
#     try:
#         password = input("Enter password (at least 8 characters): ")
#         if len(password) < 8:
#             raise ValueError("Password must be at least 8 characters long.")  #raise valueerror makes it explicit to the user that there is error if the if condition is not met
#         print("Password set successfully!")
#         break  # Exit the loop if password validation passes
#     except ValueError as e:
#         print("Error:", e) #In Python, when catching an exception using a try-except block, you can specify a variable name after the as keyword to assign the exception instance to that variable. This variable name can then be used within the except block to refer to the exception instance.

"""Same example can be executed without try-exception"""

# while True:
    
#     password= input("enter password 8 characters long: ")
#     if len(password) > 8 :
#         print ("password set successfully!")
#         break                               #break this loop when the condition is met so break is within scope of if
#     else:
#         print ("Password unacceptable. Must be 8 characters long! ")
    
"""User Age Verification.Write a Python program that prompts the user to enter their age. 
The program should verify the age to ensure it is between 0 and 150 (inclusive). 
If the age is valid, print "Age verified successfully!" 
Otherwise, display an error message and prompt the user to enter their age again."""

# while True:
#     try:    
#         age = int(input(" Enter age: "))
        
#         if 0 < age <= 150 :
#             print ("Age verified successfully")
#             break
#         else:
#             raise ValueError ("Age is out of range")
#     except ValueError as e :
#         print ("Error", e)

