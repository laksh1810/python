'''
#Division by Zero

try:
    result = 10 / 0
except ZeroDivisionError:
    print("cannot divide by zero!")
'''
'''
#File Not Found
try:
    file = open('non_existent_file.txt','r')
except FileNotFoundError:
    print("File not found!")
'''
'''
#Invalid Index Access
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range!")
'''
'''
#Key Not Found in Dictionary
try:
    My_Dict ={1:"Laksh", 2:"Sparsh", 3:"Shivam"}
    print(My_Dict[4])
except:
    print("Key not found")
'''
'''
#Value Error in Type Conversion
try: 
    number = int("hello")
except ValueError:
    print("Invalid literal for int()!")
'''
'''
#Attribute Error
try:
    my_list = [1, 2, 3]
    my_list.append('a')
    my_list.non_existent_method()
except AttributeError:
    print("Attribute does not exist!")
'''
'''
#Import Error
try:
    import mathg
except ImportError:
    print("Module not found!")
'''
'''
#Handling Generic Exception
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
'''
'''
#Nested Try-Except
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero!")
    result = int("xyz")
except ValueError:
    print("Outer: Invalid literal for int()!")
'''
'''
#Division by Zero with Multiple Exceptions
try:
    num = int("ABC")
    result = 10 / 0
except ValueError:
    print("Invalid literal for int()!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except:
    print("An unexpected error occurred!")
    '''
'''
#IndexError and KeyError

try:
    my_list = [1, 2, 3]
    my_dict = {"a": 1, "b": 2}
    print(my_list[4])
    print(my_dict["c"])
except IndexError:
    print("Index out of range!")
except KeyError:
    print("Key not found in dictionary!")
except:
    print("An unexpected error occurred!") 
'''
'''
#TypeError and ValueError in Conversion
try:
    num = int("abc")
    result = 'a' + 1
except ValueError:
    print("Invalid literal for int()")
except TypeError:
    print("incompatible types for operation")
except:
    print("An unexpected error occurred")
'''