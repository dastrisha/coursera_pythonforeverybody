# #When the bracket operator appears on the left sideof an assignment, it identifies the element of the list that will be assigned.
# numbers = [1,2,3]
# # numbers[1] = 5 #number at position 1 is assigned the value 5
# # print (numbers)

# for i in range(len(numbers)) :
#     numbers[i] = numbers[i] * 2 #Take the number at position i in the list numbers, multiply it by 2, and put the result back into the same position
#     print (numbers)

# """splicing""" 

# numbers = [1, 3, 5]
# splice = numbers [1:3]
# print (splice)

# #A slice operator on the left side of an assignment can update multiple elements:
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# t[1:3] = ['x', 'y']
# print (t)

"""Delete elements"""

t = ['a', 'b', 'c', 'd', 'e', 'f']
# x = t.pop(1)
# print (t)    #gives list without element thats being removed
# print (x)    #prints removed element

#If you know the element you want to remove (but not the index), you can use remove
# t.remove("a") 
# print(t)

#To remove more than one element, you can use del with a slice index
# del t[1:3]
# print (t)


"""Appending List"""

# #modfies an existing list
# t = ['a', 'b', 'c', 'd', 'e', 'f']
# # t.append("s")
# # print (t)

# #makes a new list
# t1 = t + ["s"]
#print (t1)

""" calculate average without list """

# total = 0
# count = 0

# while True :
#     input_num = input("input a number : ")
#     if input_num == "Done" : break 
#     else :
#         float_num = float(input_num)
#         count =+ 1
#         total =+ float_num

# print ("average: ", total/count)

"""Calculating average"""
# num = []
# while True :
#     input_num = input("input a number : ")
#     if input_num == "Done" : break 
#     else :
#         try: 
#             float_num = float(input_num)
#             num.append(float_num)
#         except ValueError :
#             print ("Enter a valid number")

# print ("Average: ", sum(num)/len(num))

"""Strings and lists """

# t= ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# delimiter.join(t)
# print ('pining for the fjords')

# s = 'pining for the fjords'
# t = s.split()     #() takes the delimter value 
# print (t)


""" Exercise question : Write a function called chop that takes a list and modifies it, removing
the first and last elements, and returns None.
Then write a function called middle that takes a list and returns a new list that
contains all but the first and last elements."""

# chop = ["a" , "b" , "c"]
# chopends = list[chop.pop(1)] 
# print (chopends)
# chop.remove("b")
# print (chop)

"""Exercise question : Write a function called chop that takes a list and modifies it, removing
the first and last elements, and returns None."""

# def chops(lst) : 
#     if len(lst) > 1 :
#         del lst[0]
#         del lst[-1]
#     return None 
# def middle(lst) :
#     return lst[1:-1]

# #example :
# chop_list = [1,2,3,4,5]
# chops(chop_list) 
# print (chop_list)

# middle(chop_list)
# print(chop_list)


"""Write a program to open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in the
list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical
order."""

#open a file romeo.txt
# fhandle = open("romeo.txt")
# combined_list = []
# for line in fhandle :
#     line = line.rstrip().rsplit()
#     combined_list += line

# list2 = ['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
# 'and', 'breaks', 'east', 'envious', 'fair', 'grief',
# 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
# 'sun', 'the', 'through', 'what', 'window',
# 'with', 'yonder']                                       #given in the exmaple

# for word in list2 :
#     if word not in combined_list :
#         combined_list.append(word)


# #other way of doing this is using set function
# #Example :

# # Convert lists to sets for efficient comparison
# set1 = set(combined_list)
# set2 = set(list2)

# # Find the words present in list1 but missing in list2
# missing_words = set2 - set1

# print("Words present in combined list but missing in list2:", missing_words)

# # combined_list.sort()
# # print(combined_list)

"""Write a program to read through the mail box data and when you
find line that starts with “From”, you will split the line into words using the split
function. We are interested in who sent the message, which is the second word on
the From line."""

# fhandle = open("mbox-short.txt")
# line_count = 0 
# for line in fhandle :
#     if not line.startswith("From ") : continue
#     final_line= line.rsplit()
#     secondword = final_line[1]
#     print (secondword)

#     line_count = line_count+1

# print(line_count)

"""Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a list
and use the max() and min() functions to compute the maximum and minimum
numbers after the loop completes."""

# empty_list = []

# while True :
#     user = input("Enter a number: ")
#     if user == "Done" :
#         break
#     user_float = float(user)
#     empty_list.append(user_float)

# print(min(empty_list), max(empty_list))

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     print(line.rstrip())

#Assignment 1

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = []
# for line in fh:   
#     words = line.strip().split()
#     lst.extend(words)
#     unique_word = list(set(lst))
#     unique_word.sort()
# print(unique_word)

#Using append as asked in the assignment


# fname = input("Enter file name: ")
# fh = open(fname)
# lst = []
# for line in fh:   
#     words = line.strip().split()
#     for word in words:
#         lst.append(word)
#         unique_word = list(set(lst))
#         unique_word.sort()
# print(unique_word)



