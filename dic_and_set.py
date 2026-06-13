# From list to Dict
# lst = [10, 22, 55]
# # idx 0->10   1->22    2->55
# print(lst[1])       # 22    [1] is called index
# # indices are from 0 to N-1
#
# dict = {0:10, 1:22, 2:55, 12345:37}
# print(dict[1])      # 22   [1] is called key
# print(dict[12345])  # 37
# # Keys are provided: {0, 1, 2, 12345}
# # Format {key1:value1, key2:value2, etc}
# # Dictionary data structure "associates" key with value

# Flexible keys
# The key can be from ANY IMMUTABLE value
# This what make dict very useful

# dict = {'a' : 'alpha',  # key:value
#         'o': 'omega',
#         'g': 'gamma'
#         }
# print(dict)
# # {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
# print(dict.keys())
# # dict_keys(['a', 'o', 'g'])
# print(dict.values())
# # dict_values(['alpha', 'omega', 'gamma'])
#
# print(dict['a'])    # alpha

"""Only immutables
● Keys are restricted
○ Immutables
● Values not"""
# immutables: int, float, tuple, string
# be careful from float as it is an approximate - don't
#
# class Employee:
#     pass
#
# dict = {
#     -1200001 : 'mostafa',
#     'ziad' : 25.5,
#     (4, 6) : [5, 8, 9],
#     'Hey' : Employee(),
#     16 : {6:90}     # value is another dict
#     #[1, 2] : 10    TypeError: unhashable type: 'list'
#     #([1, 2]) : 10   TypeError: unhashable type: 'list'
# }
# print(dict[(4, 6)]) # [5, 8, 9]

# Update and delete

# # Dict is mutable. We can update its content
# dict = {}   # No initial value
# dict[12] = [405, (1, 'mostafa')]    # Add a new key-value
# dict['mostafa'] = 20
#
# print(dict[12]) # [405, (1, 'mostafa')]
# dict[12] = 'hello'
# print(dict[12]) # hello
# print(dict.keys())  # dict_keys([12, 'mostafa'])
#
# del dict[12]
# print(dict.keys())  # dict_keys(['mostafa'])
# #print(dict[12])    # KeyError: 12
#
# dict[12] = 10
# dict[12] += 5
# print(dict[12])    # 15
# print(dict.pop(12)) # 15 : get and remove
# print(dict.pop('hey', 37))  # 37 default value


# Indexing dict values
# dict = {
#     'mostafa' : 'saad',
#     1 : [1, 5, 7, 9],
#     3 : [[3, 7], [8, 9, 10]]
# }
#
# print(dict['mostafa'])      # saad
# print(dict['mostafa'][-1])  # d
# print(dict[1][1])           # 5
# print(dict[3][1][2])        # 10


#  Set default
# dict = {
#     int: [6, 9, 10],
#     float : 10,
#     6: 20,
#     6: 70,
#     6: 80,
# }
# print(dict[float])  # 10    observe we can use data types, as they are immutable
# print(dict[6])      # 80    mutliple same keys: last value is used
# #print(dict[7])      # KeyError: 7
#
# # setdefault: returns the value of the item with the specified key.
# # If the key does not exist, insert the key, with the specified value
# print(dict.setdefault(6, -8))   # 80
# print(dict.setdefault(7, 20))   # 20
# print(dict[7])      # 20


# Membership Operator
# dict = {
#     -1200001 : 'mostafa',
#     'ziad' : 25.5,
#     (4, 6) : [5, 8, 9],
# }
#
# print('ziad' in dict)   # True
# print(100 in dict)      # False
#
# #if dict[7] == 5:    # KeyError: 7
# #    pass
#
# if 7 in dict and dict[7] == 5:
#     pass    # short-circuit evaluation


# Get method
# dict = {
#     -1200001 : 'mostafa',
#     'ziad' : 25.5,
#     (4, 6) : [5, 8, 9],
# }
#
# print(dict.get(7))          # None
# print(dict.get(7, 15))      # 15    (return default val if not exist)
# print(7 in dict)            # False
# print(dict.get((4, 6)))     # [5, 8, 9]
#
# dict.clear()       # remove all keys


# Popitem method
# dict = {'x': 11, 'b': 22, 'y': 30}
# dict['a'] = 33
#
# while dict:
#     print(dict.popitem())
"""
removes the last key-value pair added from d 
    and returns it as a tuple:
('a', 33)
('y', 30_oop)
('b', 22)
('x', 11)
"""


# Insertion order: NOW preserved (Python 3.7)
# dict = {}   # empty dict
# dict[20] = 10
# dict['mostafa'] = 10
# dict[30] = 15
# dict[(2, 7)] = 150
# dict[30] = 10
# # observe: values can be anything and can repeat
#
# print(dict.keys())
# dict_keys([20, 'mostafa', 30_oop, (2, 7)])
# Starting from python 3.7 specification : the keys order is preserved (insertion order)
# However, due to several reasons, it is still best practice to not depend on that
# Maybe after 10 years. For now, if order matter: use OrderedDict
# In practice: typically u don't care about insertion order but sorted keys themselves

# Useful readings
# http://gandenberger.org/2018/03/10/ordered-dicts-vs-ordereddict/
# https://realpython.com/python37-new-features/#the-order-of-dictionaries-is-guaranteed
# https://sdrees.gitbooks.io/python-order-is-now-key/content/first-question.html
# https://stackoverflow.com/questions/1867861/how-to-keep-keys-values-in-same-order-as-declared


# Keys!
# dict = {'x': 11, 'b': 22, 'y': 30}
#
# print(dict.items())    # dict_items([('x', 11), ('b', 22), ('y', 30_oop)])
#
# for key, value in dict.items():
#     print(key, value)   # x 11 b 22 y 30_oop
#
# print(dict.keys())  # dict_keys(['x', 'b', 'y'])
# print(list(dict.keys()))  # ['x', 'b', 'y']
#
# for key in dict.keys():
#     print(key, dict[key])   # same, but slower (extra access)
#
# for key in sorted(list(dict.keys())):
#     print(key, dict[key])   # sorted keys: b x y
#
# for key in sorted(dict):    # shortcut for ordered keys
#     print(key, dict[key])  # sorted keys: b x y

# List vs Dict
# lst = [10, 20, 30, 40]
# print(lst)
# # [10, 20, 30_oop, 40]
# # list: ordered sequence
# # can be indexed or sliced
#
# dict = {0:10, 3:40, 2:30, 1:20}
# print(list(dict.values()))
# # [10, 40, 30_oop, 20]
# # dict: ORDERED collection of key-value-pairs
# # items INSERTION order is preserved (3.7)

# Shallow copies
# class Employee:
#     def __init__(self):
#         self.id = 10
#     def __repr__(self):
#         return str(self.id)
# emp = Employee()
# lst = [5, 8, 9]
# dict = {'ziad' : 25.5, 2 : lst, 'Hey' : emp}
# print(dict) # {'ziad': 25.5, 2: [5, 8, 9], 'Hey': 10}
#
# lst.pop()
# emp.id += 100
# print(dict) # {'ziad': 25.5, 2: [5, 8], 'Hey': 110}
#
# lst = [5]
# print(dict) # {'ziad': 25.5, 2: [5, 8], 'Hey': 110}
# d2 = dict.copy()
# print(d2['Hey'] is emp) # True - shallow copy

# Merge, len, all, any
# dict = {'x': 11, 'b': 22, 'y': 30}
# dict['a'] = 33
#
# dict.update({'aaa':3, 'b':-2})  # merge
# print(str(dict)) # {'x': 11, 'b': -2, 'y': 30_oop, 'a': 33, 'aaa': 3}
# # you can pass dict or list of tuples
#
# print(len(dict))    # 5
#
# # True if all keys are trye
# print(all(dict))    # True
# dict[''] = "hey"
# print(all(dict))    # False
# print(any(dict))    # True


# Dictionary Comprehension

# without
# squares = {}
# for x in range(6):
#     squares[x] = x*x
# print(squares)
#
# # with
# squares = {x: x*x for x in range(6)}
#
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Constructors
# # most common
# a = {'one': 1, 'two': 2, 'three': 3}
# # constructor: pass dict as an argument
# b = dict({'three': 3, 'one': 1, 'two': 2})
# # from list of tuples: key/value
# c = dict([('two', 2), ('one', 1), ('three', 3)])
# # Use keyword arguments
# d = dict(one=1, two=2, three=3)
# # From a dictionary, followed by keywords
# e = dict({'one': 1, 'three': 3}, two=2)
# # zip on 2 lists used as key/value
# f = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#
# print(a == b == c == d == e == f)


# fromkeys
# a = [1, 2, 20, 6, 210, 2, 1]
# d = dict.fromkeys(a)
# # {1: None, 2: None, 20: None, 6: None, 210: None}
#
# print(dict.fromkeys(a, 7))
# # {1: 7, 2: 7, 20: 7, 6: 7, 210: 7}
#
# unique_keys = dict.fromkeys(a).keys()
# print(unique_keys)   # dict_keys([1, 2, 20, 6, 210])
# # removed duplicated + preserved the order
#
# unique_keys = list({10:2, 1:5})
# print(unique_keys)  # [10, 1]


"""Practice 1: Letters Frequency
● Read a string of lower/upper letters. 
● Convert to lowercase and then compute the frequency of letters.
○ Print from small to large.
● Input: bAAAaaazz
● Output (ordered based on key)
○ Letter a repeated 6 times
○ Letter b repeated 1 times
○ Letter z repeated 2 times
● Use dict in an efficient & simple way

Practice 1: Letters Frequency
● Convert to lower
● Get current letter value. It it doesn’t exist, set to 0
● Increment frequency
● Printed by sorted key"""

# if __name__ == '__main__':
#
    # line = input()
    # dict = {}
    # for char in line:
    #     char = char.lower()
    #     dict.setdefault(char, 0)    # if not exist, put value 0
    #     dict[char] += 1
    #
    # for key in sorted(dict):
    #     print(f'Letter {key} repeated {dict[key]} times')


"""Practice 2: Find most frequent number
● Read a line of N integers. The values can be big and negative
● Find all the values that repeated the most number of times.
○ Print them from small to large
● Input:    -123456 10 -123456 20 -30 -123456 20 25 20
● Output: The highest frequency is 3 for values: [-123456, 20]
● Don’t use nested loops
Practice 2: Find most frequent number
● We used list before, but the -ve value range was smaller (shift trick)
● Dict makes the problem trivial"""

# if __name__ == '__main__':
#
#     lst = list(map(int, input().split()))
#     dict = {}
#     for value in lst:
#         dict.setdefault(value, 0)
#         dict[value] += 1
#
#     mx = max(dict.values())
#     freq = sorted([key for key, value in dict.items() if value == mx])
#     print(f'The highest frequency is {mx} for values: {freq}')


"""Practice 3: Search for a number
● Read a line of N integers, but the values can be big and negative
● Then read a line of Q integer
○ For each integer, print the index of the last occurance in the list or -1 if it doesn’t exist
● By overriding the values, we easily know the last occurance"""


# if __name__ == '__main__':
#
#     lst = list(map(int, input().split()))
#     queries = list(map(int, input().split()))
#
#     dict = {}
#     for idx, value in enumerate(lst):
#         dict[value] = idx
#
#     for q in queries:
#         ans = dict.get(q, -1)
#         print(f'Query {q} answer {ans}')
#
# """ -1000 500 -1000 70 2 2 70 3 20 20
# 2 3 20 70 500 -1000  999 """

# Practice 3: Search for a number: print all indices

# if __name__ == '__main__':
#
#     lst = list(map(int, input().split()))
#     queries = list(map(int, input().split()))
#
#     dict = {}
#     for idx, value in enumerate(lst):
#         dict.setdefault(value, [])
#         dict[value].append(idx)
#
#     for q in queries:
#         ans = dict.get(q, -1)
#         print(f'Query {q} answer {ans}')


"""Problem #1: Special String Mapping
● Read a string and do the following conversions for its letters
○ If it is lower letter, use this map of 26 letters:
■ abcdefghijklmnopqrstuvwxyz
■ YZIMNESTODUAPWXHQFBRJKCGVL
■ E.g. a ⇒ Y   and z ⇒ L
○ If it is digit, use this map of 10 letters:
■ 0123456789
■ !@#$%^&*()
○ Otherwise, don’t change it!
● Input ⇒ Output
○ acMNmn39 ⇒ YIMNPW$)
○ vwXYZ0123 ⇒ KCXYZ!@#$"""

# if __name__ == '__main__':
#     # Create a dict with requested mapping
#     from_str = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     to_str = 'YZIMNESTODUAPWXHQFBRJKCGVL!@#$%^&*()'
#     # create the dict with comprehension
#     dict = {from_str[idx]:to_str[idx] for idx in range(len(from_str))}
#
#     string = input()
#     res = ''
#     for char in string:
#         if char in dict:
#             char = dict[char]
#         res += char
#     print(res)


"""Problem#2: Sort by type
● Implement function: 
def 
sort_different_types
(lst):
● It takes a list of different data types (int, float, string, list, tuple)
○ Return a list:
○ For every data type, group and sort from small to large
○ Within data types: Order them based on the order of the list (int comes first? Be first)
○ Assumption: provided lists or tuples will be comparable."""

"""
For every type, maintain a list in a dict
Order the values of every type
Flatten the lists

From python 3.7, the order is preserved. Hence the lists already sorted by type :)
"""

# def sort_different_types(lst):
#
#     dict = {}
#     for item in lst:
#         t = type(item)
#         dict.setdefault(t, [])
#         dict[t].append(item)
#
#     #SyntaxError: iterable unpacking cannot be used in comprehension
#     #return [*sorted(lst) for lst in dict.values()]
#     lsts = [sorted(lst) for lst in dict.values()]
#     return [item for lst in lsts for item in lst]
#
#
#
# if __name__ == '__main__':
#     lst = [10, 'most', 2.5, 7, 'aly', 9, 4.5, 2, 'ziad', -4, 1.1, [1, 5], 5, [0, 7, 8]]
#     print(sort_different_types(lst))


"""Problem #3: Fast Prefix Finder
● Read an Integer N on a line, then read 
N lines of strings (database)
● Then read an Integer Q on a line, then 
read Q lines of strings (queries)
● For every query, list all database 
strings that starts with this query
○ However the database is huge: using query 
in lst is very slow
● Print entries according to reading order
● See screenshoot"""

# if __name__ == '__main__':
#     n = int(input())
#     dct = {}
#     # Generate all prefixes and put in a dict
#     while n:
#         line = input()
#         for idx in range(len(line)):
#             substr = line[:idx +1]
#             dct.setdefault(substr, [])
#             dct[substr].append(line)
#         n -= 1
#
#     q = int(input())
#     while q:
#         line = input()
#         if line not in dct:
#             print('Not found')
#         else:
#             print(f'{line} matches {dct[line]}')
#         q -= 1


"""Problem #4: Filter Duplicates!
● Write function: 
def 
filter_duplicates_preserve_order
○ Input is list of list of integers
○ Output: A new list after removing all duplicate lists
○ You must preserve the input order
○ Use a Dict"""


# def filter_duplicates_preserve_order(lst_of_lsts):
#     # Convert internal  list into tuples to be immutable
#     tpls = [tuple(lst) for lst in lst_of_lsts]
#     my_dict = list(dict.fromkeys(tpls)) # get rid of duplicates
#     return [list(tup) for tup in my_dict]
#
# if __name__ == '__main__':
#     print(filter_duplicates_preserve_order([[7, 1], [2, 4],
#                                             [7, 1], [5, 2], [2, 4]]))


# set: unordered
# (don't preserve insertion order / no values order)
# unique: duplicates are ignored
# items: must be immutable

# st = set()
# st.add(20)
# st.add(10)
# st.add(20)
# st.add(-2537)
# st.add(10)
# print(st)   # {10, 20, -2537}


# st = {1, 5, 1, 3, 5}
# print(st)   # {1, 3, 5}
#
# st = set(['saad', 'most', 'saad'])  # takes iterable
#
# print('al' in st)       # False
# for item in st:         # No guarantee on order
#    print(item, end=' ') # most saad
# print()
#
# print(list(st))     # ['most', 'saad']
# print(set({1:10, -2:30}))   # {1, -2}
#
# print(set('Hey'))       # {'H', 'y', 'e'}
# print(set(['Hey']))     # {'Hey'}
# print(set({'Hey'}))     # {'Hey'}


# Functions
# st = {(1, 5), (2, 7), (1, 5), (2, 7)}
# print(st)   # {(2, 7), (1, 5)}
#
# # TypeError: unhashable type: 'list'
# #st = {(1, 5), [2, 7]}
#
# print(len(st))  # 2
# print(max(st))  # (2, 7)
# print(sorted(st))  #[(1, 5), (2, 7)]
#
# print(sum({1, 1, 1, 1, 2, 2, 2, 2}))    # 3 = 1+2
# print(all({1, 2, 'hey'}))       # True
# print(all({1, 2, 'hey', ()}))   # False: empty tuple



# Methods
# st1 = {1, 3, 5, 7, 8, 10}
#
# st1.add(-20)
# st1.remove(10)
# #st1.remove(30_oop)  # if not exist, error => KeyError
# st1.discard(30)  # if not exist, no problem
# print(st1)  # {1, 3, 5, 7, 8, -20}
#
# print(st1.pop())    # remove random element. If empty = error
# st1.clear() # remove elements


# Set comprehension
# Set comprehension
# line = "I am mostafa saad Ibrahim"
# unique_vowels = {i for i in line if i in 'aeiou'}
#
# print(unique_vowels)    # {'o', 'a', 'i'}


# Union and Intersection
# st1 = {1, 5, 7, 8}
# st2 = {1, 5, 3, 10}
#
# print(st1 | st2)        # {1, 3, 5, 7, 8, 10}: union using | operator
# print(st1.union(st2))   # same
# print(st1.union([1, -5, -7]))   # pass any iterable
# # note: st1 is not updated
#
# st3 = {5, 6, 1}
# su = st1 | st2 | st3
# si = st1 & st2 & st3    # set intersection
# print(si)   # {1, 5}
# print(st1.intersection(st2).intersection(st3))  # {1, 5}
# print(st1.intersection(st2, st3))  # {1, 5}


# Difference
# st1 = {1, 5, 7, 8}
# st2 = {1, 5, 3, 10}
#
# # return the set of all elements that are in st1 but not in st2
# print(st1 - st2)                # {8, 7}
# print(st1.difference(st2))      # same
#
# #  return the set of all elements in either st1 or st2, but not both:
# print(st1 ^ st2)    # {3, 7, 8, 10}
# print(st1.symmetric_difference(st2))
#
# # True if no intersection
# print(st1.isdisjoint(st2))      # False
# print(st1.isdisjoint([4, 6]))   # True


# Is subset? superset?
# st1 = {1, 5}
# st2 = {2, 1, 5, 3}
#
# # True if every element of st1 is in st2
# print(st1 <= st2)           # True
# print(st1.issubset(st2))    # True
#
# # True if every element of st1 is in st2, but not equal
# print(st1 < st2)            # True
# print(st1 < {1, 5})         # False
#
# print(st2 >= st1)             # True
# print(st2.issuperset(st1))    # True
# print(st1 >= {1, 5})          # True
# print(st1 > {1, 5})           # False


# Updates
# st1 = {1, 5, 7, 8}
# st2 = {1, 5, 3, 10}
#
# st1 |= st2  # union and update st1
# st2.update(st1)
#
# # same &= ^=


# frozenset
# immutable set
# st1 = frozenset([7, 5, 1, 8])
# # can't change it: no add/remove etc
#
# print(id(st1))  # 0x111
# st1 |= {20, 10}
# print(id(st1))  # 0x222 DIFFERENT - recall strings!
#
# # useful if u need a set, but immutable
# dct = {st1 : 5}
#
# for item in sorted(st1):
#     print(item, end=' ')
#     # 1 5 7 8 10 20


"""Practice: Filter Duplicates v2!
● Write function: 
def 
filter_duplicates
(lst):
○ Input is list of list of integers
○ Output: A new list after removing all duplicate lists
○ You don’t need to preserve order!"""
#
# def filter_duplicates(lst_of_lsts):
#     st = set()
#     result = []
#
#     for lst in lst_of_lsts:
#         tup = tuple(lst)    # must use immutable objects
#         if tup not in st:
#             st.add(tup)
#             result.append(lst)
#     return result
#
# if __name__ == '__main__':
#     print(filter_duplicates([[7, 1], [2, 4],
#                              [7, 1], [5, 2], [2, 4]]))
