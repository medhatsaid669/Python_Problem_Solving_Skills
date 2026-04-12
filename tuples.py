"""Tuples
● Another an ordered collection of objects
○ Some pronounce it as though it were spelled “too-ple”
○ and others as though it were spelled “tup-ple”
● Several similarities with list
○ Iterating, Indexing, slicing, comparisons, multiple elements: min(), max(), sorted()
● More:
○ A immutable data type: We can’t change or delete ith item
■ Many methods don’t exist: append, insert, remove
■ Though we can change the item internal content if mutable!
○ Fast iteration (visible with large collection)
○ Key with Dict. List can’t
○ Multiple return from a function or multiple assignments"""

# def f():
#     return 1, 2, 3
#
# a, b, c = f()
#
# together = f()
# print(type(together))   # <class 'tuple'>
#
# x, y, z = together      # unpack
#
# # ValueError: too many values to unpack (expected 2)
# #x, y = together
#
# # ValueError: not enough values to unpack (expected 5, got 3)
# #x, y, z, w1, w2 = together
# #print(w1)
#
# my_tuple = (5, 6, 7)    # Create tuple
# x, y, z = together      # unpack
#
# x, y = y, x         # swap


# # creation
# t = ('mostafa', 12, 2.5, 12)    # 4 items!
# t = ('mostafa', 12, 2.5, 12, )  # also 4 items!
#
# t = (10)
# print(type(t))  # SADLY int not tuple :(
# t = (10, )      # tuple of 1 item
# t = ()          # tuple of 0 item
#
# print(len((True, 'mostafa')))     # 2
#
# # all are tuples
# x, y = 1, 2
# x, y = (1, 2)
# (x, y) = (1, 2)
#
# # TypeError: tuple expected at most 1 arguments, got 3
# #t = tuple(1, 2, 3)
# t = tuple((1, 2, 3))    # constructor: iterable
# t = tuple([1, 2, 3])
# t = tuple('most')       # ('m', 'o', 's', 't')


#
# # Same as lists
#
# numbers = (10, 2, 7, 5, 3)
#
# print(numbers[0], numbers[-1])  # 10 3
#
# print(numbers[2:])    # (7, 5, 3)
# print(numbers[::])    # (10, 2, 7, 5, 3)
# print(numbers[::-1])  # (3, 5, 7, 2, 10)
#
# for item in numbers:
#     print(item, end=' ')    # 10 2 7 5 3
#
# #TypeError: 'tuple' object does not support item assignment
# #numbers[0] = 4


#
# numbers = (10, 2, 7, 2, 2, -5)
#
# print(numbers.count(2))     # 3
# print(numbers.index(2))     # 1
#
# #AttributeError: 'tuple' object has no attribute 'remove'
# #numbers.remove(0)
#
# #TypeError: 'tuple' object doesn't support item deletion
# #del numbers[0]
#
# print(min(numbers), max(numbers))   # -5 10
#
# lst = sorted(numbers)   # LIST: [-5, 2, 2, 2, 7, 10]
#
# print(tuple(sorted(numbers))) #   (-5, 2, 2, 2, 7, 10)
# print(tuple(reversed(numbers))) # (-5, 2, 2, 7, 2, 10)



# class Employee:
#     def __init__(self):
#         self.id = 0
#
# lst = [1, 2, 3, 4]
# emp = Employee()
#
# tu = (lst, emp)
# print(tu[0])    # [1, 2, 3, 4]
#
# # we can't change the items, but can change thier content if mutable
# #tu[0] = [6, 7]  # TypeError
# lst[0] = 100
# emp.id = 20
#
# print(tu[0])     # [100, 2, 3, 4]



# t1 = (1, 2, 3)
# t2 = ('mostafa', True)
#
# t = t1 + 2 * t2
#
# print(t)
# # (1, 2, 3, 'mostafa', True, 'mostafa', True)
#
# # TypeError: can only concatenate tuple (not "list") to tuple
# #t = t1 + [2, 3, 4]
#
# print(('Hi') * 4)    # HiHiHiHi
# print(('Hi',) * 4)   # ('Hi', 'Hi', 'Hi', 'Hi')


# tup = 1, 2, 3, 4, 5
# a, b, c, d, e = tup     # normal unpacking
# a, _, _, _, _ = tup     # what If i don't care? use _ a common notation
#
# # what if I am not sure from the total number? use *
#     # * here refers to varying number of arguments
# a, b, *c = tup
# print(c)    # [3, 4, 5]
#
# *a, b, c = tup
# print(a)    # [1, 2, 3]
#
# a, *b, c = tup
# print(b)    # [2, 3, 4]
#
# a, *b, c, d = tup
# print(b)    # [2, 3]
#
# # Although we can do the same with slicing
# # but the * operator is more elegant and makes code simpler!
#
# def f(*items):
#     print(items)  # (1, 2, 3, 4)
#
# f(1, 2, 3, 4)


# * unpacking operator

# lst = [1, 2, 3]
# print(lst)      # [1, 2, 3]
# print(*lst)     # 1 2 3   unpack first, then print: print received 3 arguments NOT 1
#
# def f(a, b):
#     print(a+b)
#
# #f(*lst)    f() takes 2 positional arguments but 3 were given
#
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# conc = [*lst1, *lst2]
# print(conc) # [1, 2, 3, 4, 5, 6]


# tup = 1, 2, (5, 6)
#
# #ValueError: not enough values to unpack (expected 4, got 3)
# #a, b, c, d = lst
#
# print(len(tup)) # 3
#
# # deep unpacking
# a, b, (c, d) = tup
# print(a, b, c, d)   # 1 2 5 6
#
# t = 1, 2, 3, (4, (5, 6))
# a, b, c, (d, (e, f)) = t
# print(a, b, c, d, e, f) # 1 2 3 4 5 6


# def f():
#     return ((10, 20), (30, 40))
#
# (x, y), (w, z)  = f()
# print(w)    # 30_oop
#
# all = f()
# print(all)          # ((10, 20), (30_oop, 40))
# sub = all[0]        # (10, 20)
# print(sub[1])       # 20
# print(all[0][1])    # 20
# print(f()[0][1])    # 20




# When you have multiple sequences and want to iterate
# such that in each iteration you have a single item
# from each sequence ==> you need zip

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
#
# # zip class constructor: def __init__(self, *iterables)
# # it takes a group of iterables
# # it then returns iterator that we can use to iterate
#
# zipped = zip(numbers, letters)
#
# print(list(zipped))
# # [(1, 'a'), (2, 'b'), (3, 'c')]
#
# words = ["mostafa", 'saad', 'ibrahim']
# print(list(zip(numbers, letters, words)))
# # [(1, 'a', 'mostafa'), (2, 'b', 'saad'), (3, 'c', 'ibrahim')]
#
# # note: zip() in Python 3 is different than Python 2


# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# words = ["mostafa", 'saad', 'ibrahim']
#
# for tuple_item in zip(numbers, words, letters):
#     print(tuple_item)
#
# """
# (1, 'mostafa', 'a')
# (2, 'saad', 'b')
# (3, 'ibrahim', 'c')
# """
#
# for number, word, letter in zip(numbers, words, letters):
#     print(number, word, letter)
# """1 mostafa a
# 2 saad b
# 3 ibrahim c"""



# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# words = ["mostafa", 'saad', 'ibrahim']
#
# for idx, tuple_item in enumerate(zip(numbers, words, letters)):
#     print(idx, tuple_item)
#
# """
# 0 (1, 'mostafa', 'a')
# 1 (2, 'saad', 'b')
# 2 (3, 'ibrahim', 'c')
# """
#
# for idx, (number, word, letter) in enumerate(zip(numbers, words, letters)):
#     print(idx, number, word, letter)
# """0 1 mostafa a
# 1 2 saad b
# 2 3 ibrahim c"""



# # what if sequences are of different length?
# # It stops at the shortest length
#
# items = list(zip(range(10, 15), range(100)))
# print(items)
# # [(10, 0), (11, 1), (12, 2), (13, 3), (14, 4)]
# # observe stopped only after 5 elements!
#
# # unzip
# seq1, seq2 = zip(*items)
# print(seq1)     # (10, 11, 12, 13, 14)
# print(seq2)     # (0, 1, 2, 3, 4)
















