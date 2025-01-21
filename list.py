'''
My_list = [1,2,3,4,5]
print(My_list)
'''
'''
#Access an Element in a List:

My_list = [1,2,3,4,5]
element = My_list[2]
print(element)
'''
'''
#Add an Element to the End of a List:

My_list = [1,2,3,4,5]
My_list.append(6)
print(My_list)
'''     
'''
#Insert an Element at a Specific Index:

My_list = [1,2,3,4,5]
My_list.insert(1,0)
print(My_list)
'''
'''
#Remove an Element by Value

My_list = [1,2,3,4,5]
My_list.remove(3)
print(My_list)
'''
'''
#Remove an Element by Index

My_list = [1,2,3,4,5]
del My_list[2]
print(My_list)
'''
'''
#Slice a List:
My_list = [1,2,3,4,5]
sub_list = My_list[1:3]
print(My_list)
'''
'''
#Reverse a List:

My_list = [1,2,3,4,5]
My_list.reverse()
print(My_list)
'''
'''
#Sort a List (In-Place): 

My_list = [1,2,3,4,5]
My_list.sort()
print(My_list)
'''
'''
#Sort a List (Creating a New List):

My_list = [1,2,3,4,5]
sorted_list = sorted(My_list)
print(sorted_list)
'''
'''
#Count Occurrences of an Element#
My_list = [1,2,3,4,4,5]
count = My_list.count(4)
print(count)
'''
'''
#Find the Index of an Element:

My_list = [1,2,3,4,4,5]
index = My_list.index(3)
print(index)
'''
'''
#Extend a List with Another List:
My_list = [1,2,3,4,5]
other_list = [6,7,8,9,10]
My_list.extend(other_list)
print(My_list)
'''
'''
#Remove the Last Element:
My_list = [1,2,3,4,5]
My_list.pop()
print(My_list)
'''
'''
#Copy a List (Shallow Copy):
My_list = [1,2,3,4,5]
new_list = My_list.copy()
print(new_list)
'''
'''
#Clear a List:
My_list = [1,2,3,4,5]
My_list.clear()
print(My_list)
'''
'''
#Find the Maximum Value in a List:

My_list = [1,2,3,4,5]
x = max(My_list)
print(x)
'''
'''
#Find the Minimum Value in a List:
My_list = [1,2,3,4,5]
x = min(My_list)
print(x)
'''
'''
#List Reversal:

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)
'''
'''
#List Palindrome Check:

my_list = [1, 2, 3, 2, 1]
is_palindrome = my_list == my_list[::-1]
print(is_palindrome)
'''
'''
#List Zipping:
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(zipped)
'''
'''
#List Element Count:

my_list = [1, 2, 2, 3, 4, 2, 5]
count = my_list.count(2)
print(count)
'''
'''
#List Element Removal:

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
'''





































