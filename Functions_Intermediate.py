'''
#Simple Calculator using Functions
def add(a,b):
    return(a+b)
def substract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    if b == 0:
        print("Error! division not possible with Zero")
    else:
        return(a/b)
    
def calculator():
    print("Simple Calculator")
    print("1. Add\n2. Substract\n3. Multiply\n4. Divide")
    choice = int(input("Enter the number of choice: "))

    num1 = float(input("Enter First number: "))
    num2 = float(input("Enter Second number: "))
    operations = {1:add, 2:substract, 3:multiply, 4:divide}
    if choice in operations:
        print("Result: ", operations[choice](num1,num2))
    else:
        print("Invalid choice!")

calculator()
'''
'''
#Palindrome checker

def is_palindrome(str):
    return str == str[::-1]
text = input("Enter a string: ")
print(f'"{text}" is a palindrome.' if is_palindrome(text) else f'"{text}" is not a palindrome.')
'''
'''
#Multiplication Table Generator

def multiplication_table(n):
    for i in range(1,11):
        
        print(f"{n} X {i} = {n*i}")

num = int(input("Enter the number: "))
multiplication_table(num)
'''


#ATM Withdrawal Simulation
def withdrawal(balance, amount):
    if amount>balance:
        return "Insufficient Balance"
    return balance - amount

balance = 5000
amount = int(input("Enter the amount: "))
new_balance = withdrawal(balance, amount)
print("New balance: ", new_balance)