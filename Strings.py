# fruit = "banana"    #code is similar to below code but not as flexible
# for letter in fruit :
#     print (letter)

# this code gives the same result as above but we can change or modify things here. However chances of doing  mistake is relatively more.
# fruit = "banana"
# index = 1
# while index < len(fruit) :
#     letter = fruit[index]
#     print (letter)
#     index = index + 1

# fruit = "banana"
# count = 0
# for letter in fruit:
#     if letter == "a" :
#         count += 1
# print ("Total count is :", count)


"""illustrate the concept of printing a variable within a loop and how it behaves based on the scope of the variable and the condition within the loop."""

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# count = 0


# # Iterate over each number in the list
# for num in numbers:
#     # Check if the number is even
#     if num % 2 == 0:
#         # Increment the count if the number is even
#         count += 1
#     # Print the current count after each iteration
# print("Current count:", count)

# # Print the final count after the loop completes
# print("Total count of even numbers:", count)


"""make a copy of greet in lower case and then store it into zap. This will make a copy so greet is going to be unchanged""" 

# greet = "Hello bob"
# zap = greet.lower()     #.lower() is a method 

# print (type(greet))
# print (dir(greet))


"""Write a loop that starts at the last character in the string and
works its way backwards to the first character in the string, printing each letter on
a separate line, except backwards"""

# #Using for loop - strategy 1 Using reverse string function

# string = "character"
# backward = ""
# for char in reversed(string) :
#     backward = backward + char
# print(backward)

#Using for loop - strategy 2 Use splicing 
# #using while loop

# word = "hello"

# # Iterate over the characters of the string in reverse order
# for char in word[::-1]:   # The [::-1] slicing syntax starts from the last character and works its way backwards to the first character.
#     print(char)

#Using while loop :
# word = "hello"
# index = len(word) - 1  # Start at the index of the last character
# Iterate using a while loop until index becomes -1 (inclusive)
# while index >= 0:
#     print(word[index])  # Print the character at the current index
#     index -= 1  # Decrement the index to move backwards in the string

"""5 practice questions covering string concepts"""

#1. Length of string using len


# length = (input("Input name"))
# print (len(length))

#2. Tranverse through a string with for loop
# string = "Hello"

# for char in string :
#     print (char)

#2. Tranverse through a string with while loop

# string = "Hello"
# index = 0 #Keeps track of the current position of the string

# while index < len(string):
#     print(string[index]) #Inside the loop, we use print() to print the character at the current position indicated by index. We access the character in the string using string[index].
#     index+=1   #This is important because it allows us to move to the next character in the string in the next iteration of the loop.


#3. String slicing: Given a string sentence = "The quick brown fox", write a Python program to print the substring "quick" using string slicing.

# sentence = "The quick brown fox"
# word_to_find = "quick"
# startIndex = sentence.find(word_to_find)
# endIndex = sentence.find(word_to_find) + len(word_to_find)
# print(sentence[startIndex:endIndex])

#4. String concatenation::  Write a Python program to concatenate two strings entered by the user and display the concatenated string.

# string1 = "Hello"
# string2 = "World"
# concant = string1 + " " + string2
# print (concant)

#4. Looping and counting: Write a Python program to count the number of occurrences of a specific character in a given string entered by the user. Use a loop to traverse through the string and count the occurrences.

# word = "fruitbasket"
# count = 0

# for letter in word :
#     if letter == "t" :
#         count = count + 1
# print(count)

#Same problem as above using while loop
# word = "fruitbasket"
# count = 0
# index = 0

# while index < len(word):
#     if word[index] == "t":
#         count += 1      # If the character at the current position is "t", this line increments the count variable by 1, indicating that another occurrence of "t" has been found.
#     index += 1          #This line increments the value of index by 1 in each iteration of the loop. It moves to the next character in the word.

# print(count)

#5. String comparision : Write a Python program that takes two strings as input from the user and checks if they are equal. If they are equal, print "Strings are equal", otherwise print "Strings are not equal".

# string1 = "Hello"
# string2 = "world"
# if string1 == string2 :
#     print ("equal")
# else :
#     print ("unequal")

#Using while loop to do above 

# string1 = "Hello"
# string2 = "Hello"

# # Initialize index for while loop
# index = 0

# # Initialize a flag to track equality - initializing equal to True provides a clear indication that the variable is intended to track equality, and it starts with the assumption that the strings are equal until proven otherwise
# equal = True

# # Check each character of the strings
# while index < len(string1) and index < len(string2):
#     if string1[index] != string2[index]:
#         equal = False   #exit the loop immidiately if inequality is found
#         break         
#     index += 1          #increment indec only if inequalityt is not found

# # If equal is still True, it means the strings are equal
# if equal:
#     print("equal")
# else:
#     print("unequal")

"""Format operators in string"""

#Format operator with one format sequence:

# age = 25
# message = "I am %d years old." % age
# print(message)


#format operator with multiple format sequences


# # Define a format string with format sequences
# format_string = 'In %d years I have spotted %g %s.'

# # Create a tuple containing values to replace the format sequences
# values_tuple = (3, 0.1, 'camels')

# # Apply the format operator (%) to format the string
# result = format_string % values_tuple

# # Print the formatted string
# print(result)


"""Chapter exercsise question"""

# str = 'X-DSPAM-Confidence: 0.8475'
# extractspace = str.find(" ")
# floatnumber = float(str[extractspace:])
# print (floatnumber)
# print(type(floatnumber))

"""quiz questions"""
# str1 = "Hello"
# str2 = 'there'
# bob = str1 + str2
# print(bob)

# x = '40'
# y = int(x) + 2
# print(y)

# x = 'From marquard@uct.ac.za'
# print(x[8])

# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])

