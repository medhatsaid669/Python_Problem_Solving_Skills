# *args and **kwargs

# *args (positional expansion)
# Recall
# tup = 1, 2, 3, 4, 5
# # * => varying number
# a, b, *c = tup      # 1, 2, [3, 4, 5]
# *a, b, c = tup      # [1, 2, 3], 4, 5
# a, *b, c = tup      # 1, [2, 3, 4], 5
# a, *b, c, d = tup   # 1, [2, 3], 4, 5
#
# def f(*args):   # receive varying arguments
#     print(args)
#
# f(1, 2, 3, 4, 5)    # (1, 2, 3, 4, 5)
# f(tup)              # ((1, 2, 3, 4, 5),)
# f(*tup)             # (1, 2, 3, 4, 5)

# *args
# Recall

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(lst1)      # [1, 2, 3]
# print(*lst1)     # 1 2 3   unpack first, then print
#
# conc = [*lst1, *lst2]   # [1, 2, 3, 4, 5, 6] conc lists
#
# l1, l2, l3 = zip(*zip(lst1, lst2, lst3))
# print(l1, l2, l3)   # (1, 2, 3) (4, 5, 6) (7, 8, 9)
# # transpose(tranpose(matrix)) = matrix

"""**kwargs (Keyword Arguments / keyword expansion)
● **kwargs is similar to *args
○ * args      accepts positional arguments (tuple of items)
○ **kwargs accepts keyword
                      ( dict
 of items)
● Reading: What to call them? Eg. Splat in Ruby community """

"""**kwargs
● We can pass a varying number of keywords
● All of the passed items will be as a dictionary
○ name = ‘mostafa’
○ Name will be a key (string)
○ ‘mostafa’ will be a value"""

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
# hello(a="Mostafa", b=10, c=(1, 2, 5))

"""
a Mostafa
b 10
c (1, 2, 5)"""

"""*args, **kwargs
● We can have both of them together, but respect the order"""

# def f(*args, **kwargs):
#     print('args', args, 'kwargs', kwargs)
#
# f(1, 2)             # args (1, 2) kwargs {}
#
# f(a=10, b=20)       # args () kwargs {'a': 10, 'b': 20}
#
# f(1, 2, a=10, b=20) # args (1, 2) kwargs {'a': 10, 'b': 20}
#
# #f(a=10, 1)  # CE positional argument follows keyword argument
#
# #def f(**kwargs, *args):    # wrong

# Standard, positional and keyword arguments

# def f(a, b, *myargs, **mykwargs):
#     print(a, b, 'args', myargs, 'kwargs', mykwargs)
#
# f(1, 2)             # 1 2 args () kwargs {}
#
# f(a=10, b=20)       # 10 20 args () kwargs {}
#
# #f(x=10, y=20)
# # TypeError: f() missing 2 required positional arguments: 'a' and 'b'
#
# f(1, 2, x=10, y=20) # 1 2 args () kwargs {'x': 10, 'y': 20}
#
# f(1, 2, 3, 4, 5, x=10, y=20)   # 1 2 args (3, 4, 5) kwargs {'x': 10, 'y': 20}
#
# #f(a=1, b=2, a=10, b=20)  # SyntaxError: keyword argument repeated
#
# # Order: Standard arguments, *args arguments, **kwargs arguments

"""Merging Dictionaries
● **dict will expand to its tuple of (key, value), hence we can build new dict from it"""

# dct1 = {'A': 10, 'B': 20}
# dct2 = {'C': 30, 'D': 40}
#
# print(*dct1)    # A B
#
# # merging dictionaries
# dct = {**dct1, **dct2}
# print(dct)
# # {'A': 10, 'B': 20, 'C': 30, 'D': 40}

# Assigning Functions

"""Variable = Function
● Python is a flexible language
● We can assign functions to variables
● This can allow several flexible codes"""

# def fun(a, b):
#     return a+b, a-b
#
# if __name__ == '__main__':
#     print(fun(10, 3))   # (13, 7)
#
#     # function as variable name
#     my_fun = fun
#     print(my_fun(10, 3))  # (13, 7)

# Passing functions

# def process(iterable, fun):
#     """Iterate on the iterable, apply function and reutmr sum"""
#     sum = 0
#     for value in iterable:
#         sum += fun(value)
#
#     return sum
#
# lst = [2, -4, 6]
#
# print(process(lst, abs))    # 12
#
# def sq(n):
#     return n*n
#
# print(process(lst, sq))     # 56
#
# funcs = [abs, sq]   # list of functions
# for f in funcs:
#     print(process(lst, f))

# Key argument

# lst = ['I', 'am', 'Mostafa', 'and', 'You']
# print(sorted(lst))                      # ['I', 'Mostafa', 'You', 'am', 'and']
#
# # key: will be used to compare elements
# print(sorted(lst, key = str.lower))     # ['am', 'and', 'I', 'Mostafa', 'You']
#
# print(sorted(lst, key = len))           # ['I', 'am', 'and', 'You', 'Mostafa']
#
# def fun(string):
#     if not string:
#         return ''
#     return string[-1].lower()
#
# print(sorted(lst, key = fun))           # ['Mostafa', 'and', 'I', 'am', 'You']
#
# n = len(max(lst, key=len))  # 7 = length of longest string in list!
#
# def get_key(id):
#     if id == 1:
#         return str.lower
#     return len

"""Replacing methods
● It is not common, but we can now even replace a method with another"""

# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def print(self):
#         print(self.name)
#
# def hack():
#     print('Hey!')
#
# if __name__ == '__main__':
#     emp = Employee('Mostafa')
#     emp.print() # Mostafa
#
#     emp.print = hack
#     emp.print() # Hey!


# Everything is object! Even functions.

# def fun():
#     fun.counter += 1
#     print(fun.counter)
#
# print(type(fun))  # <class 'function'>
#
# # everything in python is object: so function var is an object!
# # this means it has attributes!
#
# print(fun.__dict__) # {}
# fun.counter = 0
#
# fun()   # 1
# fun()   # 2
# fun()   # 3
#
# # we typically don't do that, just to administrate the idea!

# Nested function
"""Nested Functions
● We can create a function inside 
a function inside a function!
● We call them nested or inner!"""

# def abs_sum(a, b, c):
#     # we can define a nested (inner function)
#     # hidden from the global scope (hidden)
#     def my_abs(x):
#         if x < 0:
#             return -x
#         return x
#
#     return my_abs(a) + my_abs(b) + my_abs(c)
#
# print(abs_sum(10, -20, 30)) # 60
# #print(my_abs(10))  not defined
# #abs_sum.my_abs  no attribute 'my_abs'
#
# # But why doing so? Hiding?
# # Better provide an outer function _my_abs

"""Scope
● Back then, we mentioned about scopes and referred to enclosing scope!"""

# def outer():
#     outer_loc1 = 30 # for inner func: this is an enclosing scope
#
#     def inner():
#         print(outer_loc1)   # 30: local? No. Enclosing? Yes, use it
#     inner()
#
# outer()
#
# """
# But how python searches for variable?
# We learned before about local, global and built-in"""

"""● Back then, we mentioned about scopes and referred to enclosing scope!
Namespaces
● In a Python program, there are four types of namespaces:
○ Built-In  (e.g. len, int, max, sum, TypeError, etc)
○ Global: contains any names defined at the level of the main program
○ Enclosing: for nested functions: the scope of the enclosing function
○ Local: local to the function and remains in existence until the function terminates.
● Using a variable in a function: Python search order?
○ Is it local? Then it is a local variable in a local namespace
○ Is it enclosing? Then it enclosing namespace
○ Is it global? Then it global namespace
○ Is it in Built-In? Then it Built-In namespace
○ None? Error"""

# LEGB Rule

# glob1 = 20   # global
#
# def outer():
#     outer_loc1 = 30
#     x = 15          # another outer local
#
#     def inner():
#         inner_loc = -5
#         x = 7       # another inner local
#         print(inner_loc)    # -5
#         print(x)            # 7: is it in my local scope? Yes, use it
#         print(outer_loc1)   # 30: local? No. Enclosing? Yes, use it
#         print(outer_loc2)   # 40: local? No. Enclosing? Yes, use it
#         print(glob1)        # 20: local? no, enc? no, global? Yes, use
#
#     outer_loc2 = 40
#     inner()
#     print(x)    # 15: local? yes, use it. inner x has no effect
#
# outer()

"""nonlocal
● nonlocal keyword helps us modify variables in enclosing scope """

# glob1 = 20   # global
#
# def outer():
#     outer_loc1 = 30
#
#     def inner():
#         #glob1 += 1         # UnboundLocalError
#         #outer_loc1 += 1    # UnboundLocalError
#
#         global glob1
#         glob1 += 1
#         nonlocal outer_loc1
#         outer_loc1 += 1
#
#     inner()
#     print(outer_loc1)   # 31
#
# outer()
# print(glob1)    # 21

# Closure
"""Enclosing scope
● 2 useful use cases for nested functions that access enclosing scope
● 1) DRY (Don’t repeat yourself)
○ If there is a logic that repeats a lot, just move to inner function
○ E.g. you do some preprocessing for something, then write a line to file
■ You need to access some of the available vars in the enclosing scope
● 2) Closure
○ The outer function return the inner function (not calling result)
■ inner not inner(10, 20)
○ The returned function will REMEMBER the used enclosing variables EVEN after the return!
■ It captures variables NOT values
■ Used with Python Decorators (later)"""

"""Closure
● The return of inner is a closure that 
will keep binding with enclosing variables x and y"""

# def outer(x):
#     y = 20
#     print(id(y))
#
#     def inner(f):
#         print(id(y))
#         return x + y + f
#
#     return inner
#
# if __name__ == '__main__':
#     f = outer(10)
#     print(f(30))  # 60: 10 + 20 + 30
#     print(f(40))  # 70: 10 + 20 + 40
#
#     print(outer(100)(5))    # 125

# Example

# def init():
#     class CustomersDataBase:
#         def load_database(self):
#             nonlocal users_ids
#             users_ids += [3, 4]
#
#         def add_id(self, id):
#             if id not in users_ids:
#                 print(f'Adding {id}')
#                 # doesn't need nonlocal
#                 users_ids.append(id)
#                 print(users_ids)
#             else:
#                 print(f'{id} is already there')
#
#     users_ids = [1, 2]
#     db = CustomersDataBase()
#     db.load_database()
#
#     return db.add_id
#
#
# def go1(adder):
#     adder(4)
#     adder(5)
#
# def go2(adder):
#     adder(6)
#
# if __name__ == '__main__':
#     id_adder = init()
#     go1(id_adder)
#     go2(id_adder)
# """
# 4 is already there
# Adding 5
# [1, 2, 3, 4, 5]
# Adding 6
# [1, 2, 3, 4, 5, 6]"""

"""Be Careful
● Variable i is captured in f(), but 
although each capture has i with 
specific value, after we return, the final 
i value is used. Closures capture 
variables NOT values"""

# def fun():
#     lst = []
#
#     for i in range(3):
#         def f():
#             return i
#         lst.append(f)
#     # all f captures var i (not value)
#     # by end of fun(), i = 2
#     return lst
#
#
# lst = fun()
# for f in lst:
#     print(f())
#
# """
# 2
# 2
# 2
# """

"""Workaround
● Add parameter with default value"""

# def fun():
#     lst = []
#
#     for i in range(3):
#         def f(i = i):   # pass as default value
#             return i
#         lst.append(f)
#     # all f captures var i (not value)
#     # by end of fun(), i = 2
#     return lst
#
#
# lst = fun()
# for f in lst:
#     print(f())
#
# """
# 0
# 1
# 2
# """

# Lambda Function
"""Lambda function
● An anonymous function is a function without a name.
○ We call them lambda function (or expression) also
● Pros:
○ Shorthand notation that makes some code use cases nicer sometime
● Cons:
○ No good stacktrace
■ You better use it for simple things that probably won’t cause problems
○ It doesn’t work well with static type checker (
like  or ) [future]
■ In python 3: we can indicate expected type
○ Limited for only a single expression, NO statements"""

"""From normal function to lambda
● Compare the normal function with lambda 
function to observe the syntax changes"""

# def sq1(x):
#     return x * x
#
# print(sq1(3))    # 9
#
# sq2 = lambda x: x * x
#
# print(sq2(3))    # 9
#
# def name1(first, second):
#     return f'{first} - {second}'
#
# print(name1('mostafa', 'saad'))  # mostafa - saad
#
# name2 =  lambda first, second: f'{first} - {second}'
#
# print(name2('mostafa', 'saad'))  # mostafa - saad
#
# print((lambda x, y: x * y)(2, 4))   # 8

# From normal function to lambda

# def process1(iterable, fun):
#     """Iterate on the iterable, apply function and reutmr sum"""
#     sum = 0
#     for value in iterable:
#         sum += fun(value)
#
#     return sum
#
# process2 = lambda iterable, fun: sum([fun(value) for value in iterable])
#
# lst = [2, -4, 6]
#
# print(process1(lst, abs))    # 12
# print(process2(lst, abs))    # 12
#
# print(process2(lst, lambda x: x * x))    # 56

# With Higher Order Functions

# lst = ['I', 'am', 'Mostafa', 'and', 'You', '']
#
#
# def fun(string):
#     if not string:
#         return ''
#     return string[-1].lower()
#
# print(sorted(lst, key = lambda string : '' if not string else string[-1].lower()))
# print(sorted(lst, key = lambda string : string[-1].lower() if string else ''))
# # ['Mostafa', 'and', 'I', 'am', 'You']
#
# # btw we call sorted: higher order functions
#     # means it receives a function

# Like normal functions

# support all the different ways of passing arguments

# s = lambda *args: sum(args)
# print(s(1, 2, 3))    # 6
#
# res = (lambda **kwargs: sum(kwargs.values()))(A=1, B=2, C=3, D=4)
# print(res)  # 10
#
# # It access local and enclosing vars. Return as a closure
# glob = 5
# def f():
#     x = 10
#     fun = lambda y : y + x + glob
#
#     return fun
#
# fun = f()
# print(fun(3))   # 18: 5+10+3

# Single Expression ONLY

# Recall: expression => evalautes to a value
    # 2 * x + 1, x * x, x == 2, somefun(.)

# statement doesn't necessairly
    # x = 2, assert x == 2, etc
    # In python 2: print was a statement

# lambda allows 1 single expression (could long / multiline)
    # It doesn't allow statements

#f = lambda x: assert x == 2 # invalid syntax

# f = lambda x : print(x, x*x, 2*x)   # return None
#
#
# print(f(5))
# # 5 25 10
# # None

"""Finally
● There are debates around lambda and their usage / issues
● I like this quote: “lambda functions are perfectly Pythonic if there is nothing 
more Pythonic available”
● Replacements include list comprehension, map, filter, reduce [future]
○ We already knows the first 2 
● Future reading"""


# Function and Variable Type Annotations
"""PEP
● PEP stands for Python Enhancement Proposal: a design document providing 
information to the Python community, or describing a new feature for Python 
or its processes or environment.
● PEP 8: Style Guide for Python Code
○ E.g. too many blank lines
● Function Annotations – 
PEP 3107 / Type Hints - 
PEP 484"""

"""Function Annotations
● We can state the expected data type for the arguments and return
● However, python interpreter just discard them!
○ But they still can communicate for the user what type of arguments to pass!
○ Also, some third library static type checker (e.g. mypy) can be applied before running code!"""

# def add(x: float, y: float) -> float:
#     print(add.__annotations__)
#     # {'x': <class 'float'>, 'y': <class 'float'>, 'return': <class 'float'>}
#     return x + y
#
# print(add(2, 7))        # 9
# print(add('2', '7'))    # 27

"""Type Hints
● We can even state the expected data type for the variables!"""

# def mylist(x: str, y) -> list:
#     # variable type
#     z : str = x + y
#     res : list = [x, y, z]
#
#     print(mylist.__annotations__)
#     # {'x': <class 'str'>, 'return': <class 'list'>}
#
#     return res
#
# mylist(10, 20)

"""Complex typing
● What if I would like to return something that could be 2+ data types?
○ Use Union to indicate them
○ Optional[] means can be None"""

# from typing import Union
#
# def div1(x: float, y: float) -> Union[float, None]:
#     if y == 0:
#         return None
#     return x / y
#
# from typing import Optional
#
# def div2(x: float, y: float) -> Optional[float]:    # same as above
#     if y == 0:
#         return None
#     return x / y

# Complex typing: More

# from typing import Union, List, Tuple, Dict
#
# def f1() -> List[int]:
#     return [1, 2, 3]
#
# def f2() -> List[Union[int, str, None]]:
#     return ['most', 26, None, 1]
#     #return ['most', 26, None, 1, 1.5]
#
# t1 : List[Union[float, str, bool]] = [10, True, 'hey']
# t2 : List[List[int]] =  [[1, 2], [3, 4]]
# t3 : List[List[Union[int, str]]] =  [[1, 2], ['hey', 4]]
# t4 : Tuple[int, int, str] = (10, 20, 'hey') # u have to state them
# t5 : Tuple[int, ...] = (1, 2, 3, 4)
# t6 : Tuple = (1, 2.5, 'he')
# t7 : Dict[str, int] = {'most' : 10, 'hey' : 20}
#
# # Above is Python 3.8 and earlier
# # from 3.9+ it will be e.g. list/tuple, NOT List/Tuple

"""Overall
● Python interpreter doesn’t consider them
○ You expect int, but still float or string work well (e.g. a + b)
● Using them may encourage you think about your I/O & code logic
● Communicate clearly the arguments & return, especially for APIs
● There are 3rd party tools to statically check your code (mypy)
● There is a debate around using them: Is it pythonic?
○ Replacement: Duck typing + try-except block
● Think: is it added value to use? If yes, use them wisely
● Future Reading"""

"""mypy tool
● In some companies, some 3rd libraries can be used to statically check
○ Popular one such as pymy: pip3 install mypy"""

# def div(x: float, y: float) -> float:
#     if y == 0:
#         return None
#     return x / y
#
# div(10, 20)
# div(10, 'most')


# More Functions Homework

"""Consider
● For simplicity in all this homework assume the following:
○ Iterables are list, tuple, set or dict
○ Their values aren’t None
● Constraints:
○ Don’t use len function
○ Pass functions as lambda functions when convenient """

"""Problem #1: Filter (easy)
● This function takes a function (filter) and an iterable. It returns a list of the 
filtered list
● Below, we try it with is_even function to remove odd numbers
● Replace is_even with lambda"""

# def myfilter(func, iterable):
#     return [item for item in iterable if func(item)]
#
# def is_even(n):
#     return n % 2 == 0
#
# res = myfilter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6, 10, 13])
#
# print(res)  # [2, 4, 6, 10]

"""Problem #2: Reduce v1
● Reduce function reduces a complete iterable to a single value by applying a 
given function. So with add function it adds all of them. With multiply, it 
multiplies all of them. The function takes 2 arguments always
● E.g. for sum(a, b) and [2, 5, 6, 7, 8]
○ Sum 2 + 5 ⇒ 7
○ Sum 7 + 6 = 13
○ Sum 13 + 7 = 20
○ Sum 20 + 8 = 20
● Try it with some lambda for:
○ sum, multiply,  max, min"""

# def myreduce(func, iterable, init = None):
#     if not iterable:
#         if init is None:
#             raise TypeError('reduce of empty sequence with no initial value')
#         return init
#
#     for item in iterable:
#         if init is None:
#             init = item
#         else:
#             init = func(init, item)
#     return init
#
# print(myreduce(max, {7, 20, 10}))   # 20
#
# print(myreduce(lambda a, b: a if a > b else b, {7, 20, 10}))
#
# # Our myreduce definition is limited as it implies None can't be in the list nor as default value!
# # There are ways to handle that, but let's keep it simple

"""Problem #2: Reduce v1
● Init value: the default value is None
● If init is given, think of it as a first element in your iterable
● In case of empty iterable:
○ If init is not None, return it
○ Otherwise raise type error with msg reduce of empty sequence with no initial value"""


"""Problem #3: Reduce v2
●
def 
myreduce(func1_overall, func2_consecutive, iterable)
● In this version we are given 2 functions:
○ Func2_consecutive is applied on every 2 consecutive numbers
○ Func1_overall is applied on their results (similar logic to last function)
○ Both of them takes 2 arguments
● Assume Func1 is multiplication and Func2 is addition
○ Input: [2, 5, 3, 4, 5, 10] ⇒ (2 + 5) * (3 + 4) * (5 + 10) = 735
○ So divide to pairs, apply func2, and apply func1 over all of them
● Don’t use len functions
● If len < 2: raise error: The length of the sequence must be at least 2
● If len is not even: The length of the sequence must be even"""

# def myreduce(func1_overall, func2_consecutive, iterable):
#     try:
#         first, second, *iterable = iterable
#         res = func2_consecutive(first, second)
#     except:
#         return RuntimeError('The length of the sequence must be at least 2')
#
#     while iterable:
#         try:
#             first, second, *iterable = iterable
#         except:
#             return RuntimeError('The length of the sequence must be even')
#         res = func1_overall(res, func2_consecutive(first, second))
#     return res
#
#
# print(myreduce(lambda a, b: a * b, lambda a, b: a + b, [2, 5, 3, 4, 5, 10]))


"""Problem #4: Map
● This function receives a function and a variable number of iterables
○ Say 5 iterables, then the passed function must receive 5 arguments
● map picks the top element from each iterable, pass them to the function and 
append the result to a list. It then picks the next top elements. It stops at the 
shortest length among iterables
● Note: Its code should be a single short line"""

# def mymap(func, *iterables):
#     return [func(*tup) for tup in zip(*iterables)]
#
# def multi_abs(a, b, c):
#     return abs(a) * abs(b) * abs(c)
#
# res = mymap(multi_abs, [1, -2, 3, 2], [-4, 5, 6, 7], [4, -5, -10, 9, 11])
#
# print(res)  # [16, 50, 180, 126]

"""Problem #5: Nested Lambda
● Nested if, loop, function, class and even lambda are no new syntax rather 
than utilizing what we learned
● First, develop a function that takes values for a range:
○
def 
ff(st, en, step)
○ The function returns a closure that receives argument function f to apply on all the range and 
return result as list. For example for a square function and range(2, 6, 1)
○
○
processor = ff(2, 6, 1)
print
(processor(sq)) ⇒ [4, 9, 16, 25]
● Second, rewrite the above function as a nested lambda. Same usage"""

# sq = lambda x : x * x
#
# def ff1(st, en, step):
#     def inner(f):
#         return [f(val) for val in range(st, en, step)]
#
#     return inner
#
# processor = ff1(2, 6, 1)
# print(processor(sq))
#
# ff2 = lambda st, en, step: lambda f: [f(val) for val in range(st, en, step)]
# processor = ff2(5, 1, -1)
# print(processor(sq))

