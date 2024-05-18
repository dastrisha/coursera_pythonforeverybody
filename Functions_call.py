# import random
# for i in range(10):
#     x = random.random()  # we are importing random function of random module so dot notation is necessary
#     print (x)
    
# from random import random   #if we do not want to use dot notation then we need to specify which function we are using while importing it here.

# for i in range(10):
#     x = random()
#     print(x)

# def print_lyrics():
#     print ("I'm a lumberjack, and I'm okay.")
#     print ('I sleep all night and I work all day.')

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# repeat_lyrics()

# def computepay(h, r):
#     return 42.37

# hrs = input("Enter Hours:")
# p = computepay(10, 20)
# print("Pay", p)

# """ assignment question"""
# def computepay(h, r):
#     if h <= 40 :
#         pay= h*r
#         return pay
#     else:
#         normal_pay= 40*r
#         overtime_hours = h - 40
#         overtime_pay = overtime_hours * r * 1.5
#         pay = normal_pay + overtime_pay
#         return pay

# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input ("Rate: ")
# r = float (rate)

# p = computepay(h,r)
# print("Pay", p)

"""Addition function"""
# def add(a,b) :
#     result =a + b
#     return result

# result = add(3,5)
# print (result)

"""Write a function called max_number that takes two numbers as input and returns the maximum of the two."""
# def maxnumber(a,b) :
#     return max(a,b)

# result = maxnumber(4,7)
# print(result)

"""Factorial function """

# def factorial(a):
#     result = 1
#     for i in range(1, a+1):
#         result= result*i
#     return result
# fact_result = factorial(8)
# print(fact_result)
    

# def area_rect(l,b) :
#     return l * b

# while True :
#     try:
#         l = float(input("length: "))   #typecasting
#         b = float (input("breath: "))
#         if l and b > 0 :
#             area = area_rect(l,b)
#             print("area of a rectangle is: ", area)
#             break
#         else :
#             print ("Enter positive number")

#     except ValueError as e :
#         print ("Error", e)

    
def area_rect(length, breadth):
    return length * breadth

while True:
    try:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        
        if length <= 0 or breadth <= 0:
            raise ValueError ("input is negative number")
        if length and breadth <= 100 :
            raise ValueError ("input exceeds 100")
        
        area = area_rect(length, breadth)
        print("Area of the rectangle:", area)
        break
    
    except ValueError as e:
        print("Error", e)

    
    




