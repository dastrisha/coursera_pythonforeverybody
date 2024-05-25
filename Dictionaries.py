#  """Running an empty dictionary"""
# eng2sp = dict()
# print (eng2sp)

# """adding value to a key in this dict"""
# eng2sp["one"] = "uno"
# print (eng2sp)

# """print more dict in curly bracket"""
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print (eng2sp['one'])

# """Does keys values or item belonh to the library"""
# keys = eng2sp.keys()
# values = eng2sp.values()
# items = eng2sp.items()

# print(keys)
# print(values)
# print(items)


"""Creating dictionary from 2 lists"""
# keys = ['name', 'age', 'city']
# values = ['Bob', 30, 'Chicago']
# person = dict(zip(keys, values))
# print(person)  # Output: {'name': 'Bob', 'age': 30, 'city': 'Chicago'}

# """Creating merged dictionary"""
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged_dict = {**dict1, **dict2}
# print(merged_dict) 

# #Alternative method is using |

# merged_dict = dict1 | dict2
# print(merged_dict) 



"""Exercise : Write a program that reads the words in words.txt and stores them
as keys in a dictionary. It doesn’t matter what the values are. Then you can use
the in operator as a fast way to check whether a string is in the dictionary."""

# #creating a dict and assigning key value
# words = dict()
# words["words.tx"] = "It is a beautiful day."

# # Checking if the specific string is in the values directly
# is_str_in_values = "It is a beautiful day." in words.values()

# print(is_str_in_values)

"""Counting the number of times a character appears in a string - Histogram"""

# string = "lafayette"
# d= dict()
# for char in string :
#     if char not in d :
#         d[char] = 1
#     else :
#         d[char] = d[char] + 1

# print (d)


"""Using get function to simply the above process"""

# string = "lafayette"
# d = dict()
# for char in string :
#     d[char]=d.get(char, 0) + 1        #if char is in string , get returns the current count of char. If char not in d, get returns 0
# print (d)


#This can also be done using counter from collections
# from collections import Counter

# character = Counter(string)

# print (character)

"""read through the lines of the file, break each
line into a list of words, and then loop through each of the words in the line and
count each word using a dictionary."""


#Textbook way of doing the above example using if else

# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print ('File cannot be opened:', fname)

#     exit()
    
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#     else:
#         counts[word] += 1
# print (counts)



"""Looping through dictionaries"""

# count = {'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in count :
#     print (key, count[key])

"""Find specific values"""
# count = {'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in count :
#     if count[key] > 10 :
#         print (key, count[key])

# """Printing Keys in alphabetical order involves comverion to list and then sorting"""
# count = {'chuck' : 1 , 'annie' : 42, 'jan': 100}
# lst = list(count.keys())
# print(lst)                 #The expression dict_keys(['chuck', 'annie', 'jan']) represents a view object in Python, specifically a view of the keys of a dictionary.
# lst.sort()
# for key in lst :
#     print (key, count[key])


"""Removing punctuation from a string """


# import string
# text = "Hello, World! This is an example."
# # Punctuation characters to remove
# punctuation_to_remove = "!?,.;:"

# # Create a translation table to map specific punctuation characters to None
# translation_table = str.maketrans('', '', punctuation_to_remove)  
# #string.punctuation will replace punction_to_remove for removing all punctuation
# #break down the parameters of str.maketrans():
# # Source String: This is the string of characters you want to replace.
# # Destination String: This is the string of characters that will replace the corresponding characters from the source string.
# # Example string with punctuation
# text = "Hello, World! This is an example."

# # Remove specific punctuation characters using the translation table
# clean_text = text.translate(translation_table)

# print(clean_text)  # Output: Hello World This is an example


"""Assignment 1: Write a program that categorizes each mail message by which day
of the week the commit was done. To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the
week. At the end of the program print out the contents of your dictionary (order
does not matter)."""

# fname = "mbox-short.txt"
# fhandle = open(fname, "r")
# word_list = []
# dictionary = {}
# for line in fhandle:
#     if not line.startswith("From ") :   #check if the line starts with From
#         continue
#     line = line.rstrip()                #remove leading and trailing white space
#     word = line.split()[2]              #Split the line into words and make the index to the second element
#     # print(word)
#     word_list.append(word)              #Append the words to the empty list
# #print (word_list)
# for lst in word_list :                  #itierate over each word in the list and count the number using .get
#     dictionary[lst]=dictionary.get(lst,0) + 1
# print(dictionary)


"""Assignment 2: Write a program to read through a mail log, build a histogram using
a dictionary to count how many messages have come from each email address,
and print the dictionary."""
# fname = "mbox-short.txt"
# fhandle = open(fname, "r")
# word_list = []
# dictionary = {}
# for line in fhandle:
#     if not line.startswith("From ") :   #check if the line starts with From
#         continue
#     line = line.rstrip()                #remove leading and trailing white space
#     word = line.split()[1]              #Split the line into words and make the index to the second element
#     word_list.append(word)

# print(word_list)
# for lst in word_list:
#     dictionary[lst] = dictionary.get(lst,0) + 1
# # print (dictionary)

"""Assignment 3: Add code to the above program to figure out who has the most messages
in the file."""

# max_values = max(dictionary.values())
# print (lst , max_values)

"""Assignment 4: This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of your
dictionary."""

# modified_dict = {}                    # Create an empty dictionary to store the modified keys

# for key, value in dictionary.items(): # Loop through the original dictionary

#     new_key = key.split("@")[1]       # Split the key using the "@" as a separator and keep only the part after the "@"

#     modified_dict[new_key] = value    # Add the key-value pair to the modified dictionary

# print(modified_dict)


string = "lafayette"
d= dict()
for char in string :
    if char not in d :
        d[char] = d[char] + 1
    else :
        d[char] = 1

print (d)
