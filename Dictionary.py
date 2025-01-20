'''
#Create an Empty Dictionary:
my_dict = {}
'''
'''
#Access a Value by Key:
person = {'name': 'John','age': 30, 'City': 'New York'}
age = person['age']
print(age)
'''
'''
#Add a New Key-Value Pair:
person = {'name': 'John','age': 30, 'City': 'New York'}
person['gender'] = 'Male'
print(person)
'''
'''
#Clear a Dictionary:
person = {'name': 'John','age': 30, 'City': 'New York'}
person.clear()
print(person)
'''
'''
#Get Value with Default:

person = {'name': 'John','age' : 30'City': 'New York'}
age = person.get('age', 25) # If 'age' key exists, get its value; otherwise, default to 25.
print(age)
'''
#Nested Dictionary:
'''
student = {'name': 'Alice', 'grades': {'math': 90, 'english': 85}}
print(student)
'''
'''
#Get Keys as a List:
person = {'name': 'John','age' : 30, 'City': 'New York'}
keys_list = list(person.keys())
print(keys_list)
'''
'''
#Get Values as a List:
person = {'name': 'John','age' : 30, 'City': 'New York'}
values_list = list(person.values())
print(values_list)
'''
'''    
#Sort Dictionary by Keys:
person = {'Name': 'John','Age' : 30, 'City': 'New York'}
sorted_person = dict(sorted(person.items()))
print(sorted_person)
'''

#Merge Two Dictionaries:
person = {'Name': 'John','Age' : 30, 'City': 'New York'}
additional_info = {'occupation': 'Engineer', 'salary': 80000}
person.update(additional_info)
print(person)













