# Variables Homework 1

# Homework 1: Math operations
"""
● Write a program that reads 2 numbers and print their + - * / computations as
in the picture
● Do good testing for your code
○ E.g. consider negative values
○ E.g. even and odd values
○ E.g. consider zero as first or 2nd number
"""
# first = float(input("Enter first number:\n "))
#
# # let's make it in a single line.
# second = float(input("Enter second number:\n "))
#
# print(first, '+', second, '=', first + second )
# print(first, '-', second, '=', first - second )
# print(first, '*', second, '=', first * second )
# print(first, '/', second, '=', first / second )
#
# print("\nEnd the programe")

# Homework 2: Students grades
"""● Write a program that reads 2 students information about math exam
○ For each student read: his name, id and grade
● Print the students
● Print the grades average
● See the picture"""

# name1 = input("Enter the first stduent's name: ")
# id1 = input("Enter the first stduent's ID: ")
# grade1 = float(input("Enter the first stduent's grade: "))
#
# name2 = input("\nEnter the second stduent's name: ")
# id2 = input("Enter the second stduent's ID: ")
# grade2 = float(input("Enter the second stduent's grade: "))
#
# print('\n\nInformat for students and their "Math" grades')
# msg = name1 + '(ID ' + id1 + ') got grade: ' + str(grade1)
# print(msg)
# msg = name2 + '(ID ' + id2 + ') got grade: ' + str(grade2)
# print(msg)
#
# average = (grade1 + grade2) / 2.0
# print('Average math grade is', average)

# Homework 3: Even and Odd sum

"""● Given 8 space-separated integers, find the sum of those in even places and 
the sum of those in odd places.
○ Note: Even place means the 2nd, 4th, 6th or 8th numbers, 
          odd places are the 1st, 3rd, 5th and 7th numbers.
○ Note: the 8 numbers will be on the same line
○ Note: Don’t print any welcome or by messages. 
● Input: 11 2 7 9 12 -8 3 -1
● Output: 2 33
● Example Explanation:
○ 2 + 9 + (-8) + (-1) = 2  for the even places
○ 11 + 7 + 12 + 3 = 33   for the odd places"""

# just create 8 variables, with suitable names for easy coding
# odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input().split())
#
# even_sum = even1 + even2 + even3 + even4
# odd_sum = odd1 + odd2 + odd3 + odd4
#
# print(even_sum, odd_sum)

# Homework #4: Special concatenation

"""● Write a program that read 3 strings.
○ For simplicity let’s say input is 3 letters A, B and C
● The output is A’B”C repeated 10 times
○ A’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”C
● Input:
○ I
○ am
○ Mostafa
● Output:
○ I'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'a
m"MostafaI'am"MostafaI'am"Mostafa"""

# A = input()
# B = input()
# C = input()
#
# combo = A + "'" + B + '"' + C
# combo = combo * 10
#
# print(combo)

# Homework 1: Guess Output

# This is called: https://www.mathsisfun.com/numbers/fibonacci-sequence.html

# num1 = 1
# num2 = 2
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3
#
# print(num3)
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3
#
# print(num3)
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3
#
# print(num3)
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3

# print(num3)
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3
#
# print(num3)
#
# num3 = num1 + num2
# num1 = num2
# num2 = num3
#
# print(num3)


# Homework 2: Swapping 2 numbers!

"""● Write a program that reads 2 integers num1 and num2
○ E.g. say we read num1 = 7 and num2 = 25
● Target: we want swap the values of num1 and num2?
○ Swap means exchange
○ So Num1 has value 25 and Num2 has value 7
○ Write 3 lines of code only"""

# num1, num2 = map(int, input().split())
# create temporary to hold num1
# num3 = num1
# give num1 value of num 2
# num1 = num2
# now give num2 the temp value
# num2 = num3
# print(num1, num2)

# num1, num2 = map(int, input().split())
# # In the next section - assignment operator you should know why this works!
# num1, num2 = num2, num1
# print(num1, num2)

# Homework 1: Swapping 3 numbers!

"""● Write a code to swap 3 numbers
● Let say we have numbers              a = 115, b = 20, c = 301
● We wanna their final values to be: a = 20, b = 301, c = 115"""

# Pythonoic way
# # In the next section - assignment operator you should know why this works!

# num1, num2, num3 = map(int, input().split())
# num1, num2, num3 = num2, num3, num1
# print(num1, num2, num3)

# one way to swap num1, num2 in 3 lines
# then swap swap num2, num3 in 3 lines
# a smarter idea to circulate them (like a circle)

# num1, num2, num3 = map(int, input().split())
# temp = num1
# num1 = num2
# num2 = num3
# num3 = temp
# print(num1, num2, num3)

# Homework 2: Print Me

"""● Write a program that reads 2 integers A, B
○ B is either -1 or 1
■ If B is -1, print 2*A+1
■ If B is  1, print A*A
● Input: 7 1 ⇒ 49.0
● Input: 7 -1 ⇒ 15.0
● Hint
○ You need to think in a 1 line formula for the output"""

# a, b = map(int, input().split())

# Let's code the 2 possible results
# equ_is_1 = a * a
# equ_is_neg_1 = 2 * a + 1

# The trick: we want to make them in 1 equation
# Where if input is: only 1 equation is computed and the second is zero
# To do so: convert -1 to 0 and 1 to 1
# With simple math, we can convert [-1 1] to [0 1] range

# # value 1 for (b 1) and value 0 for (b -1)
# is_1 = (b + 1) / 2
# # value 1 for (b -1) and value 0 for (b 1)
# is_neg_1 = 1 - is_1
# # Either 1*something + 0*something for b = 1
# # Or     0*something + 1*something for b = -1
# ans = is_1 * equ_is_1 + is_neg_1 * equ_is_neg_1
# print(ans)

######
# # In the future, we will learn how with more tools, this is actually a trivial task as following
# # code for future purposes only
# if b == -1:
#     print(2 * a + 1)
# else:
#     print(a * a)
# # Another way (not straightforward) with operators from next section:
# print(b == -1 and equ_is_1 or equ_is_neg_1)

# Homework 3: Sum numbers from 1 to N
"""● Write a program that reads integer N and Print the sum from 1 to N
○ E.g. If input N = 5, then Output is: 15
■ Why? As 1+2+3+4+5 = 15
○ Below table of more values
○ 3 ⇒ 6 (1+2+3)
○ 4 ⇒ 10 (1+2+3+4)
○ 5 ⇒ 15 (1+2+3+4+5)
● You need to find a simple 1 line formula to solve the problem :) 
○ Hint: Let N = 8. Write numbers from 1 to 8
○ What is the sum of 1st and 8th number? sum of 2nd and 7th? And so on
○ Your formula should be good for even and odd N. Be careful programmer!"""
# print( (1 + 2) * (3 + 1) / 2)
# n = int(input())
# ans = (n * (n + 1)) / 2
# print(ans)
"""
Why such equation?
Here is an intuition for N = 8
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
Let's arrange as following
1 8   2 7    3 6     4 5       [first number and last number]   [2nd number, and 2nd from back] ...
What is the value of each pair? 9 = n+1
How many pairs? 4 = n/2
So n/2 pair, each has value n+1
So total sum is (n * (n+1))/2
Now, this works for even N
Your turn: why works for odd N
More readings: http://mathcentral.uregina.ca/qq/database/qq.02.06/jo1.html"""

