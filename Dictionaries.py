# """Running an empty dictionary"""
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

string = "lafayette"
d = dict()
for char in string :
    d[char]=d.get(char, 0) + 1        #if char is in string , get returns the current count of char. If char not in d, get returns 0
print (d)