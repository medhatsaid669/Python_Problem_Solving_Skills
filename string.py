# # Recall:
#
# s1 = 'most'
# s2 = 'saad'
# s3 = s1 + 2 * s2    # mostsaadsaad
#
# lst = list(s1)  # ['m', 'o', 's', 't']
#
# # iterate on position, char string
# for idx, char in enumerate(s1):
#     pass
#
# print('most' < 'Most')      # False
#
# a, b, c, d = 'Most'
# print(c)    # s
#
# # same with list btw
# a, b = [3, 4]

# # functions
#
# s1 = 'moST'
#
# print(len(s1), min(s1), max(s1))     # 4 S o
#
# print(sorted(s1))   # ['S', 'T', 'm', 'o']
#
# print(tuple(reversed(s1)))   # ('T', 'S', 'o', 'm')



# # Indexing and Slicing
#
# s1 = 'moST'
#
# print(s1[0], s1[-1])  # m T
#
# print(s1[2:])    # ST
# print(s1[::])    # moST
# print(s1[::-1])  # TSom
#
# #TypeError: 'str' object does not support item assignment
# #s1[0] = 'c'
#
# #TypeError: 'str' object doesn't support item deletion
# #del s1[0]


# lst = ["Hello", "World", "Python","is", "Cool"]
# first_letters = [word[0] for word in lst]
# print(first_letters)    # ['H', 'W', 'P', 'i', 'C']
#
#
# first_letters = [word[0].lower() for word in lst]
# print(first_letters)    # ['h', 'w', 'p', 'i', 'c']
#
#
# my_str = "Please 10 finds 123all dig0ts"
#
# digits = [int(char)  for char in my_str if char.isdigit()]
# print(digits)   # [1, 0, 1, 2, 3, 0]


# my_str = 'mostafa'
#
# # TypeError: 'str' object does not support item assignment
# #my_str[3] = 'T'        #immutable!
#
# my_str = my_str[:3] + my_str[3].upper() + my_str[4:]
# print(my_str)   # mosTafa
#
# my_str2 = my_str
# print(my_str is my_str2)        # True
#
# print(id(my_str))   # 0x111
# my_str += ' saad'
#
# print(id(my_str))   # 0x222
# print(id(my_str2))  # 0x111
#
# print(my_str is my_str2)        # False


"""String Methods
● capitalize()
● center()
● casefold()
● count()
● endswith()
● expandtabs()
● encode()
● find()
● format()
● index()
● isalnum()
● isalpha()
● isdecimal()
● isdigit()
● isidentifier()
● islower()
● isnumeric()
● isprintable()
● isspace()
● istitle()
● isupper()
● join()
● ljust()
● rjust()
● lower()
● upper()
● swapcase()
● lstrip()
● rstrip()
● strip()
● partition()
● maketrans()
● rpartition()
● translate()
● replace()
● rfind()
● rindex()
● split()
● rsplit()
● splitlines()
● startswith()
● title()
● zfill()
● format_map()"""



# print('abcDEF'.lower())        # abcdef : conver to lower letters
# print('abcDEF'.upper())        # ABCDEF : conver to upper letters
#
# print('abc'.islower())      # True : all cased characters in S are lowercase?
# print('ABC'.isupper())      # True: all cased characters in S are uppercase?
# print('123'.isdecimal())    # True : all characters in S are 0 to 9?
#
# print('abcdef'.startswith('abc'))       # True
# print('abcdef'.startswith('abcD'))      # False
# print('abcdef'.endswith('def'))         # True
#
# print('abcdbcd'.find('bc'))         # 1  lowest index
# print('abcdbcd'.find('xx'))         # -1 if not exist
# print('abcdbcd'.rfind('bc'))        # 4  highest index
# #print('abcdbcd'.index('xx'))       # same as finds, but ValueError if not found
#
# print('HiHiHi'.count('Hi'))       # 3 occurrences for Hi
# print('AAAA'.count('AA'))         # 2 occurrences NOT 3
#
#
# print(' '.isspace())        # True
# print('\n'.isspace())       # True
# print('\t'.isspace())       # True
#
# print('\n\tHello   \t'.strip())     # Hello
#
# print('Hi Jack? Hi'.replace('Hi', 'Most'))  # Most Jack? Most
#
# print('\nI am     33 '.split())     # ['I', 'am', '33']
#
# print('Hey\nHow\nAre you?'.splitlines())   # ['Hey', 'How', 'Are you?']
#
#
# # by default split based on space
# print('\n\n\they mostafa'.split())
# # ['hey', 'mostafa']
#
# print(' I am   mostafa,saad,ibrahim'.split())
# # ['I', 'am', 'mostafa,saad,ibrahim']
#
# print(' I am   mostafa,saad,ibrahim'.split(','))
# # [' I am   mostafa', 'saad', 'ibrahim']
#
# print(' I am   mostafa,saad,ibrahim'.split('a'))
# #[' I ', 'm   most', 'f', ',s', '', 'd,ibr', 'him']
#
# print('\n\n\they mostafa'.split(' '))
# #['\n\n\they', 'mostafa']
#
# print('1,,,2'.split(','))
# #['1', '', '', '2']
#
# input().split()
#
#
# lst = ['a', 'bb', 'ccc']
#
# print(''.join(lst)) # abbccc     *** most common case
#
# print(','.join(lst)) # a,bb,ccc  *** most common case
#
# print('#$#'.join(lst)) # a#$#bb#$#ccc
#
# # join takes an iterable: list, string, tuple, dict, set
# # join them with the used string
#
# s1 = 'abc'
# s2 = '12345'
# print(s1.join(s2))  # 1abc2abc3abc4abc5
#
# print(s2.join(s1))  # a12345b12345c


"""String formatting
● Typically you need to print a message that involve values
○ Please enter a number from 1 to 5   (5 is number of menu choices)
○ Mostafa age is 33 and salary is 1000  (we have 3 variables: mostafa, age, 1000)
● We can do that with what we learned so far, but not great enough
● String formatting is about having some template/structure to make it easier
● There are 3 ways for that
○ Modulus operator: old - avoid, but u will read in legacy codes
○ Replacements Fields - ok, but avoid for verbose outputs
○ F-string - the modern way to go
● We will highlight the most common features, but there are a lot of details
○ Future 
reading
● Tip: Stop one by one and try!"""

#
# name, age = 'mostafa', 33
# print(name, 'is', age, 'years old')             # 1 old way
# print(name + ' is ' + str(age) + ' years old')  # 2 old way
#
# # The first {} is replaced with mostafa
# # the 2nd is replaced with 33
# print('{} is {} years old'.format(name, age))   # mostafa is 33 years old
#
# # we call this string with curly braces {} as template
#
#
# #IndexError: tuple index out of range   - u need to provide 3 arguments
# #print('{}{}{}'.format('Hey'))
#
# print('{}{}{}'.format(1, 2, 3, 4, 5, 6))    # 123 - OK to provide more. Ignored
#
# print('{}')       # {}
# print('{{}}')     # {{}}
# print('{{{}}}'.format('Hey'))     # {Hey}   If you want to surround an item with {}, use double: {{ }}
# #print('{{{{{{}}}}}}'.format('Hey'))      # don't :)     {{{}}}
# #print('{{{{{{{}}}}}}}'.format('Hey'))    # don't :)   {{{Hey}}}


# name, age = 'mostafa', 33
#
# print('{0} is {1} years old'.format(name, age))     # mostafa is 33 years old
#
# #print('{0} is {2} years old'.format(name, age))     # IndexError - no idx 2
#
# print('{0} is {1} years old. Are you {1} years as {0}'.format(name, age))
# # mostafa is 33 years old. Are you 33 years as mostafa
# # pros: you provie positional argument once and use it many
#
# print('{name} is {AGE} years old. Are you {AGE} years as {name}'.format(name=name, AGE=age))
# # mostafa is 33 years old. Are you 33 years as mostafa
# # similarly, we can use keyword arguments but flxible order!
#
# # Be careful from mixing
# print('{} is {age} years old'.format(name, age=age))    # mostafa is 33 years old
# print('{0} is {age} years old'.format(name, age=age))   # mostafa is 33 years old
#
# #print('{1} is {age} years old'.format(age=age, name))
# # SyntaxError: positional argument follows keyword argument
# #print('{1} is {age} years old'.format(name, age=age))   # IndexError


# {[<name>][!<conversion>][:<format_spec>]}
# Python has too many details in these parts
# https://realpython.com/python-formatted-output/

# my_lst = ['mostafa', 33, 1000]
#
# print('{lst[0]} is {lst[1]} years old with salary {lst[2]}'.format(lst = my_lst))
# # mostafa is 33 years old with salary 1000



# for i in range(0, 20, 2):
#     print('Given i={0}: i^4 = {1} i^3 = {2}'.format(i, i* i * i * i, i * i * i))

"""
How to format to view nicely?

Given i=0: i^4 = 0 i^3 = 0
Given i=2: i^4 = 16 i^3 = 8
Given i=4: i^4 = 256 i^3 = 64
Given i=6: i^4 = 1296 i^3 = 216
Given i=8: i^4 = 4096 i^3 = 512
Given i=10: i^4 = 10000 i^3 = 1000
Given i=12: i^4 = 20736 i^3 = 1728
Given i=14: i^4 = 38416 i^3 = 2744
Given i=16: i^4 = 65536 i^3 = 4096
Given i=18: i^4 = 104976 i^3 = 5832
"""


# for i in range(0, 20, 2):
#     print('Given i={:2}: i^4 = {:7} i^3 = {:4}'.format(i, i* i * i * i, i * i * i))

"""
{1:7}: Format position 1 in field of 7 spaces

Given i= 0: i^4 =       0 i^3 =    0
Given i= 2: i^4 =      16 i^3 =    8
Given i= 4: i^4 =     256 i^3 =   64
Given i= 6: i^4 =    1296 i^3 =  216
Given i= 8: i^4 =    4096 i^3 =  512
Given i=10: i^4 =   10000 i^3 = 1000
Given i=12: i^4 =   20736 i^3 = 1728
Given i=14: i^4 =   38416 i^3 = 2744
Given i=16: i^4 =   65536 i^3 = 4096
Given i=18: i^4 =  104976 i^3 = 5832
"""


# for i in range(0, 20, 2):
#     print('Given i={:<2}: i^4 = {:<7} i^3 = {:<4}'.format(i, i* i * i * i, i * i * i))

"""
Using :<7 makes it left-aligned

Given i=0 : i^4 = 0       i^3 = 0   
Given i=2 : i^4 = 16      i^3 = 8   
Given i=4 : i^4 = 256     i^3 = 64  
Given i=6 : i^4 = 1296    i^3 = 216 
Given i=8 : i^4 = 4096    i^3 = 512 
Given i=10: i^4 = 10000   i^3 = 1000
Given i=12: i^4 = 20736   i^3 = 1728
Given i=14: i^4 = 38416   i^3 = 2744
Given i=16: i^4 = 65536   i^3 = 4096
Given i=18: i^4 = 104976  i^3 = 5832
"""


# for i in range(0, 20, 2):
#     print('Given i={:2}: i^4 = {:<7} i^3 = {:^4}'.format(i, i* i * i * i, i * i * i))

"""
:7 right-aligned
:<7 left-aligned
:^7 center-aligned

Given i= 0: i^4 = 0       i^3 =  0  
Given i= 2: i^4 = 16      i^3 =  8  
Given i= 4: i^4 = 256     i^3 =  64 
Given i= 6: i^4 = 1296    i^3 = 216 
Given i= 8: i^4 = 4096    i^3 = 512 
Given i=10: i^4 = 10000   i^3 = 1000
Given i=12: i^4 = 20736   i^3 = 1728
Given i=14: i^4 = 38416   i^3 = 2744
Given i=16: i^4 = 65536   i^3 = 4096
Given i=18: i^4 = 104976  i^3 = 5832
"""


# val = 71.01234567890123456789012345678901234567890123456789
#
# print(val)                      #71.01234567890124 ==> 14 decisimal precision printed
# print('{:20}'.format(val))      #   71.01234567890124 ==> total 20 output units, right-aligned
# print('{:11f}'.format(val))     #  71.012346 ==>  print 11 units. Use default precision (typically 6)
# print('{:11.3f}'.format(val))   #     71.012 ==> 11 output units, 3 of them precision
# print('{:3.5f}'.format(val))    #71.01235 ==> 5 precision. It will have more priority
# print('{:.8f}'.format(val))     #71.01234568 ==> 8 precision. No specific alignments
# #print('{.8f}'.format(val))     #AttributeError
#

# # Precision
# val = 2.67
# print(val)                     #2.67
# print('{:11f}'.format(val))    #   2.670000 ==>  trailing zeros  : 11 output units (6 is precision)
# print('{:11.2f}'.format(val))  #       2.67   (.2f use 2 precision)
# print('{:11.1f}'.format(val))  #        2.7   rounding
# print('{:11.0f}'.format(val))  #          3   rounding
#
# print('{:11.0f}'.format(2.5))  #          2   rounding to 2
# print('{:11.0f}'.format(-2.5))  #        -2   rounding to -2
#
# # {value:width.precision}

# fstring is the modern way


# # F-string: The very modern way
# name, age = 'mostafa', 33
#
# # mostafa is 33 years old
# print('{} is {} years old'.format(name, age))
# print('{name} is {age} years old'.format(name=name, age=age))
#
# print(f'{name} is {age} years old')
#
#
# val = 71.0123456789012345678901234
#
# #     71.012
# print('{:11.3f}'.format(val))
# print(f'{val:11.3f}')


# # F-string: The very modern way
# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Employee {self.name} is {self.age} years old'
#
#     def __repr__(self):
#         return f'Employee(name="{self.name}", age={self.age})'
#
# most = Employee('mostafa', 33)
# print(f'{most}')        # Employee mostafa is 33 years old
# # add !r to use the dunder repr
# print(f'{most!r}')      # Employee(name="mostafa", age=33)
#
# print(f"{2 * 3+ 1}")    # 7
# name = 'mostafa'
# print(f"{name.lower()} has udemy courses")  # mostafa has udemy courses


# # Modulus Operator: The very old way
# # mostafa is 33 years and salary 100.578900
# print('%s is %d years and salary %f' % ('mostafa', 33, 100.5789))
#
# #mostafa is 33 years and salary 100.579
# print('%s is %d years and salary %.3f' % ('mostafa', 33, 100.5789))
#
# #mostafa is 33 years and salary         100.579
# print('%s is %d years and salary %15.3f' % ('mostafa', 33, 100.5789))
#
# print('%d' % 123)   # 123
# #print('%d' % '123')   # 123        TypeError


"""Homework 1: Is Palindrome?
● A palindrome is a string reads the same backward as forward
○ E.g. madam, racecar, 11/11/11, 12321
● Read a string and print YES if palindrome and NO if not.
○ Note: Whenever I write string, by default no spaces"""

# if __name__ == '__main__':
#     mystr = input()
#
#     if mystr == mystr[::-1]:
#         print('YES')
#     else:
#         print('NO')


"""Homework 2: Convert to number
● Read a string, convert it to int then print number number*3
○ Note: Don’t use the int() function. We will write our function
○ Define function: 
● Input ⇒ output
def 
our_int(string):
○ “100” ⇒ 100 300
○ “0000200” ⇒ 200 600"""

# def our_int(string):
#     res = 0
#     digits = '0123456789'
#
#     for char in string:
#         # search for char in digits to know its value: e.g. convert '5' to 5
#         res = res * 10 + digits.find(char)
#     return res
#
# if __name__ == '__main__':
#     mystr = input()
#
#     ans = our_int(mystr)
#     print(ans, ans * 3)


"""Homework 3: Grouping
● Read a string (sz > 0) of letters and digits, then divide it to consecutive groups 
of the same character (regardless of casing lower or upper). 
● Print the group comma separated. No comma after last one
● Input ⇒ outputs
○ 111222aabbb ⇒  111,222,aa,bbb
○ HHHH ⇒ HHHH
○ 5 ⇒ 5
○ abcdddddeefa ⇒  a,b,c,ddddd,ee,f,a
○ abcdDdDdeEfa ⇒ a,b,c,dDdDd,eE,f,a"""

# if __name__ == '__main__':
#     line = input() + '$'    # to make coding easier: add char that is not part of input
#
#     res = []
#     group_start_idx = 0
#     for idx in range(1, len(line)):
#         # as long as same char, let's keep expanding - .lower to avoid casing
#         if line[idx].lower() != line[idx-1].lower():
#             res.append(line[group_start_idx : idx])    # cut a group
#             group_start_idx = idx # next group start
#
#     print(','.join(res))
#     # an iterative way for the comma - just for educational purpose
#     #for idx, item in enumerate(res):
#     #    sep = ',' if idx != len(res)-1 else ''  # always , except the last entry empty
#     #    print(item, end=sep)


"""Homework 4: Conc Strings
● Read a line of 2 strings: S and T
● Print a new string that contains the following:
○ First letter of the string S followed by the First letter of the string T.
○ Second letter of the string S followed by the Second letter of the string T.
○ and so on…
○ Once one of them is finished, print the remaining of the second
● Input ⇒ Output
○ abc defghi ⇒ adbecfghi
○ AM CICPC ⇒ ACMICPC"""


# # conc strings
#
# def print_conc(str1, str2):
#     for c1, c2 in zip(str1, str2):
#         print(c1 + c2, end='')
#
#     if len(str1) < len(str2):  # canonicalize: make sure first is bigger
#         str1, str2 = str2, str1
#
#     if len(str1) > len(str2):
#         print(str1[len(str2):], end='')
#     print()
#
#     # observe: I did not explicitly create a new string. Concatenation is slow process
#     # always there is a single new line printed not 2 sometimes
#     # observe usage of zip
#     # observe canonicalization step. Instead of different handling for which is bigger
#     # we change content to make sure there is only one case
#
# if __name__ == '__main__':
#     str1, str2 = input().split()
#     print_conc(str1, str2)


"""Homework 1: Filtering
● Read a line of words that could be separated with any of ,$ # (4 letters)
○ Several separators on same line
○ Words themselves have no spaces
● Extract all the words, sort them and print the words
● Input
○ apple,banana, , , apple,student### #student$$apple
● Output:
○ ['apple', 'apple', 'apple', 'banana', 'student', 'student']
● Can you code all of it in a single line? A bit long one
○ Feel free to do it your way"""


# if __name__ == '__main__':
#     # flip every separator to a space, then trivially split and sort
#     # input() reads a line
#     # .replace(',', ' ')  return a string with replacements
#     # consective .replace is applied on return
#     # then .split on a string with just spaces
#     # then sorted over the returned list
#     # then print over the list argument
#     print(sorted(input().replace(',', ' ').replace('$', ' ').replace('#', ' ').split()))
#
#     # I am coding it this way for educational purpose
#     # In practice: you should divide the code to a few lines
#
# # apple,banana, , , apple,student### #student$$apple


"""Homework 2: Compressing
● Read a string (sz > 0) of lower letters, then divide it to consecutive groups of 
the same character and compress them
○ If more than a letter: aaaa ⇒ 4a
○ If a single letter: a ⇒ a
○ Order the groups based on the frequency (bigger first), then based on letter (smaller first)
■ Tip: Start with frequency smaller.
● Input ⇒ outputs
○ aaabbbccc ⇒  3a_3b_3c
○ z ⇒ z
○ aabbbbbddddcccc ⇒  5b_4c_4d_2a
○ aabbccaa ⇒ 2a_2a_2b_2c"""



# if u have numbers [1, 5, 6]
# if we wanna order small to large: we can use .sort
# large to small: sort(reverse=true)
# here is a nice math trick
# if u multiplied all numbers we -1, then we can use .sort to order them also from large to small

# below i multiply length with -1
# then we can order from small to large both letter and frequency

#
# if __name__ == '__main__':
#     line = input() + '$'
#
#     res = []
#     group_start_idx = 0
#     for idx in range(1, len(line)):
#         if line[idx] != line[idx-1]:
#             ln = idx - group_start_idx
#             res.append( (-ln, line[idx-1]) )
#             group_start_idx = idx
#
#     res.sort()
#     for idx, (freq, char) in enumerate(res):
#         freq = -freq
#         if freq == 1:
#             res[idx] = char
#         else:
#             res[idx] = '{}{}'.format(freq, char)
#
#     print('_'.join(res))


"""Homework 3: Order Data
● We have N employees in the company, 
each name, age and salary (both int)
● Line #1: read integer N
● In next N lines: read per line name, age 
and salary
● Print the data ordered: by name first, 
then age, then salary
● Input
○ 5
○ mostafa 33 2000
○ belal 10 900
○ mostafa 20 10000
○ belal 10 6000
○ ZIAD 2 0"""


# if __name__ == '__main__':
#     n = int(input())
#     lst = [0] * n   # more efficient to allocate early
#
#     for pos in range(n):
#         name, age, salary = input().split()
#         lst[pos] = name, int(age), int(salary)    # tuple
#
#     lst.sort()  # each tuple will be compared
#     for idx, (name, age, salary) in enumerate(lst): # deep unpacking
#         print(idx, name, age, salary)


"""Homework 4: Replace substring
● Implement 
def 
our_replace(main_str, pattern, repalce_with):
○ The function similar to string.replace. We will implement ours
○ Don’t use any method in the string class.
● Read a line of 3 strings
● The function replaces every pattern with to and return it
○ Input: “aabcabaaad”, “aa”, “x”           -      Return: “xbcabxad”
○ Input: “aabcabaaad”, “aa”, “aaaa”     -      Return: “aaaabcabaaaaad”
○ Input: “aabcabaaad”, “aa”, “”             -      Return: “bcabad”
○ Input: “aabcabaaad”, “”, “xx”             -      Return: “aabcabaaad”"""



# def our_replace(main_str, pattern, repalce_with):
#     idx = 0
#     res = ''
#     n = len(pattern)
#
#     if n == 0:
#         return main_str
#
#
#     while idx < len(main_str):
#         # If matched: add and jump. Otherwise move to the next step
#         substr = main_str[idx:idx + n]
#         if substr == pattern:
#             res += repalce_with
#             idx += n
#         else:
#             res += main_str[idx]
#             idx += 1
#     return res
#     # the code can be improved. For example: all these += are inefficient
#
#
# if __name__ == '__main__':
#     main_str, pattern, repalce_with = input().split()
#
#     print(our_replace(main_str, pattern, repalce_with))

















