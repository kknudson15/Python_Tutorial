import numpy
import pandas

#There are two ways to do comments in Python The # sign is for single line comments.
"""
The other way is to use  three sets of double quotes
and can be used for multi line comments.
"""

#Variable declarations

# Strings are marked by either ' '  or " ".
'''
name = 'Kyle'
name2 = "JJ"
'''


# numbers are either integers or float values
'''
Pay attention to the type of the number when doing arithmetic
'''
'''
age = 200
bank = 102.567
'''


#True or false values, booleans, are indicated using True or False.
#True and False must be capitilized
'''
boolean = True
boolean2 = False
'''


#Lists
'''
Lists are similar to arrays in other languages.  They are mutable and are very important when working with 
data science concepts.
'''

'''
animals = ['tiger', 'cat', 'dog']
print(animals[0])
print(animals.append('lion'))
#looping through a list
for animal in animals:
    print (animal)

#if you need the index as well
for index, animal in enumerate(animals):
    print(index, animal)

#another type of loop
for number in range(1,10):
    print(number)

#Slicing lists listName[start:end:increment]
#easy way to reverse order of a list in python is this:
reverse = animals[::-1]
print(reverse)
'''



#Dictionaries
"""
Dicitonaries work similar to arrays.  They act on the concept of key-Value pairs.
These values can either be of the same type or different types. These are extremely 
important in python.  One of the most used data structure in advanced programs.
"""

'''
dict = {'j': 123, 'k': 234, 'l': 'no value'}
print(dict['j'])
print(dict['l'])
print(dict.keys())
print(dict.values())
'''


#function declarations
'''
def myfunction():
    print('This is a function!')

#function call
myfunction()

'''


#Creating a class in python
'''
class Dog:
    #special method similar to constructors in other languages.
    def __init__(self):
        print('dog made')

#creating a Dog object.
dog = Dog()
'''




'''
Ok! Now lets use Python to solve some problems!
'''

'''
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(4))
'''


# Binary Search
'''
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
low = 0
high = 16
target = 1

#Binary Search
def binary_search(list, low, high, target):
    if not low < high:
        return -1

    mid = (high + low)// 2
    if list[mid] < target:
        return binary_search(list, mid + 1, high, target)
    elif list[mid] > target:
        return binary_search(list, low, mid, target)
    else:
        return mid

location = binary_search(numbers,low, high, target)
if (location == -1):
    print('Value not found')
else:
    print("The Location of the number is:", location)
'''
