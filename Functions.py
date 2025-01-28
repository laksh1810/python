'''
#addition function

def add(x, y):
    return x+y
print(add(3,5))
'''
'''
#Subtraction function

def substraction(x, y):
    return x-y
print(substraction(5,3))
'''
'''
#Multiplication function

def multiplication(x, y):
    return x*y
print(multiplication(3,5))
'''
'''
#division function

def division(x, y):
    return x/y
print(division(15,5))
'''
'''
#factorial function

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n*factorial(n-1)
print(factorial(5))
'''
'''
#power function

def power(x,n):
    return x**n
print(power(3,2))
'''
'''
#Square Root Function:
def Square(x):
    return x**0.5
print(Square(625))
'''
'''
#Cube Function:
def cube(x):
    return x**3
print(cube(3))
'''
'''
#Check Even or Odd Function:

def odd_even(n):
    if n % 2 ==0:
        return "Even"
    else:
        return "Odd"
print(odd_even(6))
'''
'''
#Check Prime Function:
def is_prime(n):
    if n <=1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % 1 == 0:
            return False
    return True
    
print(is_prime(9))
'''
'''
#Reverse a String Function:
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello World"))
'''
'''
#Check Palindrome Function:
def palindrome(p):
    if p == p[::-1]:
        return ("Thats a palindrome")
    else:
        return("Thats not a palindrome")
print(palindrome("radar"))
'''
'''
#Sum of List Function:
def sum_list(lst):
    return sum(lst)
print(sum_list([1,2,3,4,5]))
'''
'''
#Average of List Function:

def average(lst):
    return sum(lst) / len(lst)
print(average([5,2,3,6,8]))
'''
'''
#Maximum Element in List Function:
def max_list(lst):
    return max(lst)
print(max_list([2,5,9,7,12,0,33]))
'''
'''
#Minimum Element in List Function:

def minimum(lst):
    return min(lst)
print(minimum([1,2,3,4,50,0,6,7]))    
'''
'''
#Count Characters in String Function:
def chars(s):
    return len(s)
print(chars("Hello"))
'''
'''
#Count Vowels in String Function:
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
print(count_vowels("hello"))
'''

#Check Leap Year Function:

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(leap_year(2024))











