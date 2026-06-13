# Exceptions
"""Logical errors and Bugs
● We create several bugs
● Also users misuse apps
● Or just things go wrong
unintientally """

"""Syntax Error vs Logical errors
● Syntax Error: You did not write the statements in the expected format
○ Parser is complaining. It occurs before running the program
○ E.g. Missing parentheses or indentation problem
■ Both of them in line 3 below
x=1
  print(x 
● Logical Error: It occur at runtime (e.g. divide by zero, access invalid index)
○ We call them exceptions!
○ We have to properly handle them!"""

"""Logical Error
● We can’t build production code this way
● Users will make errors
● Or hackers wanna
get service down """
#
# def read_int(msg):
#     age = input(msg)  # 'Hey'
#     age = int(age)
#     return age
#
# age = read_int('Enter age: ')
# print(age)    # not reachable if RTE before it

"""
Traceback (most recent call last):
  File "01.py", line 4, in <module>
    age = int(age)
ValueError: invalid literal for int() with base 10: 'Hey'"""

"""Blocking Errors
● When we develop applications, we may face conditions where we can’t 
complete the function
○ Creating an array, but system rejects as no enough memory
○ Open a file, but system rejects due to file permissions
○ Network disconnection during a remote call
○ Payment system: pay a bill, but the money is a negative value!
○ Compute sqrt(x), but x is negative!
○ Coding mistakes: access array out of the boundary
● We typically can’t continue processing. We have to stop!
● Sometimes we can detect the problem, sometimes it just happens!
○ How can we communicate as possible the problem? Handle the error?"""

"""2 Major approaches
● Return error codes
○ Your function return some number to indicate results
■ E.g. zero for success, 1 for InvalidURL
○ This is not popular python approach.
● Throwing & Handling Exception 
○ This is a programming language mechanism
■ We can stop processing by raising an exception
■ We can catch it and properly handle it
○ More common & safer
● Future reading: 
Error codes vs exceptions"""

"""Raising Exception
● You can raise errors by yourself
● ValueError is one of the built-in 
classes for exceptions
● Using this syntax you can raise 
exception that can stop the code
● Next: we learn how to handle the 
exception to NOT stop our app"""

# def f(x):
#     if x < 0:
#         raise ValueError(f'{x} is negative value')
#     print(x / 2)
#
#
# if __name__ == '__main__':
#     f(-10)

"""
  File "02.py", line 9, in <module>
    f(-10)
  File "02.py", line 4, in f
    raise ValueError(f'{x} is negative value')
ValueError: -10 is negative value"""

"""Try Catch
● The try and except block can 
help us prevent the exceptions 
from stopping the code
● Try: Run this code
● Except: Jump and Run this 
code if faced stopping errors"""

# def read_int(msg):
#     try:
#         # Please execute this code
#         age = input(msg)  # 'Hey'
#         age = int(age)
#     except:
#         # if a crash, come here to clean!
#         print('Invalid input')
#         age = None
#
#     return age
#
#
# age = read_int('Enter age: ')
# print(age)

"""
Enter age: aaa
Invalid input
None"""

"""Else
● The else is an optional part
● Its block will be executed ONLY if 
the except block is not executed
○ E.g. no errors occurred"""


# def read_int(msg):
#     try:    # Please execute this code
#         age = input(msg)  # 'Hey'
#         age = int(age)
#     except: # if a crash, run to handle!
#         print('Invalid input')
#         age = None
#     else:   # optional: if no crash, run
#         print('Thanks!')
#     return age
#
# age = read_int('Enter age: ')
# print(age)

"""
Enter age: 10
Thanks!
10"""

"""Finally
● The finally block is run in ALL cases
● Useful for final cleaning
○ E.g. close a file
● Both else and finally are optional
○ You can have one of both of them"""

# def read_int(msg):
#     try:    # Please execute this code
#         age = input(msg)  # 'Hey'
#         age = int(age)
#     except: # if a crash, run to handle!
#         print('Invalid input')
#         age = None
#     else:   # optional: if no crash, run
#         print('Thanks!')
#     finally:    # optional: run in all cases
#         print('End of Func')
#
#     return age
#
# age = read_int('Enter age: ')
# print(age)

"""
Enter age: aaa
Invalid input
End of Func
None

Thanks!
End of Func
20
"""

# def read_int(msg):
#     try:
#         # Please execute this code
#         age = input(msg)  # 'Hey'
#         age = int(age)
#     except:
#         # if a crash, come here to clean!
#         print('Invalid input')
#         age = None
#     finally:    # optional
#         # come here regardless crash or not
#         print('End of Func')
#
#     return age
#
#
# age = read_int('Enter age: ')
# print(age)

"""
Enter age: aaa
Invalid input
End of Func
None

Enter age: 10
End of Func
10
"""

# Multiple Exceptions Handling

"""Multiple Exceptions
● Consider this file (data.txt) and the code
● Figure Out as much as u could from the exceptions that may occur during the 
run time"""

# path, idx = input().split()
# idx = int(idx)
#
# file = open(path, 'r')
# lst = file.read().splitlines()
# print(lst[idx])
#
# file.close()
"""
How many possible exceptions?
data.txt 1          ==> 1
data.txt            ==> ValueError: unpack
not_exist.txt 1     ==> FileNotFoundError
/boot/efi/ 1        ==> PermissionError
data.txt hey        ==> ValueError
data.txt 1000       ==> IndexError
data.txt -1000      ==> IndexError
data.txt -1         ==> 30"""

# Multiple Exceptions

# try:
#     path, idx = input().split()
#     idx = int(idx)
#
#     file = open(path, 'r')
#     lst = file.read().splitlines()
#     print(lst[idx])
#
#     file.close()
# except ValueError:
#     print('ValueError')
# except IndexError:
#     print('IndexError')
# except FileNotFoundError:
#     print('FileNotFoundError')
# except:
#     print('Something else')

"""
For the mentioned 3 errors, special handling
Otherwise: last block"""

"""Multiple Exceptions Handling
● We can use except <specific exception>"""

"""Grouping exceptions
● To group exceptions: use a tuple of exceptions"""

# try:
#     path, idx = input().split()
#     idx = int(idx)
#
#     file = open(path, 'r')
#     lst = file.read().splitlines()
#     print(lst[idx])
#
#     file.close()
#
# except (ValueError, IndexError):    # observe ()
#     print('ValueError or IndexError')
# except FileNotFoundError:
#     print('FileNotFoundError')
# except:
#     print('Something else')

#For both ValueError or IndexError => one handling

"""Proper resources Handling
● Utilize the finally block!"""

# file = None
# try:
#     path, idx = input().split()
#     idx = int(idx)
#
#     file = open(path, 'r')
#     lst = file.read().splitlines()
#     print(lst[idx])
#
# except OSError: # cover all sub-types
#     print('Catch all OS errors')
# except:
#     print('Something else')
#
# finally:
#     # In all previous codes we wrongly handled it
#     if file is not None:
#         file.close()

"""Use with statement with files
● Recall: With statement closes the file always if it was opened
○ Even with exceptions
● Also observe new syntax: BaseException, as e, str(e)"""

# try:
#     path, idx = input().split()
#     idx = int(idx)
#
#     with open(path, 'r') as file:
#         lst = file.read().splitlines()
#         print(lst[idx])
#         # File will ALWAYS be closed
# except BaseException as e:      # same as except without class
#     # as e: e is the created exception object
#     error = str(e)  # get the error msg
#     print(error)

"""Reading
● Built-in Exceptions (Exception hierarchy)
○ Short Summary
○ Skip what you don’t understand!
● Future reading: 
Using Python errno
○ We can actually get a number (error code) per exception
○ Caution: codes are platform dependent
● Future reading: Raising an 
Exception to Another Exception"""

# Stack Trace

"""Stack Trace (aka traceback and backtrace)
● The function calls made in your code at a specific point
○ We saw it during debugging functions calls
○ The word stack coming from the Stack data structure (LIFO)
● In big projects, an exception can be in module that called a module that has a 
function called a function
● The trace helps us:
○ What is the exact file/line where problem occurred
○ The function calls from begin to the failure point"""

# import mod2
#
# def f1(x):
#     return mod2.f2(x)
#
# import mod3
#
# def f2(x):
#     return mod3.f3(x)
#
# import mod4
#
# def f3(x):
#     return mod4.f4(x)
#
# import math
#
# def f4(x):
#     return math.sqrt(x)
#
# import mod1
# print(mod1.f1(-10))

"""Stack Trace: Observe
● Last line: Direct message with the error
● Directly before it: where the issue occured
○ File path / Line number
○ Click it, go directly to the line
● Go back and back till the calling point: f4, f3, f2, f1 (LIFO)
● Note: Python 2 was very limited in stack trace info"""

# Stack Unwinding
# Who catch the exception?

# def f4(path, idx):
#     file = open(path, 'r')
#     idx = int(idx)
#     lst = file.read().splitlines()
#     res = lst[idx]
#     file.close()
#     return res
#
# def f3(path, idx):
#     try:
#         return f4(path, idx)
#     except FileNotFoundError:
#         print('F3 caught FileNotFoundError')
#         return -3
#
# def f2(path, idx):
#     try:
#         return f3(path, idx)
#     except ValueError:
#         print('F2 caught ValueError')
#         return -2
#
# def f1(path, idx):
#     try:
#         return f2(path, idx)
#     except IndexError as e:
#         print('F1 caught IndexError')
#         print('Log and raise again')
#         raise e
#
# if __name__ == '__main__':
#     path, idx = input().split()
#     print(f1(path, idx))
#     print('Bye')

"""Stack Unwinding
● Assume some function1 calls function2:
● Assume function2 throws an exception:
○ Does it have a try catch surrounding its location?
■ No ⇒ Terminate the function, remove function2 from stack
■ Yes ⇒ Does it have a matching type?
● No ⇒ Same as last NO
● Yes ⇒ Go to its except block (which may throw again)
● If function1 receives a thrown exception from function 1
○ It does the same logic
○ Either catch and end it or terminate function and propagate up to the caller 
● If caller script received  a thrown exception and did not handle:
○ program crashes at this point"""

"""Trace: not_exist.txt 1
● F4: May throw several errors
● F3: Catch File not found Error
● F2: Catch Value Error
● F1: Catch Index Error / Rethrow
● Main: No global catch
● F4 throws FileNotFoundError
● F3 catches it and return -3
● Program exists without exceptions
Trace: data.txt hey
● F4: May throw several errors
● F3: Catch File not found Error
● F2: Catch Value Error
● F1: Catch Index Error / Rethrow
● Main: No global catch
● F4 throws ValueError
● F3 can’t catch it
○ It propagates up to F2
● F2 catches it
● Program exists without exceptions
Trace: data.txt 1000
● F4: May throw several errors
● F3: Catch File not found Error
● F2: Catch Value Error
● F1: Catch Index Error / Rethrow
● Main: No global catch
● F4 throws IndexError
● F3 can’t catch it: Propagate up
● F2 can’t catch it: Propagate up
● F1 catches it, but raise again
● Program exists an exception
Trace: data.txt 1000
● Observe: Exit code 1. 
● Observe the traceback
Tips
● Don’t throw an exception for a normal flow
○ Exception means something blocking!
● Swallowing Exceptions
○ Don’t hide it. 
○ Either don’t catch
○ Or catch
■ Handle it
■ Or log and Raise
● Be careful from code inside except/else/finally to raise another exception 
unintentionally"""

# Assertions
"""Assertions
● We used assertion before to verify some condition
● assert <condition>, <msg>
● Easy to check, raise exception if condition is not met
○ The exception type is: AssertionError
● What if I want to disable all code assertions?
○ E.g. I intended only some validations but no exception handling and code may fail
● From command line you can pass extra flag: -O (for basic optimization)"""

# Assertions
# x = int(input())
# assert x <= 10, 'x is greater than 10'
# print(2*x)

"""But I may want to optimize but leave assertions?!
● A more risky scenario is as following
● We have several important and intended assertions
● Later, we want to run python but allows more optimizations from interpreter!
● But the optimizer disabled our Assertions!
● The proper way for the intended assertions is to throw an error
○ Regardless the flag, it will be raised"""

# Raise AssertionError

# x = int(input())
# if x > 10:
#     raise AssertionError('x is greater than 10')
# print(2*x)


# Exceptions Homework

"""Problem #2: Compute Differences V2
● Recall v1 program. Please use my code
● Assumptions
○ If a row is invalid, 
■ Either it will have the word NA as part of it
■ Or it has one of its items can’t be parsed to total reviews & total students
○ There will be no missing days in the middle, though it doesn’t matter!
■ At least one valid day
○ The data otherwise will be correct (e.g. has same # of columns / valid entries)
Beyond the homework
● As you see, I am posing assumptions that makes the task easy
● In practice, you can imagine all sort of uncertainties
○ E.g. a row may have less items than total courses
○ E.g. there might be no valid entries per data
○ You may want per day & course, to save the last valid entry
○ To present the best possible output from the file
● Feel free to go as complicated as u want and think in smart solutions"""


