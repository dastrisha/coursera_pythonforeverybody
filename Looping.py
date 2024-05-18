print ("hello world!")

"""Write a program which repeatedly reads numbers until the user enters
“done”. Once “done” is entered, print out the total, count, and average of
the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.
  
  """

# total = 0
# count = 0
# try:
#     while True:
#         num_input = input("Enter a number: ")
        
#         if num_input.lower() == 'done':
#             break
        
#         number = float(num_input)
#         total += number
#         count += 1

#     if count > 0:
#         print("Total:", total)
#         print("Count:", count)
#         print("Average:", total / count)
#     else:
#         print("No numbers were entered.")

# except ValueError:
#     print("Invalid input")

# """ above question can be solved using for loop """
# total = 0
# count = 0

# for _ in range(float('inf')):
#     num_input = input("Enter a number (or 'done' to finish): ")
    
#     if num_input.lower() == 'done':
#         break
    
#     try:
#         total += float(num_input)
#         count += 1
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# if count > 0:
#     print("Total:", total)
#     print("Count:", count)
#     print("Average:", total / count)
# else:
#     print("No numbers were entered.")

#assignment

#largest = None
#smallest = None
listnumber = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        number = int(num)
        listnumber.append(number)

        smallest = min(listnumber)
        largest = max(listnumber)

    # for itervar in listnumber:
    #     if smallest is None or itervar < smallest:
    #         smallest = itervar
    # print("Minimum is ", smallest)

    # for itervar in listnumber:
    #  if largest is None or itervar > largest :
    #     largest = itervar
    # print ('Maximum is ', largest)
    except ValueError :
        print("Invalid Input")
        
print ('Maximum is ', largest)
print ("Minimum is ", smallest)



# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     print(num)

# print("Maximum", largest)