'''
#Countdown:
count = 10
while count > 0:
    print(count)
    count -= 1
'''
'''
#multiplication of Numbers:
n = int(input("Enter the number: "))
i = 1
while i <=10 :
    print(i,"X", n, "=", n*i)    
    i +=1
'''
'''
#Sum of Numbers:
sum = 0
num = 1
while num <= 10:
    sum += num
    num += 1
print("Sum:", sum)
'''
'''
#Print Even Numbers:

i = 0
while i <=20 :
    print(i)
    i +=2
'''
'''
#Guess the Number Game:
secret_num = 47
guessed_num = int(input("Enter the number: "))
while secret_num == guessed_num:
    print("correct! you guessed it right")
    break
else:
    print("Incorrect guess")
'''
'''
#Table of 7:

num = 7
i = 1
while i <=10:
    print(num, "X", i, "=", num*i)
    i +=1
'''
'''
# check palindrome                  #explain
word = "radar"
is_palindrome = True
i, j = 0, len(word) - 1
while i < j:
    if word[i] != word[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
print("Palindrome:", is_palindrome)
'''

'''
#power of 2: 

exponent = 0
while exponent <= 10:
    print(2 ** exponent)
    exponent += 1
'''
'''
#Print Odd Numbers:

num = 1
while num <=20:
    print("odd numbers: ", num)
    num += 2
'''
'''
#Find the Average:                      explain

total = 0
count = 0
while True:
    num = int(input("Enter a number (or 0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1
average = total / count if count > 0 else 0
print("Average:", average)
'''
'''
#Print Characters in a String:

string = "Hello, World!"
index = 0
while index < len(string):
    print(string[index])
    index += 1
'''
'''
#Sum of Squares:

sum_of_squares = 0
num = 1
while num <= 5:
    sum_of_squares += num ** 2
    num += 1
print("Sum of squares:", sum_of_squares)
'''

#calculate square root

# num = 5
# while num ** 2:
#     print(num**2)
#     break

number = 25
guess = number / 2
while abs(guess * guess - number) > 1e-6:
    guess = 0.5 * (guess + number / guess)
    print("Square root:", guess)














































