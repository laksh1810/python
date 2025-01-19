'''
#concatenate Two Strings

String1 = input("Enter the first string: ")  
String2 = input("Enter the second string: ")   
result = String1+String2
print(f"Concatenated string: {result}")
'''
'''
#Find the Length of a String

String1 = input("Enter the string: ")
length = len(String1)                             #why cant we use len.string1
print(f"The length of the string is: {length}")
'''
'''
#Convert String to Uppercase

String = input("Enter your string: ")
uppercase = String.upper()                     #why () at the end? 
print(uppercase)
'''
'''
#Convert String to Lowercase

String = input("Enter your string: ")
lowercase = String.lower()
print(lowercase)
'''
'''
#Count a Specific Character in a String

String = input("Enter your string: ")
char = input("Enter the character to count: ")
count = String.count(char)
print(f"{char} appears {count} times in the string.")
'''
'''
#Check if a String Starts with a Specific Substring

String = input("Enter your string: ")
substring = input("Enter the starting substring: ")
is_start = String.startswith(substring)
print(f"Does the substring starts with {substring}? {is_start}")
'''
'''
#Check if a String Ends with a Specific Substring

String = input("Enter your string: ")
substring = input("Enter the ending substring: ")
is_end = String.endswith(substring)
print(f"Does the string ends with {is_end}? {is_end}")
'''
'''
#Remove Leading and Trailing Whitespaces

String = input("Enter the text: ")
trimmed = String.strip()
print(f"Your trimmed text is: {trimmed}")                         # '{trimmed}' or {trimmed}

'''
'''
#Replace a Character in a String

String = input("Enter your desired text: ")
old_char = input("Enter the character you wish to replace: ")
new_char = input("Enter the new character: ")
result = String.replace(old_char, new_char)
print(f"The new string is {result}")
'''
'''
#Repeat a String Multiple Times
String = input("Enter your desired text: ")
times = int(input("How many times to repeat it?"))
result = String * times
print(f"repeated result: {result}")
'''
'''
#Check if a String Contains a Substring

String = input("Enter the desired text: ")
substring = input("Enter the substring to check: ")
is_present = substring in String
print(is_present)
'''
'''
#Convert a String into a List of Words

string = input("Enter a sentence: ")
words = string.split()
print(f"List of words: {words}")

'''
'''
#Capitalize the First Letter

String = input("Enter the text: ")
capitalize = String.capitalize()
print(capitalize)
'''
'''
#Check if All Characters are Alphabets                             #counting space as non- alphabet

string = input("Enter a string: ")
is_alpha = string.isalpha()
print(is_alpha)
'''
'''
#Remove All Spaces from a String

String = input("Enter the text: ")
x = String.replace(" ","")
print(x)
'''

'''
#Reverse the Words in a Sentence

String = input("Enter the text: ")
reversed_words = " ".join(String.split()[::-1])                       #explaination
print(reversed_words)
'''
'''
#Check if a String is Numeric

String = input("Enter the text: ")
x = String.isdigit()
print(x)
'''
'''
#Count the Number of Spaces in a String

String = input("Enter the sentence: ")
x = String.count(" ")
print(x)
'''

#counts vowels in a String

String1 = ("Aa bete kaha kahan let paaya")
vowels = "aeiou"
count = sum(1 for char in String1.lower() if char in vowels)
print(count)










































































