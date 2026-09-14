import hello_world
import copy
import csv
'''
def count_vowels(word):
    vowels='aeiou'
    count=0
    for char in word.lower():
        if char in vowels:
            count+=1
    return count

print(count_vowels("Precious"))
  '''   
    

#list
# an ordered collection of items, also called elements
# can contain elements of different data types
# is mutable

# Q1: How do we create a list?
scores = [85, 92, 78, 90, 10]

# Q2: How do we access individual elements of a list?
# indexing, positive/negative indices, len()

# Q3: How do we access a portion of a list?
# Q4: Can we change elements of a list after it is created?

# Q5: How do we loop through a list?
# for value, range(len()), enumerate()

for idx, val in enumerate(scores):
    print(idx, val)

# Q6: What operators can we use with lists?
# concatenation (+), repetition (*), membership (in, not in)



# Q7: What built-in functions can we use with lists?
# len(), sum(), min(), max(), sorted()


# Q8: What methods can we use to modify a list?
# append(), extend(), insert(), remove(), pop(), sort()
# sorted() vs sort()


# Q9: How do we represent two-dimensional data using lists?
# nested lists, [row][column], nested loops


# Q10: How can we create a list more concisely?
# list comprehension
# [expression for item in iterable if condition]


# Q10: What happens when two variables refer to the same list?
# aliasing, == vs is

# Q11: How can we create a copy of a list?
# .copy() or [:] both create a shallow copy.
# What does "shallow copy" mean for nested lists?
# copy.deepcopy()


# Q12: What happens when we pass a list to a function?
# parameter refers to the same list object
# Be careful about modifying mutable arguments


# Q13: Can a function create and return a list?
# start with [], append elements, return the list

#class activity
'''
import random
def generate_num():
    num=[random.randint(1,10) for _ in range(20)]
    return num

def count(val_list,target):
    count= val_list.count(target)
    print(target,"appear", count, "times")

def remove_number(numbers, target):
    if target not in numbers:
        print("Sorry, your number is not here!")
    else:
        while target in numbers:
            numbers.remove(target)

#main program
number=generate_num()
number.sort()
print(number)
count(number,4)
remove_number(number,8)
print(number)
'''
