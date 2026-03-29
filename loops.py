# While Loops Homework 1

# Homework 1: Print Range
"""● Given a starting integer X and an ending integer Y, print all integers between
X and Y inclusive, each on a line.
● Input 3 7
● Output
○ 3
○ 4
○ 5
○ 6
○ 7"""
#
# start, end = map(int, input().split())
#
# while start <= end:
#     print(start)
#     start += 1

# Homework 2: Repeat Me
"""● Read integer N and string S.
● Print S repeated N times as below
● Input: 5 Hi
● Output: HiHiHiHiHi
● Note: we can use string * 5
○ Please use while loops"""

# n, str = input().split()
# n = int(n)
#
# while n:
#     print(str, end='')
#     n -= 1

# Homework 3: Print face down left angled triangle
"""● Read integer N. 
● Print a face down left angled triangle that has N rows as in picture"""

# n = int(input())
#
# row = n
# while row > 0:
#     stars_count = 1
#
#     while stars_count <= row:
#         print('*', end='')
#         stars_count += 1
#
#     print()
#     row -= 1


# Homework 4: Special Average
"""● Read integer N, followed by reading N numbers
○ Each on separate lines
● Print 2 values
○ The average of the numbers in odd positions (1st, 3rd, 5th, …)
○ The average of the numbers in even positions (2nd, 4th, 6th, …)
● Explantation
○ (10+20+30)/3 = 20
○ (100+200+600)/3 = 300"""

# even_sum, odd_sum, even_count, odd_count = 0, 0, 0, 0
# n = int(input())
#
# cnt = 1
# while cnt <= n:
#     value = float(input())
#
#     if cnt % 2 == 0:    # even position
#         even_sum += value
#         even_count += 1
#     else:               # odd position
#         odd_sum += value
#         odd_count += 1
#
#     cnt += 1
#
# print(odd_sum / odd_count, even_sum / even_count)

# While Loops Homework 2

# Special Calculator
"""● Design a small application that keeps asking the user 3 choices:
○ Enter 1 to sum integers from 1 to N
○ Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)
■ Expect 3 items. Operations are: + - * / // **
○ Enter 3 to end the program
● The user should input value from 1 to 3
○ Otherwise, inform that this is invalid and try again
● Take proper input from the user and compute the answer
○ See next console simulation"""

# while True:
#     print('\n\nMenu:')
#     print('Enter 1 to sum numbers from 1 to N')
#     print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)')
#     print('Enter 3 to end the program')
#
#     user_inp = input('\nEnter choice from 1 to 3: ')
#
#     if user_inp != '1' and user_inp != '2' and user_inp != '3':
#         print('Invalid Input...Try again')
#         continue
#
#     if user_inp == '1':
#         n = int(input('Enter a number: '))
#         sum = (n * (n+1))//2
#         print('Sum from 1 to', n, 'is', sum)
#     elif user_inp == '2':
#         num1, operation, num2 = input('Enter a simple expression: ').split()
#         num1, num2 = float(num1), float(num2)
#
#         # None is a value that means nothing assigned
#         result = None
#
#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '**':
#             result = num1 ** num2
#         else:
#             # / or //
#             if num2 == 0:
#                 print('Sorry: No way to compute this expression')
#             elif operation == '/':
#                 result = num1 / num2
#             else:
#                 result = num1 // num2
#
#         if result != None:
#             print('Expression value is ', result)
#     else:
#         break

# Homework 1: Print Diamond
"""● Read an integer N. Print diamond of 2N rows as below."""

"""
Let's print the upper triangle first
Let's assume N = 4, how many spaces and starts we print
Row 1	Spaces 3	Stars 1
Row 2	Spaces 2	Stars 3
Row 3	Spaces 1	Stars 5
Row 4	Spaces 0	Stars 7

Now we wanna develop formulas for number of spaces and number of starts
For a given 'row'
Spaces are: N - rows   	(3, 2, 1, 0)
Starts are: 2*row -1	(1, 3, 5, 7)

Now we just iterate for each row
print spaces
then print starts
"""

# n = int(input())
#
# row = 1
# while row <= n:
#     # Print N - rows spaces
#     stars_count = 1
#     while stars_count <= n - row:
#         print(' ', end='')
#         stars_count += 1
#
#     # Print 2*rows-1 spaces
#     stars_count = 1
#     while stars_count <= 2 * row-1:
#         print('*', end='')
#         stars_count += 1
#
#     print()
#     row += 1
#
#
# row = n
# while row > 0:
#     # Print N - rows spaces
#     stars_count = 1
#     while stars_count <= n - row:
#         print(' ', end='')
#         stars_count += 1
#
#     # Print 2*rows-1 spaces
#     stars_count = 1
#     while stars_count <= 2 * row-1:
#         print('*', end='')
#         stars_count += 1
#
#     print()
#     row -= 1


# Homework 2: Special multiples 1
"""● Read an integer N : print all numbers <= N that satisfy the following property
○ Either number is divisible by 8
○ Or divisible by both 4 and 3
● Input: 100
● Output: 0 8 12 16 24 32 36 40 48 56 60 64 72 80 84 88 96"""


# result = 0
# n = int(input())
#
# cnt = 0
#
# while cnt <= n:
#     if cnt % 8 == 0 or cnt % 3 == 0 and cnt % 4 == 0:
#         print(cnt, end=' ')
#
#     cnt += 1



# Homework 3: Special multiples 2
"""● Read an integer N (1 <= 30): Print the first N numbers that are 
○ multiple of 3 but not multiple of 4
● Input: 11
● Output: 3 6 9 15 18 21 27 30 33 39 42 
● Notice
○ 12 is divisible by both 3 and 4 ⇒ so excluded """

# n = int(input())
#
# cnt = 0
# current_number = 0
#
# while cnt < n:
#     if current_number % 3 == 0 and current_number % 4 != 0:
#         print(current_number, end=' ')
#         cnt += 1
#
#     current_number += 1


# Homework 4: Minimum of values
"""● Read T for number of test cases. 
● For each test case read integer N: For number of 
integers to read
● Then read N integers, each on a seperate line
● For each test case, print the minimum of the N 
integers.
● See picture
○ 2 for 2 test cases
■ The length of the first is 6
■ And the length of the second is 3"""

# total_cases = int(input())
#
# # Outer loop for cases
# while total_cases > 0:
#     numbers_cnt = int(input())
#
#     pos = 0
#     result = 0
#
#     # Inner loop to read a case
#     while pos < numbers_cnt:
#         value = int(input())
#
#         if pos == 0:
#             result = value
#         elif result > value:
#             result = value
#
#         pos += 1
#
#     print('Min value is:', result)
#     total_cases -= 1


# While Loops Homework 4

# Homework 1: Find NOs
"""● Read integer N, then read N strings (one per line). 
○ Print only the strings (of 2 letters). 
○ These 2 letters must be letter ‘N’ and letter ‘O’ (regardless of 
lower/upper case/order)
○ E.g. print “No”, “ON”, “no”  but ignore e.g. “YEs”, “Noooo”
○ That is, the word of 2 letters only N and O
○ See the picture"""

# total_cases = int(input())
#
# pos = 0
#
# while pos < total_cases:
#     str = input()
#
#     # there are 8 different ways to make 2 letters no in lower/upper cases
#     if str == "no" or str == "No" or str == "nO" or str == "NO" or \
#         str == "on" or str == "oN" or str == "On" or str == "ON":
#         print('Match:', str)
#
#     pos += 1
#
# # Observe \ in end of line 9
# # It allows us to split a long exprssion on several lines

# total_cases = int(input())
#
# pos = 0
#
# while pos < total_cases:
#     str = input()
#
#     # In future we will learn about methods such as lower
#     str = str.lower()
#     # now str is lower case. There is only 2 cases for the code
#
#     if str == "no" or str == "on":
#         print('Match:', str)
#
#     pos += 1

# The code only given for future reference. Skip if you can't get in 3 minutes

# Homework 2: Reverse number
"""● Read an integer N, then find its reverse integer R
○ Print R R*3
● input ⇒ Output
○ 123  ⇒ 321 963"""

# N = int(input())
#
# number = 0
#
# while N > 0:
#     last_digits = N % 10
#     N //= 10    # remove last digit
#
#     number = number * 10 + last_digits
#
# print(number, number * 3)

# In the future we will learn how to do that without the above math
# E.g.
# N = 1234
# str_num = str(N)        # convert to string
# str_num = str_num[::-1] # reverse string
# N = int(str_num)
# print(N, N*3)


# Homework 3: Multiplication table
"""● Read an integer N and M, then print NxM lines for their multiplication table.
● Input 3 4
● Output
○ 1 x 1 = 1
○ 1 x 2 = 2
○ 1 x 3 = 3
○ 1 x 4 = 4
○ 2 x 1 = 2
○ 2 x 2 = 4
○ 2 x 3 = 6
○ 2 x 4 = 8
○ 3 x 1 = 3
○ 3 x 2 = 6
○ 3 x 3 = 9
○ 3 x 4 = 12"""

# n, m = map(int, input().split())
#
# cnt_n = 1
#
# # first col loop
# while cnt_n <= n:
#     cnt_m = 1
#
#     # second col loop
#     while cnt_m <= m:
#         print(cnt_n, " x ", cnt_m, " = ", cnt_n * cnt_m)
#         cnt_m += 1
#
#     cnt_n += 1

# Homework 4: Special Sum
"""● Read integer T for number of test cases. 
● For each test case read integer N. 
● Then read N integers a, b, c, ….. On seperate lines
● Compute the sum of:
○ (a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……)
○ That is the k-th number is repeated k times
○ Don’t use the power operator (**)
● Expantation: 
○ 2 test cases
○ 3   5 7 2
■ (5 + 7*7 + 2*2*2)  = 62
○ 4  1 2 3 4
■ (1+2*2+3*3*3+4*4*4*4) = 288"""

# We need 3 nested loops
# loop over test cases
#   loop over reading numbers
#       loop to repeat the number K times (multiplication)


# T = int(input())
# # Loop on cases
# while T > 0:
#     N = int(input())
#     cnt_N, sum = 1, 0
#
#     # loop over reading a case
#     while cnt_N <= N:
#         value = int(input())
#         cnt_deep, result = cnt_N, 1
#
#         # Loop to compute the sum: a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……
#         while cnt_deep > 0:
#             result *= value
#             cnt_deep -= 1
#
#         sum += result
#         cnt_N += 1
#
#     print('Sum is', sum)
#     T -= 1


# For Loops Homework

# Homework 1: Printing X
"""● Read an Integer N, then print an X using * as following
○ N always odd"""
#
# n = int(input())
#
# for i in range(n):
#     for j in range(n):
#         if i == j or n - i - 1 == j:
#             print("*", end='')
#         else:
#             print(" ", end='')
#     print()


# Homework 2: Find Special Pairs
"""● Count How many X, Y numbers such that
○ X in range [50-300]
○ Y in range [70-400]
○ X < Y
○ (X+Y) divisible by 7
● Output
○ 8040
● After solving, think in minor optimizations"""

# cnt = 0
#
# for x in range(50, 301):
#     for y in range(70, 401):
#         if x < y and (x + y) % 7 == 0:
#             cnt += 1
#
# print(cnt)

# cnt = 0
#
# for x in range(50, 301):
#     '''
#     Let's speed it
#     We can always start from the right condition maximum(70, x+1)
#         Saves some Y iterations
#         Remove the x < y condition
#     '''
#     start = max(70, x+1)
#
#     for y in range(start, 401):
#         if (x + y) % 7 == 0:
#             cnt += 1
#
# print(cnt)


# Homework 3: Find all quadruples
"""● Count how many integer (a, b, c, d) with the following property:
○ 1 <= a, b, c, d <= 200
○ a + b = c + d
● Output:
○ 5333400
● Code it once using 4 loops  (very slow!)
● Code it once using 3 loops only
● In future: you can do it using 2 loops only!"""

# count = 0
# for a in range(1, 201):
#     for b in range(1, 201):
#         for c in range(1, 201):
#             for d in range(1, 201):
#                 count += (a + b == c + d)
#
# print(count)

# count = 0
# for a in range(1, 201):
#     for b in range(1, 201):
#         for c in range(1, 201):
#             d = a + b - c   # lets' compute d
#             if 1 <= d <= 200:
#                 count += 1
#
# print(count)

# Homework 4: Is Prime?
"""● Read an integer N (< 500) and print YES if it is prime, otherwise NO
○ A prime number is greater than 1 AND cannot be formed by multiplying two smaller numbers. 
■ In other words, number%whatever != 0
■ The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.
● Input ⇒ Output 
○ 13 ⇒ YES           (only 1 * 13)
○ 12 ⇒ NO             (E.g. 12 = 2 *6, so 12 can be divided by 2 or 6)"""



# number = int(input())
#
# if number <= 1:
#     print("NO")
# else:
#     is_ok = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_ok = False
#             break
#
#     if is_ok:
#         print("YES")
#     else:
#         print("NO")


# Homework 5: Print Primes
"""● Read integer N (<500), then print all prime numbers <= N  
● Input ⇒ Output
○ 18 ⇒ 2 3 5 7 11 13 17"""

# max_num = int(input())
#
# for number in range(2, max_num+1):
#     is_ok = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_ok = False
#             break
#
#     if is_ok:
#         print(number, end=' ')

# Homework 6: Digits sum in range
"""● Read three integers N, A, B. 
● Print the summation of the numbers between 1 and N whose sum of digits is 
between A and B.
● Input ⇒ Output
○ 20 2 5 ⇒ 84
■ Numbers whose sums of digits are between 2 and 5, are: 2,3,4,5,11,12,13,14, 20.
● E.g. digits sum of 13 is 4 : which is between (2, 5)
○ 10 1 2 ⇒ 13
○ 100 4 16 ⇒ 4554"""

# n, a, b = map(int, input().split())
# total = 0
#
# for i in range(1, n+1):
#     tmp = i     # be careful - take copy
#     digits_sum = 0
#
#     while tmp > 0:
#         digits_sum += tmp % 10
#         tmp //= 10
#
#     if a <= digits_sum <= b:
#         total += i
#
# print(total)





























