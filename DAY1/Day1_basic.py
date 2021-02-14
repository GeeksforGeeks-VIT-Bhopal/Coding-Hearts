# Variables
myname = 'Kritika'
x = 6
y = 10.0
print(y)
print(myname)

"""
# Data types
# str, int , float, list, etc..
"""
print("My name is " + myname )
print("x =", x)


# conditional statements
# ==, !=, >, <, >=..

# If else statement 
money = 400
if money>500:
    print("Go for a party!!")
    print("YAYY")
else:
    print("Be at Home")


# nested if else
#if....elif....else
# money = 1100
# money = 650
money = 200
if money>1000:
    print("Go for Underbelly")
elif money>500:
    print("Go to visa")
else:
    print("Have Pani puri")


# List
# 0-indexing        0       1       2..
# negative indexing -1
valentine_gifts = ["rose", "ring", "chocolates", "teddy", "promise card", "date"]
# input() function to get input from user
date = input("Enter the value of date ")    # by default input is of string type
# use int(input()) for integer input, similarly use float(input()) for float data
# date = int(input("Enter the value of date ")) 

# type() function to know the type of our variable
print(type(date))  # string type
print(type(valentine_gifts))  # list type
print("date is " + date)

if date == '14':
    print(valentine_gifts[-1])


# Solution of the ques. asked during session regarding list, indexing and if-else
valentine_gifts = ["rose", "ring", "chocolates", "teddy", "promise card", "date"]
date = int(input("Enter the value of date "))

if date == 7:
    print("Gift " + valentine_gifts[0])
elif date == 8:
    print("Gift " + valentine_gifts[1])
elif date == 9:
    print("Gift " + valentine_gifts[2])
elif date == 10:
    print("Gift " + valentine_gifts[3])
elif date == 11:
    print("Gift " + valentine_gifts[4])
elif date == 14:
    print("Go for a " + valentine_gifts[5])
else:
    print("Milne chale jao yaar virtual gifts kab tak bhejoge")


# Loops - 2 types: for and while
# for loop
for i in range(5):
    print("Sorry!")


# while loop
i = 0   # initialize the looping variable
while i<5:  # check the condition
    print("Sorry!")
    i+=1    # increment the looping variable
