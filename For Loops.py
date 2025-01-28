'''
for i in ("Text"):
    print(i)
'''
'''
#Calculate the sum of numbers from 1 to 10:

sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)
'''
'''
#Print even numbers from 1 to 20:
for i in range(0,21,2):
    print(i, end=" ")
'''
'''
#Calculate the factorial of a number:

n = 5
factorial = 1
for i in range(1, n+1):
    factorial *= i
print("Factorial of", n, "is", factorial)
'''
'''
#Print a list of fruits:
fruits = ["Apple", "Banana", "Mango"]
for fruits in fruits:
    print(fruits)
'''
'''
#Find the largest number in a list:

numbers = [2,3,9,8,7,2,15,8,7,8,9,223,54,7]
max_num = numbers[0]

for num in numbers: 
    if num > max_num:
        max_num = num
print("Largest Number is: ", max_num)
'''
'''
#Print a pattern of stars:

for i in range(1,6):
    print("*" *i)
'''
'''
#Count the number of vowels in a string:

text = "hello world"
count = 0
vowels = "aeiou"
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
'''
'''
#Print a multiplication table:
num = int(input("Enter the number: "))
for i in range(1,11):
    print(num, "X",i, "=", num * i)
'''
'''
#Calculate the sum of a list of numbers:
numbers = [4, 7, 2, 9, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)
'''
'''
#Reverse a string:
text = "Hello"
x = ""

for char in text:
    x = char + x
print(x)
'''
'''
#Print the Fibonacci sequence:                          #Explanation    
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
a, b = b, a + b
'''
'''                                                             #explanation
#Find and print prime numbers in a range:
start = 10
end = 50
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
else:
    print(num)
'''
'''
#Calculate the average of a list of numbers

numbers = [3, 6, 9, 12, 15]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)
'''
'''
#Print the first n even numbers:

n = int(input("Enter the number: "))
for i in range(2,n+1,2):
    print(i)
'''
'''
#Print the squares of numbers from 1 to 10:
for i in range(1,11):
    print(i, "=",i**2)
'''
'''
#Print a countdown from 10 to 1:

for i in range (10,0,1):
    print(i)
'''














