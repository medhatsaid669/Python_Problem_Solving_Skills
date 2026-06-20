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

# Homework 2
"""Problem #1: List Increment v2
● This is the same task as in homework 1, but this time the change is inplace
○ Hint: consider some default argument"""

# def list_increment(lst, position = 0):
#     if len(lst) == position:
#         return
#
#     lst[position] += len(lst) - position
#     list_increment(lst, position + 1)
#
# if __name__ == '__main__':
#     lst = [1, 8, 2, 10, 3]
#     list_increment(lst)
#
#     print(lst)  # [6, 12, 5, 12, 4]

"""Problem #2: List Accumulation v2
● This is the same task as in homework 1, but this time the change is inplace"""
#
# def list_accumulate(lst, ln = None):
#     if ln is None:
#         ln = len(lst)
#
#     if ln <= 1:
#         return
#
#     list_accumulate(lst, ln - 1)    # accumulate first N-1 elements
#     # Last element of N-1 has all accumulation of first N-1 elements (lst[ln - 2])
#     lst[ln - 1] += lst[ln - 2]
#
# if __name__ == '__main__':
#     lst = [1, 8, 2, 10, 3]
#     list_accumulate(lst)
#
#     print(lst)  # [1, 9, 11, 21, 24]

"""Problem #3: Left-Max
● Given list of numbers, return a list where  each element at position i to be the 
maximum of numbers from 0 to index i
● E.g. input 1 3 5 7 4 2 ⇒ [1, 3, 5, 7, 7, 7]"""

# def left_max(lst):
#     if len(lst) <= 1:   # handling 2 base case with single condition
#         return lst
#
#     # at least 2 elements
#     head = left_max(lst[:-1])
#     last = max(head[-1], lst[-1])
#     head.append(last)
#     return head
#
# if __name__ == '__main__':
#     lst = [1, 3, 5, 7, 4, 2]
#
#     print(left_max(lst))  # [1, 3, 5, 7, 7, 7]

"""Problem #4: Right-Max
● Given list of numbers, return a list where  each element at position i to be the 
maximum of numbers from index i to end of the list
● E.g. input 1 3 5 7 4 2 ⇒ [7, 7, 7, 7, 4, 2]"""

# def right_max(lst):
#     if len(lst) <= 1:   # handling 2 base case with single condition
#         return lst
#
#     # at least 2 elements
#     head = right_max(lst[1:])
#     last = max(head[0], lst[0])
#     head.insert(0, last)
#     return head
#
# if __name__ == '__main__':
#     lst = [1, 3, 5, 7, 4, 2]
#
#     print(right_max(lst))  # [7, 7, 7, 7, 4, 2]

"""Problem #5: Is Palindrome
● Given a list of items, check recursively if it is a palindrome or not 
○ We can read it the same from both directions"""

# def is_palindrom(lst):
#     if len(lst) <= 1:
#         return True
#
#     if lst[0] != lst[-1]:
#         return False
#
#     return is_palindrom(lst[1:-1])
#
# if __name__ == '__main__':
#     lst = [1, 3, 5, 7, 4, 2]
#
#     print(is_palindrom([]))  # True
#     print(is_palindrom([5]))  # True
#     print(is_palindrom([5, 7]))  # False
#     print(is_palindrom([5, 5]))  # True
#     print(is_palindrom([1, 2, 3, 2, 1]))  # True
#     print(is_palindrom([1, 2, 3, 3, 2, 1]))  # True
#     print(is_palindrom([1, 2, 3, 4, 2, 1]))  # False

"""Problem #6: startswith
● The startswith() function returns True if a string starts with the specified 
prefix(string). If not, it returns False."""

# def startswith(main, pattern):
#     if not pattern:
#         return True
#
#     if not main:
#         return False
#
#     if main[0] != pattern[0]:
#         return False
#
#     return startswith(main[1:], pattern[1:])
#
# if __name__ == '__main__':
#     print(startswith("abcdefg", ""))        # True
#     print(startswith("abcdefg", "abcd"))    # True
#     print(startswith("abcdefg", "ax"))      # False
#     print(startswith("abcd", "abcdefg"))    # False
#     print(startswith("abcd", "abcd"))       # True
#     print(startswith("", ""))               # True

"""Problem #7: Trace 
● Without running code on the right
● Guess the output
● What are these methods doing"""

# def do_something1(n):
#     if n:
#         print(n%10, end='')
#         do_something1(n//10)
#
# def do_something2(n):
#     if n:
#         do_something2(n//10)
#         print(n % 10, end='')
#
# if __name__ == '__main__':
#     do_something1(12345)
#     print()
#     do_something2(12345)
#     do_something2(0)

"""do_something1 prints the number backward, but do_something2 prints it in normal order
Both functions don't handle the zero"""


# Homework 3
"""Problem #1: Count primes
● Implement function: 
def count_primes(start, end)
○ It counts prime numbers in this range
● Don’t use loops at all. 
● Don’t use any python functions"""

# def is_prime(m, cur_test_number = 3):
#     if m == 2:
#         return True
#
#     if m <= 1 or m % 2 == 0:
#         return False
#
#     if m == cur_test_number:
#         return True
#
#     if m % cur_test_number == 0:
#         return False
#
#     return is_prime(m, cur_test_number + 2)
#
# def count_primes(start, end):
#     if start > end:
#         return 0
#
#     result = is_prime(start)
#     result += count_primes(start + 1, end)
#
#     return result
#
# print(count_primes(10, 20))          # 4
# print(count_primes(10, 200))         # 42
#
# #print(count_primes(10, 2000))       # RecursionError

"""Problem #2: Greedy Robot
● Read an integer matrix (all distinct values)
● A robot starts at cell (0, 0). 
● Take the value in the current cell and moves. 
○ It can move only one step to either: Right, Bottom or the diagonal. 
○ It always selects the destination cell that has maximum value. 
● Print the total values the robot collects
Problem #2: Greedy Robot
● Write a function that takes a matrix and compute the path sum"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
# def is_within_grid(r, c, rows, cols):
#     return 0 <= r < rows and 0 <= c < cols
#
# def get_neibghours(i, j, rows, cols):
#     dir = [(1, 0), (0, 1), (1, 1)]
#     return [(r, c) for di, dj in dir
#             if is_within_grid(r := i + di, c:= j + dj, rows, cols)]
#
# def argmax(lst):
#     return lst.index(max(lst))
#
# def get_path_sum(matrix, r = 0, c = 0): # from the old homework
#     total_sum = matrix[r][c]
#     rows, cols = len(matrix), len(matrix[0])
#
#     if not (positions := get_neibghours(r, c, rows, cols)):
#         return total_sum
#
#     values = [matrix[i][j] for i, j in positions]
#     r, c = positions[argmax(values)]
#
#     total_sum += get_path_sum(matrix, r, c)
#
#     return total_sum
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#     print(get_path_sum(matrix))

"""Problem #3: Standard Max
● In this task, we would like to implement a max function to almost behave like 
standard one: what we pass, return and raised errors!
○ The recursive part of this function is trivial, like what we met
○ Make use of this task to think how things in professional development are done"""
#
# # If u know smarter ways to do this code, GIVEN what is taught in the course so far, share with me
# # In practice, we may implement it in more safer way (e.g current TypeError/ValueError) below are a bit risky
#
# # instead of using None as default, which make it hard for others, we define our temp class
# class _DefaultMarker:
#     pass
#
# __special_default_object = _DefaultMarker() # internal dummy special object
#
# def _my_max(*iterable, key = None):
#     first, *iterable = iterable
#
#     if not iterable:
#         return first    # if no more elements, let's return it
#
#     remain = _my_max(*iterable)
#
#     if key is None:
#         return first if first > remain else remain
#
#     first_key, remain_key = key(first), key(remain)
#
#     return first if first_key > remain_key else remain
#
#
# def my_max(*iterable, default = __special_default_object, key = None):
#     # This function will try to handle the different errors
#     # If no errors, it will call the actual maximization
#     try:
#         # Make sure at least 1 element
#         first, *sub_iterable = iterable
#     except:
#         raise TypeError('max expected 1 argument, got 0') from None
#         # without from None: you see 2 exceptions: original one (ValueError) and our TypeError
#
#     if not sub_iterable:    # just single item: either iterable or not. If iterable, it might be empty, e.g. []
#         try:
#             # Let's try to unpack it
#             return _my_max(*first)
#         except TypeError:
#             raise TypeError(f"'{type(first).__name__}' object is not iterable") from None
#             # The step (*first) will fail as * expects first to be iterable. Input e.g. 15
#         except ValueError:
#             if default is not __special_default_object:
#                 return default
#             raise ValueError('my_max() arg is an empty sequence') from None # Empty such as []
#             # It will happen from the unpacking in _my_max: first, *iterable = iterable
#
#     # # At least 2 items: let's call our max now
#     return _my_max(*iterable, key = key)
#
# if __name__ == '__main__':
#     #my_max = max   # uncomment to test python max
#
#     print(my_max(2, 5))                       # 5
#     print(my_max([10, 3, 60, 20]))            # 60
#     print(my_max(10, 3, 6, 20))               # 20
#     print(my_max({5, 7, 1}))                  # 7
#     print(my_max([5, 1], [4, 9]))             # [5, 1]
#     print(my_max('1234'))                     # 4
#     print(my_max('1234', '98'))               # 98
#     print(my_max('1234', '98', key = len))    # 1234
#     print(my_max([5, 1], [4, 9], key = sum))  # [4, 9]
#
#     # Don't show any other internal exceptions
#     #print(my_max())                # TypeError: max expected 1 argument, got 0
#     #print(my_max(default = -1))    # TypeError: max expected 1 argument, got 0
#     #print(my_max([]))              # ValueError: max() arg is an empty sequence
#     print(my_max([], default = None)) # None
#     #print(my_max(-15))    # TypeError: 'int' object is not iterable
#     #print(my_max(3, [4])) # TypeError: '>' not supported between instances of 'list' and 'int'

"""Problem #4: Deep Reverse v1
● The standard reverse function/method only reverse the top level
● What if we have list of list 
list and we would like to
reverse all of them, 
regardless how deep?
● Develop in-place function"""

# def deep_reverse(lst):
#     for item in lst:    # reverse every item
#         if isinstance(item, list):
#             deep_reverse(item)
#
#     lst.reverse()       # reverse list itself
#
# if __name__ == '__main__':
#
#     lst = [1, [2, 3, 4], [5, 6]]
#     lst.reverse()   # top level reverse ONLY
#     print(lst)  # [[5, 6], [2, 3, 4], 1]
#
#     lst = [1, [2, 3, 4], [5, 6]]
#     deep_reverse(lst)   # reverse very deep lists
#     print(lst)  # [[6, 5], [4, 3, 2], 1]
#
#     lst = [1, [2, 3, 4], [5, [6, 7, 8]]]
#     deep_reverse(lst)
#     print(lst)  # [[[8, 7, 6], 5], [4, 3, 2], 1]
#
#     lst = [1, [2, 3, 4], [5, [6, 7, [8, 9.5, 'hey']]]]
#     deep_reverse(lst)
#     print(lst)  # [[[['hey', 9.5, 8], 7, 6], 5], [4, 3, 2], 1]

"""Problem #5: Deep Reverse v2
● The exact problem, but consider:
○ The function is not inplace. Return a new deeply reversed list
○ Implement in a single line!"""

# def deep_reverse(lst):
#     return list(reversed([item if not isinstance(item, list) else deep_reverse(item) for item in lst]))
#
# if __name__ == '__main__':
#     lst = [1, [2, 3, 4], [5, 6]]
#     print(deep_reverse(lst))    # [[6, 5], [4, 3, 2], 1]
#
#     lst = [1, [2, 3, 4], [5, [6, 7, 8]]]
#     print(deep_reverse(lst))    # [[[8, 7, 6], 5], [4, 3, 2], 1]
#
#     lst = [1, [2, 3, 4], [5, [6, 7, [8, 9.5, 'hey']]]]
#     print(deep_reverse(lst))    # [[[['hey', 9.5, 8], 7, 6], 5], [4, 3, 2], 1]

"""Problem #6: Fibonacci
● Implement fibonacci: def fibonacci(n)
○ Recall fibonacci sequence: 1 1 2 3 5 8 13 21 35
○ E.g. fibonacci(6) = 13
○ Recall that: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2). E.g. fib(6) = fib(5)+fib(4) =13
■ So it calls 2 subproblems of its type
● Can u compute fibonacci(35)? fibonacci(40)? fibonacci(50)? More?
○ Why? Any work around? Hint: Save the intermediate results"""

# memory = None
#
# def fib(n):
#     if n <= 1:
#         return 1
#
#     global memory
#     if memory is None:  # first call
#         memory = [-1] * (n+1)   # create n+1 list entries, intialize to -1
#
#     if memory[n] != -1:
#         return memory[n]        # computed already. Just return it
#
#     memory[n] = fib(n-1) + fib(n-2)
#     return memory[n]    # we can merge these 2 lines
#
# if __name__ == '__main__':
#     memory = None
#     print(fib(6))
#
#     memory = None
#     print(fib(35))  # 14930352
#
#     memory = None
#     print(fib(50))  # 20365011074
#
#     memory = None
#     print(fib(800))  # 225591516161936330872512695036072072046011324913758190588638866418474627738686883405015987052796968498626

