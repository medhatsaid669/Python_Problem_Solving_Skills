# Homework 1: Create logic!
"""● Write a program that reads 3 integers about the class room
○ Number of boys (nb), number of girls (ng), number of teachers (nt)
● Prepare and print a boolean variable for
these cases:
● nb greater than 25
● ng less than or equal to 30
● nb > 20 and nt > 2 or ng > 30 and nt > 4
● Either nb < 60 or ng < 70
● Neither nb >= 60 nor ng >= 70
● nb is 10 more students than ng
● Difference between nb and ng is more than 10 or nt > 5
● Either nb is 10 more students than ng or ng is 15 more students than nb"""

# nb, ng, nt = map(int, input().split())
#
# # nb greater than 25
# print(nb > 25)
#
# # ng less than or equal to 30_oop
# print(ng <= 30)
#
# # nb > 20 and nt > 2 or ng > 30_oop and nt > 4
# print(nb > 20 and nt > 2 or ng > 30 and nt > 4)
#
# # Either nb < 60 or ng < 70
# print(nb < 60 or ng < 70)
#
# # Neither nb >= 60 nor ng >= 70
# print(  not nb >= 60 and not ng >= 70 )
#
# # nb is 10 more students than ng
# print(nb == ng + 10)
#
# # Difference between nb and ng is more than 10 or nt > 5
# print(nb - ng > 10 or nt > 5)
#
# # Either nb is 10 more students than ng or ng is 15 more students than nb
# print(nb == ng + 10 or ng == nb + 15)

# Homework 2: Simplify expressions

"""● For each expression:
○ Manually Simplify it step by step to finally be a T or F
● T and T and F and T                                # False
● T and T and F and T or T and T                     # True
● T and T and T and T or T and (T or F)              # True
● T and T and T or T and (F or (T and (T and T)))    # True
● T and T or T and F and T or T and T and F or (T and (T or F))        # True
● T and T or T and F and T or (T and T and F or (T and (T or F)))      # True
● (T and T or T and F and T or T) and T and F or (T and (T or F))      # True
● T and T or T and (F and T or T and T) and F or (T and (T or F))"""   # True

# Division and Modulus

# Homework 1: Averages

"""● Write a program that reads 5 numbers and print the following:
○ A) Their average
○ B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
○ C) The average of the first 3 numbers divided by the average of the last 2 numbers.
○ What is the math relation between B and C?
● Input 1 2 3 4  5
○ 3
○ 0.666666667
○ 0.444444444"""

# a1, a2, a3, a4, a5 = map(float, input().split())

# avg1 = (a1 + a2 + a3 + a4 + a5) / 5.0   # A
# sum1 = (a1 + a2 + a3) / (a4 + a5)       # B
# first3_avg = (a1 + a2 + a3) / 3.0
# last2_avg = (a4 + a5) / 2.0
# avg2 = first3_avg / last2_avg           # C

# print(avg1, sum1, avg2)
# print(sum1 * 2/3)                       # C = 2/3 B


# Homework 2: Fractional Part

"""● Write a program that reads 2 numbers a, b and divides them (a/b), but prints 
only the fraction part
● Input: 201 25
● Output: 0.04
○ Notice: 201 / 25 = 8.04
○ We only want the fraction part: 0.04
● Note:
○ Floats are approximations. So output like 0.039999999 is valid too"""

# a, b = map(float, input().split())
#
# result1 = a/b
# result2 = a//b
# result = result1 - result2


# Homework 3: Our remainder

"""● We know N % M computes the remainder of division
● Write a program that reads 2 positive integers and print such reminder without 
using the modulus operator %
● Input: 27 12
● Output: 3
○ Remember in math: 27 % 12 = 3"""

# n, m = map(int, input().split())
#
# # let's try 13/5
# # 13/5 = 2  [2 complete units, each is 5]
# # 2*5 = 10  [total complete units]
# # Reminder is 13-10 = 3. This number generates the fractional part
# result = n - (n // m) * m
#
# print(result)

# Division and Modulus

# Homework 1: Is even?

"""● The following code, reads an integer and computes a boolean if the number is 
even in 3 different ways. The number can be +ve or -ve.
● Fill in the is_even to solve the problem in 3 ways as following
● Using only %2
● Using only %10
● Using only /2"""

# num = int(input())
#
# # Is even using %2
# is_even1 = num % 2 == 0
#
# # is even using /2
# by2 = num / 2.0         # this is either X.0 or X.5  try 10, 11
# by2 = by2 - num//2    # Remove X. This is now either 0 for even or 0.5 for odd
# is_even2 = by2 == 0
#
# # is even using %10
# last_digit = num % 10	    # even last digit is 0, 2, 4, 6, 8
# is_even3 = last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8
#
# print(is_even1, is_even2, is_even3)
#
# # If using both / and //
# is_even4 = num / 2 == num // 2
# print(is_even4)


# Homework 2: Last 3 digits sum

"""● Write a program that reads an integer and prints the sum of its last 3 digits.
● Inputs ⇒ Outputs examples
○ 15     ⇒ 6     
○ 125    ⇒ 8  
○ 1000   ⇒  0
○ 1001   ⇒ 1
○ 1234   ⇒ 9
○ 99999  ⇒ 27"""

# n = int(input())
#
# # remember
# # number % 10   => gets the last digit
# # number // 10  => removes the last digit
#
# # logic: get digit, remove it. Apply 3 times to get the last 3 digits
#
# last1 = n % 10
# n = n // 10
#
# last2 = n % 10
# n //= 10
#
# last3 = n % 10
# n //= 10
#
# sum = last1 + last2 + last3
# print(sum)

# Homework 3: 4th digits from the end

"""● Write a program that reads an integer and print the 4th from the right side. If 
no such digit, print 0
● Inputs => outputs
○ 15 => 0
○ 125 => 0
○ 1000 => 1
○ 5001 => 5
○ 1234 => 1
○ 654321 => 4
○ 99999 => 9"""

# n = int(input())
#
# # /1000 => removes last 3 digits
#
# n_without_last_3_digits = n // 1000
#
# # %10 get digit = 4th
# print (n_without_last_3_digits % 10)


# Homework 1: 100 or 7?

"""● Write a program that reads an integer and print 100 if number is even or 7 if 
number is odd
○ E.g. for input 8 ⇒ 100
○ E.g. for input 133 ⇒ 7"""

# num = int(input())
# is_even = num % 2 == 0
# is_odd = num % 2 == 1
# result = is_even * 100 + is_odd * 7
# print(result)


# Homework 2: Years!

"""● Assume a year is 12 months, but each month is 30 days
○ That is a year has 12 * 30 =  360 days
● Read an integer: whole number of days of someone age. Print 3 numbers
○ Total years     total months    remaining days
● Inputs ⇒ Outputs
○ 360       1 0 0                                   each 360 days a year
○ 30         0 1 0                                   each 30 days a month
○ 10         0 0 10                                 just days infant!
○ 391       1 1 1                                   391 = 360 + 30 + 1 = 1 year, 1 month, 1 day
○ 61         0 2 1                                   61 = 2*30 + 1   
○ 200       0 6 20                                 200 = 30*6 + 20
○ 1000    2 9 10                                  1000 = 2*360 + 9*30 + 10
○ 5000     13 10 20"""

# days = int(input())
#
# # By integer division over 360, we know how many 360s in the days
# # Days should be: years * 360 + remaining_days
# # //360 gives the years. %360 remove the year
#
# years = days // 360
# days = days % 360       # now we remove # of complete years. One easy way is mod
#
# # same concept as above
# months = days // 30
# days = days % 30


