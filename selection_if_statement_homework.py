# Selection Homework 1

# Homework 1: Arithmetic

"""● Read 2 integers A, B and print based on following cases:
○ if both are odd print their product  A*B
○ if both are even print their division A/B   (float division / assume B != 0)
○ if the first is odd and the second is even then find their sum A+B
○ if the first is even and the second is odd then find their subtraction A-B
● Inputs ⇒ outputs
○ 5 7 => 35
○ 12 2 => 6
○ 5 6 => 11
○ 12 3 => 9"""

# a, b = map(int, input().split())
#
# is_a_even = a % 2 == 0
# is_b_even = b % 2 == 0
#
# if not is_a_even and not is_b_even:
#     print(a * b)
# elif is_a_even and is_b_even:
#     print(a / b)
# elif not is_a_even and is_b_even:
#     print(a + b)
# else:
#     print(a - b)

# Homework 2: Sort 3 numbers
"""● Given 3 integers, sort (order) them in ascending order and print them .
● Inputs ⇒ outputs
○ 1 2 3 ⇒ 1 2 3
○ 1 3 2 ⇒ 1 2 3
○ 2 1 3 ⇒ 1 2 3
○ 2 3 1 ⇒ 1 2 3
○ 3 1 2 ⇒ 1 2 3
○ 3 2 1 ⇒ 1 2 3
● Do you notice there are only 6 ways to permutate 3 numbers!"""
#
# a, b, c = map(int, input().split())
#
# # To understand: apply on 3 2 1
#
# if b < a:  # Swap them:
#     a, b = b, a
#
# # Now a and b are in correct order: e.g. 2 3 1
#
# if c < b:  # Swap them
#     b, c = c, b
#
#     # Now b, are correct
#     # But a, may not be again with b: e.g. 2 1 3
#
#     if b < a:      # Swap them
#         a, b = b, a
#
#         # Now 1 2 3
#
# print(a, b, c)

# Homework 3: Maximum but constrained
"""● Given 3 integers, you have to find the biggest one of them which is < 100. 
○ Print -1 if no such number
● Inputs
○ 22 90 115 ⇒ 90
■ Here [20 90] are only < 100. Maximum (20, 90) = 90
○ 200 300 400 ⇒ -1
■ All of them are > 100, so no answer
○ 50 100 150 ⇒ 50
■ Only 50 is < 100.
○ 10 30 20 ⇒ 30
■ The 3 numbers < 100, so their max is 30"""

# a, b, c = map(int, input().split())
#
# # Assume numbers >= 0
# res = -1
# if res < a < 100:
#     res = a
#
# if res < b < 100:
#     res = b
#
# if res < c < 100:
#     res = c
#
# print(res)
#
# # test: -10 -20 -30_oop

# a, b, c = map(int, input().split())
#
# if a >= 100 and b >= 100 and c >= 100:
#     res = -1
# else:
#     # First, find any valid value to initalize
#     if a < 100:
#         res = a
#     elif b < 100:
#         res = b
#     else:
#         res = c
#
#     if res < a < 100:
#         res = a
#
#     if res < b < 100:
#         res = b
#
#     if res < c < 100:
#         res = c
#
# print(res)
#
# # test: -10 -20 -30_oop


# Homework 4: Conditional Count
"""● Write a program that reads number X, then other 5 numbers. Print 2 values:
○ How many numbers <= X
○ How many numbers > X
○ Any relation between these 2 outputs?
● Inputs
○ 10       300 1 5 100 200
○ Output: 2 3
○ Explantation
○ 2 numbers (1, 5) are <= 10
○ 3 numbers (100, 200, 300) are > 10 """

# x, a1, a2, a3, a4, a5 = map(float, input().split())
# cnt = 0
#
# # We can use if else, but for educational purpose:
# cnt += a1 <= x
# cnt += a2 <= x
# cnt += a3 <= x
# cnt += a4 <= x
# cnt += a5 <= x
#
# # clearly the 2 values just complement each others
# print(cnt, 5 - cnt)

# Homework 1: Find Maximum of 10 numbers
"""● Read 10 numbers and find which of them has the biggest value and print it.
● Inputs (each integer on a seperate line)
○ 1
○ 67
○-9
○ 88
○-45
○ 129
○ 90
○ 65
○ 77
○ 34 
● Output ⇒ 129
● Restriction: In your whole code there should be 2 variables defined ONLY"""

# # Read first number
# result = float(input())
#
# # Read other 9 numbers
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# num = float(input())
# if result < num:
#     result = num
#
# print(result)

# Homework 2: Find Maximum up to 10 numbers
"""● Read an integer N (1 <= N <= 10)
● Then read N numbers, find which of them has the biggest value and print it.
● Inputs (but they will be on seperate lines)
○ 5  1 3 2 4.5 2 ⇒ 4.5
■ 5 means read 5 integers
■ Then we read them [1 3 2 4.5 2]. Their maximum is 4.5
○ 10 1  67  -9  88  -45  129  90  65  77  34 ⇒ 129
■ Same as last homework. This time we are given first N (10)"""

# cnt = int(input())
#
# # read first number
# result = float(input())
# cnt -= 1
#
# # read UP to 9 times
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num
#
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# print(result)

# Homework 1: Intervals
"""● Read an integer X then read 6 integers s1, e1, s2, e2, s3, e3
○ These 6 numbers are for 3 interval
○ Each Interval is a range [start, end]
○ Number X in a range if start <= X <= end
○ E.g 7 in range [5, 12] but not in range [10, 20]
● Print how many intervals that 
X is part of
● Inputs
○ 7        1 10    5 6     4 40 ⇒ 2
■ Number 7 exists in 2 intervals [1, 10] and [4, 40]
○ 10    5 15     6 100    3 30 ⇒ 3
■ 10 exists in the 3 intervals  [5 15], [6 100], [3 30]
○ 10    100 200    100 101   120 170 ⇒ 0       [doesn’t exist in any interval]"""

# x, s1, e1, s2, e2, s3, e3 = map(int, input().split())
#
# #Read start and end, see if X is between them or not, times
# cnt = 0
# cnt += s1 <= x <= e1
# cnt += s2 <= x <= e2
# cnt += s3 <= x <= e3
#
# print(cnt)

# Homework 2: Two Intervals Intersection
"""● Read 4 integers representing 2 intervals and print their intersection interval. If 
they don’t intersect, print -1
● Inputs
○ 1 6     3 8    ⇒ 3  6
■ Interval [1 6] and [3 8] only intersects at [3, 6]
■ Why: interval [1, 6] has numbers: {1, 2, 3, 4, 5, 6}
■ And: interval [3, 8] has numbers: {3, 4, 5, 6, 7, 8}
■ So the intersection is {3, 4, 5, 6} = [3, 6]
○ 1 15  20 30 ⇒ -1"""

s1, e1, s2, e2 = map(int, input().split())

if e1 < s2 or e2 < s1:
    print(-1)		# One of them ends before start of the another
else:
    # This is tricky. Trying to list all cases will be hard and buggy
    # You need to notice which ones came first
    # Then consider the possible cases (e.g. one of them completely inside the second)

    # However, thinking makes it easier
    # The intersection starts at the maximum of the starts
    # The intersection ends at the minimum of the ends
    # Draw some examples

    if s1 < s2:
        s1 = s2	    # maximum of (s1, s2)
    if e1 > e2:
        e1 = e2	    # minimum of (e1, e2)

    print(s1, e1)

'''
Cases
1 15  20 30_oop		==> -1
20 30_oop 1 15		==> -1
1 6    1 6		==> 1 6
1 6    1 3		==> 1 3
1 6    2 3		==> 2 3
1 6    3 8		==> 3 6
3 8    1 6		==> 3 6
'''





























