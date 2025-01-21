'''
#Creating an empty set:
empty_set = set()
print(empty_set)
'''
'''
#Creating a set with values:
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
'''
'''
#Adding an element to a set:
fruits = {'apple', 'banana', 'cherry'}
fruits.add('date')
print(fruits)
'''
'''
#Removing an element from a set:
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('cherry')
print(fruits)
'''
'''
#Finding the number of elements in a set:
fruits = {'apple', 'banana', 'cherry'}
x = len(fruits)
print(x)
'''
'''
#Copying a set:
fruits = {'apple', 'banana', 'cherry'}
x = fruits.copy()
print(x)
'''
'''
#Clearing a set:
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)
'''
'''
#Creating a set from a list with duplicates removed:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
'''