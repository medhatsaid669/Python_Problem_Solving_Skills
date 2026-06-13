# Recursive Functions 1

"""Problem and subproblems
● Sometimes we can decompose a problem into a set of sub-problems
● E.g. Print all prime numbers that are palindrome and < 1000000
● We have 2 sub-problems
○ def is_prime(n):
○ def is_palindrome(n):
● Now we iterate from 1 to 1000000
○ If the number satisfies the 2 conditions: count it
● What if the sub-problem is the same type as the problem? Recursion!"""

"""Recall the factorial
● factorial(6) = 1 * 2 * 3 * 4 * 5 * 6
● factorial(5) = 1 * 2 * 3 * 4 * 5
● factorial(4) = 1 * 2 * 3 * 4
● factorial(3) = 1 * 2 * 3
● factorial(2) = 1 * 2
● factorial(1) = 1
● Think for a few minutes:
○ What is relation between factorial(6) and factorial(5)?
○ Can you know factorial(6) if you know factorial(5)?"""

# Factorial

# def factorial(n):
#     res = 1
#
#     for i in range(2, n + 1):
#         res *= i
#
#     return res
#
# if __name__ == '__main__':
#     print(factorial(3))  # 1 * 2 * 3
#     print(factorial(4))  # 1 * 2 * 3 * 4
#
#     print(factorial(5))  # 1 * 2 * 3 * 4 * 5
#     # factorial(4)  * 5 = 120
#
#     print(factorial(6))  # 1 * 2 * 3 * 4 * 5 * 6 = 720
#     # factorial(5)      * 6 = 720
#     # factorial(4)  * 5 * 6 = 720
#     # factorial(3)*4* 5 * 6 = 720

"""Factorial: Problem and subproblem
● Let's say we want to solve factorial(6)
○ This is our problem
○ We can solve it directly with 1*2*3*4*5*6
● Another thinking is: can we think of it is
○ What is factorial(5)? A simpler subproblem
○ Would it help if u know its answer? Yes: 6 * factorial(5) =  factorial (6)
○ Same logic for factorial(5). It is 5 * factorial(4). 
● Going forever in smaller sub-problems? No
○ There must be a case where no more subproblems. We call it the base case
○ Factorial 1 = 1"""

# Factorial: Problem and subproblem
#
# def factorial1():
#     return 1    #    base case. No subproblems
#
# def factorial2():
#     return factorial1() * 2
#
# def factorial3():
#     return factorial2() * 3
#
# def factorial4():
#     return factorial3() * 4
#
# def factorial5():
#     return factorial4() * 5
#
# def factorial6():
#     return factorial5() * 6
#
# print(factorial6())


# Recursive Functions 2
"""Factorial: A recursive function
● A recursive function: Function that calls itself with smaller input (sub-problem) 
till calls reach a base case"""

# def factorial(n):
#     print("Function Call: factorial: n=", n)
#
#     if n == 1:      # base case
#         return 1
#     subproblem = factorial(n-1)
#     return subproblem * n
#
# print(factorial(6))

"""Let’s trace it
● Call Factorial(6)
○ If 6 == 1? False
○ Call Factorial (5) and multiply results with 6
■ If 5 == 1? False
■ Call Factorial (4) and multiply results with 5
● If 4 == 1? False
● Call Factorial (3) and multiply results with 4
○ If 3 == 1? False
○ Call Factorial (2) and multiply results with 3
■ If 2 == 1? False
■ Call Factorial (1) and multiply results with 2
● If 1 == 1? True
○ Return 1"""


# What did program print?

# def factorial(n):
#     print("Function Call: factorial: n=", n)
#
#     return factorial(n-1) * n
#
# print(factorial(6))

# Practice
# Print a Triangle (v1)

# def print_triangle(levels):
#     if levels == 0:
#         return
#
#     for i in range(0, levels):
#         print("*", end='')
#     print("")
#
#     print_triangle(levels - 1)
#
# print_triangle(5)

"""Print 3n+1 Sequence
● A 3n+1 goes as following
● Start from a number n
● If this number is even, next number in sequence is n / 2
● If this number is odd, next number in sequence is 3 * n + 1
● If this number is 1 = end of sequence
● E.g. Start from 5: 5 16 8 4 2 1
● E.g. Start from 6: 6 3 10 5 16 8 4 2 1 
● E.g. Start from 9: 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
● Write a recursive function to print it
○ Stop the video and try"""

# Print 3n+1 Sequence

# def print_3n_plus_1(n):
#     print(n, end=' ')
#
#     if n == 1:
#         return
#
#     if n % 2 == 0:
#         print_3n_plus_1(n // 2)
#     else:
#         print_3n_plus_1(3 * n + 1)
#
# print_3n_plus_1(6)  # 6 3 10 5 16 8 4 2 1


# Homework 1

"""Problem #1: Length of 3n+1 
● Implement 3n+1 function to compute the length of the sequence
● def length_3n_plus_1(n):
● E.g. length_3n_plus_1(6) ⇒ 9"""

# def length_3n_plus_1(n):
#     if n == 1:
#         return 1
#
#     if n % 2 == 0:
#         return 1 + length_3n_plus_1(n // 2)
#     else:
#         return 1 + length_3n_plus_1(3 * n + 1)
#
# print(length_3n_plus_1(6))  # 9 for sequence 6 3 10 5 16 8 4 2 1

"""Problem #2: Power function
●
def 
my_pow(value, p = 2):
● Return value * value ….. * value p times
● E.g. my_pow(7, 3) = 7 * 7 * 7 = 343
● Note: if p = 0, answer is 1
● P is positive integer"""

# def my_pow(value, p = 2):
#     if p == 0:
#         return 1
#
#     return value * my_pow(value, p - 1) # 7^5 = 7 * 7^4
#
# if __name__ == '__main__':
#     print(my_pow(7))        # 49
#     print(my_pow(7, 0))     # 1
#     print(my_pow(7, 3))     # 343


"""Problem #3: List sum
● Given a list of 0 or more numbers, find the sum among them"""

# def list_sum(lst):
#     if len(lst) == 0:
#         return 0
#
#     sub = list_sum(lst[1:])     # 1 2 3 4 5 6
#
#     return lst[0] + sub
#
# if __name__ == '__main__':
#     print(list_sum([]))           # 0
#     print(list_sum([5]))          # 5
#     print(list_sum([5, 7]))       # 12

"""Problem #4: List maximum
● Given a list of 1 or more numbers, find the maximum among them"""

# def list_max(lst):
#     first, *lst = lst
#
#     if not lst:
#         return first
#
#     if first > (sub := list_max(lst)):
#         return first
#
#     return sub
#
# if __name__ == '__main__':
#     print(list_max([5]))                            # 5
#     print(list_max([5, 7]))                         # 7
#     print(list_max(['most', 'saad', 'ibrahim']))    # saad

"""Problem #5: List average
● Given a list of 1 or more numbers, find the average among them"""

# def list_avg(lst):
#     if len(lst) == 0:
#         return 0
#
#     if len(lst) == 1:
#         return lst[0]
#
#     n = len(lst)
#     # This sublist is average of n-1 elements. Let's get the sum
#     sub = list_avg(lst[1:]) * (n-1)
#
#     return (lst[0] + sub) / n
#
# if __name__ == '__main__':
#     print(list_avg([5]))           # 5
#     print(list_avg([5, 7]))        # 6.0
#     print(list_avg([1, 2, 3, 4]))  # 2.5

"""Problem #6: List Increment v1
● Given a list of numbers, we would like to increment each element based on its 
position and the list length as following
○ Assume list has length N
○ Then first element is increased with N, the second with N-1, and so on till last with 1
○ Develop a function that returns a new list with the requested increment"""

# def list_increment(lst):
#     if len(lst) == 0:
#         return []
#
#     cur = lst[0] + len(lst)
#     return [cur] + list_increment(lst[1:])
#
# if __name__ == '__main__':
#     lst = [1, 8, 2, 10, 3]
#
#     print(list_increment(lst))  # [6, 12, 5, 12, 4]

"""Problem #7: List Accumulation v1
● Given a list of numbers, accumulate it
● E.g. list: 1 2 3 4 5 6 ⇒ 1, 3, 6, 10, 15, 21
○ 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5, 1+2+3+4+5+6"""

# def list_accumulate(lst):
#     if len(lst) <= 1:   # handling 2 base case with single condition
#         return lst
#
#     # at least 2 elements
#     head = list_accumulate(lst[:-1])
#     last = head[-1] + lst[-1]
#     head.append(last)
#     return head
#
# if __name__ == '__main__':
#     lst = [1, 8, 2, 10, 3]
#
#     print(list_accumulate(lst))  # [1, 9, 11, 21, 24]

