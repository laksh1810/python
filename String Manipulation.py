'''
#Reverse a String                                       #explaination

String = "hello"
x = String[::-1]    
print(x)
'''

'''
#Check if a String is Palindrome

String = "madam"
x = String == String[::-1]
print(x)
'''
'''
# Count Vowels in a String                              #explaination

String = "Hello World"
vowels = "aeiou"
count = sum(1 for char in String.lower()if char in vowels)
print(count)
'''
'''
#Remove Vowels from a String                         #explaination

String = "Hello World"
vowels = "aeiou"
result = ''.join(char for char in String if char.lower() not in vowels)
print(result)
'''
'''
#Replace Spaces with Hyphens

String = "Hello World"
x = String.replace(" ","-")
print(x)
'''
'''
#Count Words in a String

String = "Hello World"
x = len(String.split())
print(x)
'''
'''
#Capitalize the First Letter of Each Word

String = "hello world"
x = String.title()
print(x)
'''
'''
#Convert String to Uppercase

String = "Hello World"
x = String.upper()
print(x)
'''
'''
#Convert String to Lowercase

String = "Hello World"
x = String.lower()
print(x)
'''
'''
#Count Occurrences of a Character

String = "Everything is planned"
x = "e"                                             #how to fetch/check multiple characters
count = String.count(x)
print(count)
'''
'''
#Check if a String is Alphanumeric

String = "123Alpha"
x = String.isalnum()
print(x)
'''
'''
#Check if Two Strings are Anagrams

String = "listen"
String2 = "silent"
x = sorted(String) == sorted(String2)
print(x)
'''
'''
#Swap Case of a String

String = "Hello World"
Swapped = String.swapcase()
print(Swapped)
'''
'''
#Find the Longest Word in a String

String = "I love programming in Python"
x = max(String.split(), key=len)
print(x)
'''
'''
#Check if a String Contains Only Digits

String = "12345"
x = String.isdigit()
print(x)
'''
'''
#Split a String by Comma

String = "apple, banana, cherry"
x = String.split(',')
print(x)
'''
'''
#Join a List of Strings

String = ["hello", "world"]
x = " ".join(String)
print(x)
'''
'''
#Reverse Words in a Sentence                        #Explaination

String = "God is good"
x = " ".join(reversed(String.split()))
print(x)
'''
'''
#Remove Whitespaces

String = "God is good"
x = String.strip()
print(x)
'''
'''
#Check if a String is a Substring of Another

String = "Hello World"
String2 = "World"
x = String in String2
print(x)
'''
'''
#Convert String to List of Characters

string = "hello" 
char_list = list(string)
print(char_list)
'''
'''
#Count Uppercase and Lowercase Letters                                  #Explaination

string = "Hello World"
uppercase = sum(1 for char in string if char.isupper())
lowercase = sum(1 for char in string if char.islower())
print(f"Uppercase: {uppercase}, Lowercase: {lowercase}")
'''















































































































