# Function Homework 1

"""Homework 1: Special Multiplication
● Develop function:
def
special_multiplication(string):
● It returns a string where each character is repeated according to its position
○ Input: abcxf
○ Output: abbcccxxxxfffff
○ Observe
■ a repeated once
■ b twice
■ c 3 times
■ x 4 times
■ And so on"""

# def special_multiplication(string):
#     result = ''
#     for idx, char in enumerate(string):
#         result += char * (idx+1)
#     return result
#
# print(special_multiplication('abcxf'))


"""Homework 2: Max of 6 numbers
● Develop these 4 functions to help 
compute maximum of 6 numbers
● Each function should be only a single 
line of code
○ Hint: make use of the other functions """

# def my_max2(a, b):
#     if a > b:
#         return a
#     return b
#
# def my_max3(a, b, c):
#     return my_max2(a, my_max2(b, c))
#
# def my_max4(a, b, c, d):
#     return my_max2(a, my_max3(b, c, d))
#
# def my_max5(a, b, c, d, e):
#     return my_max2(a, my_max4(b, c, d, e))
#
# def my_max6(a, b, c, d, e, f):
#     return my_max2(a, my_max5(b, c, d, e, f))
#
# print(my_max6(5, 3, 8, 2, 10, 3))


"""Homework 3: Get nth-prime
● Implement the following 2 functions:
● is_prime(num);
○ Return true if number is prime (it is not divisible by any number 
> 1
● nth_prime(n);
○ Return the n-th prime number. It should use is_prime function
○ E.g nth_prime(6) = 13
■ Recall primes are: 2, 3, 5, 7, 11, 13, 17, 19"""

# def is_prime(num):
#     if num <= 1:
#         return False
#
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
#
# def nth_prime(n):
#     start = 2
#     while n > 0:
#         if is_prime(start):
#             n -= 1
#             if n == 0:
#                 return start
#         start += 1
#
#     return -1   # not reachable
#
#
# for i in range(1, 10):
#     print(i, nth_prime(i))

"""Homework 4: Get nth-fibonacci
● Fibonacci is a popular sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, …
○ Every number is sum of last 2 numbers
○ E.g. 13 = 5 + 8
● Write function: nth_fib(n)
○ That returns the nth term
○ Hint: Simple loop"""

# def nth_fib(n):
#     def nth_fib(n):
#
#         if n == 1:
#             return 0
#         if n == 2:
#             return 1
#         # note: we can merge above 2 lines in single condition. Try
#
#         a, b = 0, 1
#         n -= 2
#
#         while n > 0:
#             c = a + b
#             a = b
#             b = c
#             n -= 1
#         return c
#
#     for i in range(1, 10):
#         print(i, nth_fib(i))


"""Recall: Special Calculator 
● Design a small application that keeps asking the user 3 choices:
○ Enter 1 to sum integers from 1 to N
○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
■ Expect 3 items. Operations are: + - * / // **
○ Enter 3 to end the program
● The user should input value from 1 to 3
○ Otherwise, inform that this is invalid and try again
● Take proper input from the user and compute the answer
○ See next console simulation"""

"""Rewrite the previous code as functions
● Print_menu: print the menu and read 
a valid choice
○ Don’t return unless go number from 1 to 3
● Divide is just divide logic for handling 
/ 0
○ If / 0 or // 0 return None
● Expression to parse e.g. x + y
● Interface: the core logic
○ Print, if else on choices
● Got lost? Just do your own rewriting """

# Your ToDo: Provide Docstring for every function

# def print_menu():
#     while True:
#         print('\n\nMenu:')
#         print('Enter 1 to sum numbers from 1 to N')
#         print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)')
#         print('Enter 3 to end the program')
#
#         user_inp = input('\nEnter choice from 1 to 3: ')
#
#         if user_inp != '1' and user_inp != '2' and user_inp != '3':
#             print('Invalid Input...Try again')
#             continue
#         else:
#             return user_inp
#
#
# def sum_1_to_n():
#     n = int(input('Enter a number: '))
#     sum = (n * (n+1))//2
#     print('Sum from 1 to', n, 'is', sum)
#
#
# def divide(num1, num2, operation):
#     # / or //
#
#     #  See this function prints nothing. This is a better design
#     # It is only responsible to compute answer if possible
#     # someone else should print
#
#     if num2 == 0:
#         result = None
#     elif operation == '/':
#         result = num1 / num2
#     else:
#         result = num1 // num2
#
#     return result
#
#
# def expression():
#     num1, operation, num2 = input('Enter a simple expression: ').split()
#     num1, num2 = float(num1), float(num2)
#
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '**':
#         result = num1 ** num2
#     else:
#         result = divide(num1, num2, operation)
#
#     if result != None:
#         print('Expression value is ', result)
#     else:
#         print('Sorry: No way to compute this expression')
#
#
# def calculator_interface():
#     while True:
#         user_inp = print_menu()
#
#         if user_inp == '1':
#             sum_1_to_n()
#         elif user_inp == '2':
#             expression()
#         else:
#             break
#
#
# calculator_interface()








