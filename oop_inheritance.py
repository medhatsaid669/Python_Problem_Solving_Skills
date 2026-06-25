# Inheritance 1: Motivation

"""Common Vs Unique
● Assume we are modeling a system for a Teacher
○ There are many classes such as Student and Teacher
● Think in classes for both of them
○ What might be common attributes and methods?
○ What might be unique attributes and methods?
○ Any critical observation?"""

# class Student:
#     def __init__(self):
#         self.name = None
#         self.email = None
#         self.address = None
#         self.national_id = None
#         self.starting_study_year = None
#         self.gpa = None
#         self.studied_courses = []
#
#     def is_valid_email(self, email):
#         pass
#     def add_course_grade(self, course_id, grade):
#         pass
#     def print_grades(self):
#         pass
#
#
# class Teacher:
#     def __init__(self):
#         self.name = None
#         self.email = None
#         self.address = None
#         self.national_id = None
#         self.starting_employement_year = None
#         self.current_salary = None
#         self.teaching_courses = []
#
#     def is_valid_email(self, email):
#         pass
#
#     def add_course(self, course_id):
#         pass

"""Is-a relationship
● Student is-a person. Teacher is-a person. Dean is-a person
○ So some common attributes/methods + some unique attributes/methods
● Circle is-a shape. 
○ Rectangle is-a shape. Triangle is-a shape. 
● Software Engineer is-an employee. 
○ Manager is-an employee. 
○ Office Boy is-an employee
● Apple is-a fruit. Orange is-a fruit. Watermelon is-a fruit
● (Wagon / Bicycle / Motor vehicle / Railed vehicle) is-a vehicle"""

# Inheritance 2: Single Inheritance

"""Back to the Student vs Teacher
● How can we avoid duplicating code in this problem?
○ Inheritance allow us to reuse code!"""

"""Inheritance in Python
● When Class A inherits Class B, it inherits its created attributes, properties 
& methods: We call A (Parent/Base) and B (Child/Derived)
○ Here Person is Base and Student is Derived"""

"""Inheritance in Python
● The parent neither know nor 
affected by the child
● Student class has print_info 
in base class, but then 
newone override it
○ Think: Reassign variable"""

# class Person:
#     def __init__(self):
#         self.name = 'Mostafa'
#         self.email = 'Mostafa@gmail.com'
#
#     def is_valid_email(self):
#         return  self.email.endswith('@gmail.com')
#
#     def print_info(self):
#         print(self.name, self.email)
#
# class Student(Person):
#     def __init__(self):
#         Person.__init__(self)   # Call parent init
#         self.GPA = .5
#         self.studied_courses = ['C++', 'Python']
#
#     def print_info(self):
#         print(self.name, self.GPA)
#
# if __name__ == '__main__':
#     st = Student()
#     st.print_info() # Mostafa 0.5
#     print(st.email) # Mostafa@gmail.com
#     print(st.is_valid_email())  # True
#
#     p = Person()
#     p.name, p.email = 'Noha', 'Noha@hotmail.com'
#     p.print_info()  # Noha Noha@hotmail.com
#     print(p.is_valid_email())   # False
#
#     print(type(st))     # <class '__main__.Student'>
#     print(isinstance(st, Student))          # True
#     print(isinstance(st, Person))           # True
#
#     print(type(st) is Student)              # True
#     print(type(st) is Person)               # False
#     print(type(st) in [Student, Person])    # True
#
#     print(issubclass(Student, Person))      # True
#     print(issubclass(Student, Student))     # True
#     print(issubclass(Student, list))        # False
#     #print(issubclass(st, Person))          # Error: class NOT object
#     print(issubclass(type(st), Person))     # True
#
#     # Be careful from type vs isinstance
#     # isinstance considers inheritance, type don't
#
#     print(issubclass(Person, object))      # True
#     print(issubclass(Student, object))     # True
#     print(issubclass(list, object))        # True
#     print(issubclass(int, object))         # True: int is object
#     print(issubclass(BaseException, object))  # True
#
#     import math
#     print(isinstance(math, object))         # True: module is object
#     print(isinstance(math.sqrt, object))    # True
#
#     # we actually inherit its attributes & methods
#     obj = object()
#     print(dir(obj)) # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
#     print(obj.__init__)
#     print(obj.__repr__())    # 0x7ff2b4169b90 default print memory address
#     print(object.__name__)   # on class level


# Inheritance with Super Function

"""Super Function
● An issue in previous calling for the parent is using the class name explicitly
○
Person.
__init__(
self)
○ With every class name change, you have to change it!
○ If you changed your inheritance hierarchy, you have to change it!
○ But Cons: Making code less explicit violates The Zen of Python
● Can we make things more dynamic? Yes super function
● super() returns an object of the superclass
○ Now we can just force call to its 
○ Later, I will explain more details__init__
● Note: Python 2 is a bit different"""

# Side note: Zen of Python (guiding principles)

# super() function

# class Person:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def print_info(self):
#         print(f'name: {self.name} ', end=' ')
#
# class Student(Person):
#     def __init__(self, name, email, gpa):
#         super().__init__(name, email)  # make it first line
#         self.gpa = gpa
#
#     def print_info(self):
#         super().print_info()    # Delegate to parent
#         print(f'GPA: {self.gpa}')
#
# if __name__ == '__main__':
#     st = Student('Mostafa', 'Mostafa@gmail.com', 3.82)
#     st.print_info()     # name: Mostafa  GPA: 3.82

# super() call order

# class Person:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.gpa = None
#
#     def print_info(self):
#         print(f'name: {self.name} ', end=' ')
#
# class Student(Person):
#     def __init__(self, name, email, gpa):
#         self.gpa = gpa
#         super().__init__(name, email)
#
#     def print_info(self):
#         super().print_info()
#         print(f'GPA: {self.gpa}')
#
# if __name__ == '__main__':
#     st = Student('Mostafa', 'Mostafa@gmail.com', 3.82)
#     st.print_info() # name: Mostafa  GPA: None

# Inheritance 4: Multilevel Inheritance

# 5 Inheritance relations types

# Multilevel Inheritance

# class A:
#     def __init__(self):
#         print('init A', self)
#     def f1(self):
#         print('f1A ')
#     def f2(self):
#         print('f2A ')
#     def f3(self):
#         print('f3A ')
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('init B', self)
#     def f1(self):
#         print('f1B ')
#     def f2(self):
#         print('f2B ')
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print('init C', self)
#     def f1(self):
#         print('f1C ')
#
#
# if __name__ == '__main__':
#
#     cobj = C()
#     cobj.f1()
#     cobj.f2()
#     cobj.f3()
#     # Guess output!

"""
init A <__main__.C object at 0x7fa42f069850>
init B <__main__.C object at 0x7fa42f069850>
init C <__main__.C object at 0x7fa42f069850>
f1C 
f2B 
f3A 
Observe: self is bound to cobj all the time! The created object
So any method call is bound to cobj all time
Many errors will be resolved by remembering that!
"""

# Multilevel Inheritance and Super()

# class A:
#     def f1(self):
#         return 'f1A'
#     def f2(self):
#         return 'f2A'
#     def f3(self):
#         return 'f3A'
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#     def f1(self):
#         return 'f1B ' + super().f1()
#     def f2(self):
#         return 'f2B ' + super().f2()
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#     def f1(self):
#         return 'f1C ' + super().f1()
#     def f3(self):
#         return 'f3C ' + super().f3()
#
# if __name__ == '__main__':
#
#     cobj = C()
#     print(cobj.f1())
#     print(cobj.f2())
#     print(cobj.f3())
#     # guess output?

"""
f1C f1B f1A
f2B f2A
f3C f3A
"""

# class A:
#     def f3(self):
#         return 'f3A ' + self.f4()
#         #return 'f3A' + super().f4()
#
# class B(A):
#     def f2(self):
#         return 'f2B ' + super().f3()
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#
#     def f1(self):
#         return 'f1C ' + self.f2()
#
#     def f3(self):
#         return super().f3() + '\t' + 'C - f3'
#
#     def f4(self):
#         return 'f4C '
#
# if __name__ == '__main__':
#     print(C().f1())     # f1C f2B f3A f4C
#     #print(B().f2())   B has no attribute f4
#     # self/methods/attributes bound to the
#     # CALLING INSTANCE not current class


# Inheritance Multiple Inheritance

# 5 Inheritance relations types

# Multiple Inheritance

# Basic multiple inheritance

# class ParentA:
#     def __init__(self, a):
#         self.a = a
#         print('init ParentA')
#
#     def fA(self):
#         print('fA')
#
# class ParentB:
#     def __init__(self, b):
#         self.b = b
#         print('init ParentB')
#
#     def fB(self):
#         print('fB')
#
# class ChildC(ParentA, ParentB):
#     def __init__(self, a, b, c):
#         ParentA.__init__(self, a)
#         ParentB.__init__(self, b)
#         self.c = c
#         print('init ChildC')
#
#     def fC(self):
#         print('fC')
#
# if __name__ == '__main__':
#     c = ChildC(1, 3, 5)
#     c.fA()
#     c.fB()
#     c.fC()

"""
init ParentA
init ParentB
init ChildC
fA
fB
fC
"""

"""Same function name
● If you are language designer, how to solve 
this confusion? 
● What might be the answer?"""

# class ParentA:
#     def f(self):
#         print('ParentA')
#
# class ParentB:
#     def f(self):
#         print('ParentB')
#
# class ChildC1(ParentA, ParentB):
#     pass
#
# class ChildC2(ParentB, ParentA):
#     pass
#
# if __name__ == '__main__':
#     print(ChildC1.__mro__)  # (ChildC1, ParentA, ParentB, object)
#
#     print(ChildC2.__mro__)  # (ChildC2, ParentB, ParentA, object)
#     ChildC2().f()           # ParentB is the left one

"""Method resolution order (MRO)
● A graph algorithm is used to find a proper ordering (C3 linearization).
○ In the previous case: we depends on the parents order left to right
● In complex hierarchy, things get complicated :("""

# class D2:
#     pass
#
# class C2(D2):
#     def f(self):
#         print('C2')
#
# class B2(C2):
#     def f(self):
#         print('B2')
#
# class D1:
#     pass
#
# class C1(D1):
#     def f(self):
#         print('C1')
#
# class B1(C1):
#     pass
#
# class A(B1, B2):
#     pass
#
# if __name__ == '__main__':
#     print(A.__mro__)
    # A, B1, C1, D1, B2, C2, D2, Object A().f() # C1

"""MRO in multilevel
● What is the classes order of A.__mro__?
● A, B1, C1, D1, B2, C2, D2
○ It ends with object - skip for now
● Assume Classes: C1, C2, and B2 has method F
○ Let’s call A().f(), which will be called?
○ C1 as it appeared first!
○ Note: code is provided
● Useful rules for mro:
○ Child class comes before its parents
○ For multiple parents: order left to right (of inheriting)
○ In multilevel:
■ Finish every branch in order from child to parent"""

"""MRO in multilevel and Simple multiple inheritance
● What is the classes order of A.__mro__?
● A, B1, X1, Y1, Z1, X2, B2, X3, Y2, Z2, X4
● Let’s view as a hierarchy
● A, 
○ B1, 
■ X1, 
● Y1, Z1
■ X2, 
○ B2, 
■ X3, 
● Y2, Z2
■ X4
● In graph they it will make sense with DFS"""

# class X4:
#     pass
#
# class Z2:
#     pass
#
# class Y2(Z2):
#     pass
#
# class X3(Y2):
#     pass
#
# class X2:
#     pass
#
# class Z1:
#     pass
#
# class Y1(Z1):
#     pass
#
# class X1(Y1):
#     pass
#
# class B2(X3, X4):
#     pass
#
# class B1(X1, X2):
#     pass
#
# class A(B1, B2):
#     pass
#
# if __name__ == '__main__':
#     print(A.__mro__)
    # A, B1, X1, Y1, Z1, X2, B2, X3, Y2, Z2, X4

"""MRO Exceptions
● If MRO couldn’t find consistent order, 
relative to its current algorithm, it will 
fail
● If you got this error, u typically is doing 
nonsense in the hierarchy
● 1) Draw it
● 2) Spot what is weird"""

# class A:
#         print('init A')
#
# class B(A):
#     def __init__(self):
#         print('init B')
#
# class C(A, B):
#     def __init__(self):
#         print('init D')
#
# C()
"""
TypeError: Cannot create a consistent 
method resolution order (MRO) for bases A, B
Note: class C(B, A): will work
"""

"""More
● In practice, we avoid multiple inheritance
○ One more video about super with inheritance
● So learn the concept and play with it, but don’t dig deep
● MRO is using an algorithm named C3 Linearization
○ It determines the order in complex hierarchies
○ You may understand it when you study graph theory, but no such big need """


# Multiple Inheritance with Super

""""super() function
● If you don’t get most of today or delay = no 
problem
● We previously mentioned: super() returns an 
object of the parent superclass
○ This is not so accurate. It has 2 mistakes.
○ It returns a proxy object (think the wrapper we took for 
now). It will delegate the call to a specific class. This is 
not an important part.
○ The returned class is NOT necessarily your parent! This 
is a critical part
■ Yah super() is more complicated 
● super() itself is an abbreviation for 
○ super(class, self)"""
#
# class A:
#     def __init__(self):
#         print('A')
#
# class B(A):
#     def __init__(self):
#         # super()
#         super(B, self).__init__()
#         # <class 'super'>
#         print(type(super(B, self)))
#         print(type(super()))
#         print('B')
#
# B()


"""Super and MRO
● Guessed init D, B, A?
○ Good trial, but wrong
○ Answer: init D, B, A, C
● The super() call finds the next 
method in the MRO at each step 
NOT necessarily one of your parents
○ At D, what is next? B. Super goes B.init
○ At B, what is next? A
○ At A, what is next? C
● Wait but A has NO parent?!
○ It is about MRO, not parents"""

# class A:
#     def __init__(self):
#         super().__init__()
#         print('init A')
#
# class B(A):
#     def __init__(self):
#         print('init B')
#         super().__init__()
#
# class C:
#     def __init__(self):
#         print('init C')
#         super().__init__()
#
# class D(B, C):
#     def __init__(self):
#         print('init D')
#         super().__init__()
#
# print(D.__mro__)    # D, B, A, C
# D()     # Guess the output
"""
init D
init B
init C
init A
"""

"""Super and MRO
● Let’s comment line 5
● Guess the output?
● Init D, B, A
● As A doesn’t make call for super, we 
stopped at this point.
○ No one is calling C.
● Super() here is doing very interesting 
work, but also this could be so annoying!"""

# class A:
#     def __init__(self):
#         #super().__init__()
#         print('init A')
#
# class B(A):
#     def __init__(self):
#         print('init B')
#         super().__init__()
#
# class C:
#     def __init__(self):
#         print('init C')
#         super().__init__()
#
# class D(B, C):
#     def __init__(self):
#         print('init D')
#         super().__init__()
#
# print(D.__mro__)    # D, B, A, C
# D()     # Guess the output

"""
init D
init B
init A
"""

"""Guess the output
● C.MRO = C, B, A
● At C
○ init C
○ Call explicitly A with 20
■ At A
● init A: 20
● super() calls after A ⇒ object
○ Call explicitly B
■ init B
● super() calls after B ⇒ A
○ At A
■ init A: None"""

# class A:
#     def __init__(self, aval = None):
#         print(f'init A: {aval}')
#         super().__init__()
#         self.aval = aval
#
# class B:
#     def __init__(self):
#         print('init B')
#         super().__init__()
#
# class C(B, A):
#     def __init__(self, aval):
#         print('init C')
#         A.__init__(self, aval)
#         B.__init__(self)
#
# print(C.__mro__)    # C, B, A
# C(20)
"""
init C
init A: 20
init B
init A: None
"""

"""Guess the output
● init C
● init A: 20
● init B
● TypeError: __init__() missing 1 
required positional argument: 'aval'
○ At line 12
● This will be shocking for some guys
○ B has no parent
○ super() init calls object init
○ Why do we need parameter?
○ We are actually calling A init NOT object init """

# class A:
#     def __init__(self, aval):
#         print(f'init A: {aval}')
#         super().__init__()
#         self.aval = aval
#
# class B:
#     def __init__(self):
#         print('init B')
#         super().__init__()
#
# class C(B, A):
#     def __init__(self, aval):
#         print('init C')
#         A.__init__(self, aval)
#         B.__init__(self)
#
# print(C.__mro__)    # C, B, A
# C(20)

"""● We know object class is common to all
● Sometimes we build such diamonds
● There are 2 issues
○ Language issue
■ Some languages are harder to handle
■ Python is good with MRO
○ Development issue
■ We get confused about function calls and typically do errors
● Tip: Don’t do such style!"""

# Inheritance with properties

"""With properties
● We simply inherit them
● But where problems may occur?
● Forgetting that: self is the calling instance """

# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.__salary = value
#
# class HourlyEmployee(Employee):
#     pass
#
# if __name__ == '__main__':
#     # inherits: init and properties
#     emp = HourlyEmployee(20)
#     print(emp.salary)
#     emp.salary = -30
#     print(emp.salary)

"""What is wrong?
● Trace the code and find the error"""

# class Employee:
#     def __init__(self, salary):
#         # self here will refer to the child class! whch doesn't has set!
#         self.salary = salary  # AttributeError: can't set attribute
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.__salary = value
#
# class HourlyEmployee(Employee):
#     extra = 100
#
#     # Override property: get only
#     @property
#     def salary(self):
#         return self.__salary + HourlyEmployee.extra
#
# if __name__ == '__main__':
#     # inherits: init and properties
#     emp = HourlyEmployee(20)
#     print(emp.salary)
#     emp.salary = -30
#     print(emp.salary)

"""Self?
● The key is to remember what is self
● Employee: has set/get property
● Override: get only
● Self wanna set"""

# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.__salary = value
#
# class HourlyEmployee(Employee):
#     extra = 100
#
#     # Override property: get & set
#     @property
#     def salary(self):
#         return self.__salary + HourlyEmployee.extra
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.__salary = value
#
# # depending on ur classes, you might have to do workarounds
# # e.g. separate set function
#
# if __name__ == '__main__':
#     # inherits: init and properties
#     emp = HourlyEmployee(20)
#     print(emp.salary)
#     emp.salary = -30
#     print(emp.salary)

"""So
● We can simply provide setter for the child class
● Or whatever solution
● Overall: Be careful and remember what is self: the calling instance
● Also remember: when u override a property, you cancel its get/set"""


# Inheritance with Static vars

# Static variables!

# class A:
#     shared = 10
#
#     def f(self):
#         print(self.shared, A.shared, type(self).shared)
#
# class B(A):
#     shared = 5
#
# if __name__ == '__main__':
#     b = B()
#     b.f()   # 5 10 5
#     b.shared = 7
#     b.f()   # 7 10 5

    # This is where using self with static vars plays critical role
    # Old tip: Access/modify the class attributes using the Class name
    # Considering inheritance: type(self) plays a good role here
    # Also think if inheritance should have effect or not
    # Note: type(self) is same as self.__class__
    # Better don't access dunder things directly


"""MRO!
● When changing a static variable, you have to remember the MRO rules and what we learned about static vars"""

# class A:
#     shared = 1
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# if __name__ == '__main__':
#     print(A.shared, B.shared, C.shared)  # 1 1 1
#     A.shared = 3
#     print(A.shared, B.shared, C.shared)  # 3 3 3
#     # With MRO: B and C, use A.shared
#
#     B.shared = 5    # Now B has its own shared
#     print(A.shared, B.shared, C.shared)  # 3 5 3
#     # Still C with MRO use A.shared
#
#     A.shared = 7
#     print(A.shared, B.shared, C.shared)  # 7 5 7
#     # B has its own one. MRO stops directly

"""With static methods
● Intuitive, nothing specific"""

# class A:
#     @staticmethod
#     def hello():
#         print('hello')
#
#     @staticmethod
#     def world():
#         print('world from A')
#
# class B(A):
#     @staticmethod
#     def world():
#         print('world from B')
#
# if __name__ == '__main__':
#     B.hello()   # hello
#     B.world()   # world from B


# Inheritance with Exceptions

# All True
# print(issubclass(Exception, BaseException))
# print(issubclass(ArithmeticError, BaseException))
# print(issubclass(ArithmeticError, Exception))
# print(issubclass(ZeroDivisionError, ArithmeticError))
# print(issubclass(PermissionError, Exception))
#
# print(issubclass(SystemExit, Exception))        # False
# print(issubclass(SystemExit, BaseException))    # True

# Order of Exceptions
#
# try:
#     path = input()
#     file = open(path, 'r')
#     file.close()
# except FileNotFoundError:
#     print('FileNotFoundError')
# except PermissionError:
#     print('PermissionError')
# except OSError:
#     print('Interrupted or Timeout errors')
# except Exception as e:
#     print(e)


# try:
#     path = input()
#     file = open(path, 'r')
#     file.close()
# except OSError:
#     print('OSError')
# except FileNotFoundError:
#     print('FileNotFoundError')
# except PermissionError:
#     print('PermissionError')
# except Exception as e:
#     print(e)

"""
not_exist.txt     ==> OSError
/boot/efi/        ==> OSError
"""

"""
not_exist.txt     ==> FileNotFoundError
/boot/efi/        ==> PermissionError
"""

"""Order of Exceptions
● You must make a child class FIRST before its PARENT class
○ Otherwise: the child class will never be triggered"""

# User-Defined Exception

# class StrNoAllowed1:
#     pass
#
# #TypeError: exceptions must derive from BaseException
# #raise StrNoAllowed1
#
# # You must extend from built-in exceptions
# class StrNoAllowed2(BaseException):
#     pass
#
# raise StrNoAllowed2


# User-Defined Exception

# class PaymentBaseException(BaseException):
#     pass
#
# class NegativePaymentException(PaymentBaseException):
#     def __init__(self, money, message = 'Paid amount must be positive'):
#         self.money = money
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f'{self.money} amount caused error. \n\tSee: {self.message}'
#
# raise NegativePaymentException(-20)

"""
__main__.NegativePaymentException: -20 amount caused error. 
	See: Paid amount must be positive
"""

"""Industrial Tip
● For your application: Create a parent exception
○ E.g. PaymentBaseException
● Let all your customized exceptions inherit from it
○ Now called to your API can gaurntee catching issues coming from your API"""


# Inheritance with Slots

"""Slots
● Sometimes we need to create thousands of instances from a specific class
○ Think Geometry Point, Article, Employee, etc
● We know the attributes of a class stored in __dict__
● Dict is strong, but slow and memory consuming on object level!
○ This means set/get the attributes will be: slow 
● Slots is another mechanism for handling the attributes
○ Faster in access and consumes less memory
○ But a bit not flexible in extending the object with new attributes
○ But there are some workarounds"""

# The normal way

# class Employee:
#     employees_cnt = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# emp = Employee('most', 12)
# print(dir(emp)) # 'employees_cnt', 'name', 'salary'
# print(emp.name) # most
#
# print(Employee.__dict__)    # {'employees_cnt': 0, '__doc__': None, etc}
# print(emp.__dict__)  # {'name': 'mostafa'}
# print(vars(emp))     # {'name': 'mostafa'}


"""With slots
● Almost same usage, but observe the inflexibility"""

# class Employee:
#     employees_cnt = 0
#     __slots__ = "name", "salary"    # tuple/iterable
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         #self.age = 1   # u can't
#
# print(Employee.__dict__)    # {'employees_cnt': 0, '__doc__': None, etc}
# emp = Employee('most', 12)
# print(dir(emp)) # 'employees_cnt': 0, '__slots__': ['name', 'salary']
#                 # 'name': <member 'name' of 'Employee' objects>, 'salary':
# print(emp.name) # most
# #print(emp.__dict__)  # AttributeError no attribute '__dict__'
# #print(vars(emp))      # TypeError: vars() argument must have __dict__ attribute
# del emp.name
#
# # For us: Almost similar usage
# # For python: Different implementation: More memory and time efficient!
# # BUT: you lose flexibility of adding attributes! Trade off

"""With inheritance: Way #1
● In child class, you can normally add attributes in the normal way"""

# class Person:
#     __slots__ = ['name', 'email']
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# #Person('mostafa', 'm@g').__dict__ # Error
#
# class Student(Person):
#     def __init__(self, name, email, gpa):
#         Person.__init__(self, name, email)
#         print(self.__dict__)   # {}
#         self.gpa = gpa
#         # Will use the parents slots + dict by default
#
# st = Student('mostafa', 'm@g', 3.7)
# print(st.__dict__)   # {'gpa': 3.7}

"""With inheritance: Way #2
● We can also extend the child class with its attributes using slot
● But u again is restricted"""

# class Person:
#     __slots__ = ['name', 'email']
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# class Student(Person):
#     __slots__ = ['gpa'] # EXTEND with new attributes
#     def __init__(self, name, email, gpa):
#         Person.__init__(self, name, email)
#         self.gpa = gpa
#
# st = Student('mostafa', 'm@g', 3.7)
# #print(st.__dict__)   # Now error!
#
# # Note: Although we can respecify __slots__ as
# # __slots__ = ['name', 'email', 'gpa']
# # but this hides parent ones! Overall, highly discouraged
# # Note: Probably this will be prevented in the future

"""The best of the 2 worlds
● By adding __dict__, you allow it as an attribute, and hence allows for more flexible entries in it"""

# class Person:
#     __slots__ = ['name', 'email']
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# class Student(Person):
#     __slots__ = ['gpa', '__dict__']
#     def __init__(self, name, email, gpa):
#         Person.__init__(self, name, email)
#         self.gpa = gpa
#
# st = Student('mostafa', 'm@g', 3.7)
# st.temp = '111'
# print(st.__dict__)  # {'temp': '111'}
#
# # By adding __dict__ as slot
# # we can have both slot and dynamic attributes!

"""Finally
● Python 3.3 
Key-Sharing Dictionaries
○ New impl for the standard dict
○ shares the keys between multiple dictionaries and improve memory use
○ Now with thousands objects of same class: we have shared keys
○ Overall: Time & Memory faster
○ Some guys claim that this feature reduce/cancel the need for slots
○ In future if you needed in a critical situation: do timing with/without slots and decide
■ Be careful from implementation changes
● Future readings: 
link link link"""

# Inheritance in Practice

"""Inheritance in practice
● In past = major technique for reusability and extensions
● Now = A lot of careful before using it  (E.g. as in homeworks) 
○ Prefer composition over inheritance
○ Avoid as much as possible inheritance. Use inheritance if you have strong justifications
■ It is really is-a relationship. 
■ Parent class is superclass for all subclasses. 
● Think deeper about future changes
● But future is really hard to predict :(
■ You don’t do it just to do some code reuse"""

"""Multiple Inheritance in practice
● Avoid it. Avoid it. Avoid it unless it is really a good one
○ With minor mistakes: you may end up with e.g. uninitialized base classes or errors for missing 
parameters. It is also a source of confusion.
○ Prepare strong justification for your team
○ Make the inheritance hierarchy a tree style
● One clear issue: if we have arguments from a class to another, then?!!
○ This is a big issue
○ One popular workaround: 
Cooperative Multiple inheritance
■ Core concept: use **kwargs in args + all calls super()
○ If you are using someone multiple inheritance, make sure to understand it / above link
○ Future readings: 
link link link link link """


# Inheritance Homework 1

"""Problem #1: Build Hierarchy
● Design set of classes (no data/functions) to express this classes hierarchy"""

# class Shape:
#     pass
#
# class TwoDimensionalShape(Shape):
#     pass
#
# class Circle(TwoDimensionalShape):
#     pass
#
# class Square(TwoDimensionalShape):
#     pass
#
# class Triangle(TwoDimensionalShape):
#     pass
#
#
# class ThreeDimensionalShape(Shape):
#     pass
#
# class Sphere(ThreeDimensionalShape):
#     pass
#
# class Cube(ThreeDimensionalShape):
#     pass
#
# class Tetrahedron(ThreeDimensionalShape):
#     pass


"""Problem #2: Build Hierarchy
● Design set of classes (no data/functions) to express this classes hierarchy"""


# class CommunityMember:
#     pass
#
# class Student(CommunityMember):
#     pass
#
# class Alumnus(CommunityMember):
#     pass
#
# class Employee(CommunityMember):
#     pass
#
# class Staff(Employee):
#     pass
#
# class Faculty(Employee):
#     pass
#
# class Teacher(Faculty):
#     pass
#
# class Administrator(Faculty):
#     pass
#
# class AdministratorTeacher(Teacher, Administrator):
#     pass

"""Problem #3: Customer Requirement
● While taking to a customer asking to build a web application for their app he 
said: “In our system, customers may pay money with cash, cheque, credit or 
debit card”
● Each order in the system should indicate how money was paid
● Design set of classes that can potentially represents such requirement
○ Mainly classes, no attributes"""

#
# class Payment:
#     pass
#
# class Card(Payment):
#     pass
#
# class CreditCard(Card):
#     pass
#
# class DebitCard(Card):
#     pass
#
# class Cash(Payment):
#     pass
#
# class Cheque(Payment):
#     pass
#
# class Order:
#     def __init__(self, payment: Payment):
#         self.payment = payment
#
# if __name__ == '__main__':
#     Order(DebitCard())

# Inheritance Homework 2

"""Problem #1: Design Review
● A fresh engineer implemented this system to express a car
○ Code wise: car has all functions it needs to provide
○ It passed system tests
● What is wrong? 
● Give a tip"""

# class FourWheels:
#     # Some variables and methods
#     pass
#
# class Engine:
#     # Some variables and methods
#     pass
#
# class Car(Engine, FourWheels):
#     # Some variables and methods
#     pass
#
# """
# The semantic is wrong. There is no clear and strong has-a relationship. Never do that in inheritance
# A car is not an Engine. The car is not 4 wheels.
# Sometimes we can stack things with inheritance and it works for now (and be a big mess later)
# The right relationship is composition. The car has an engine and 4-wheels
# Prefer composition over inheritance most of the time, even if inheritance makes more sense unless it really should be an inheritance. Think twice.
# """
#
# class Car2:
#     def __init__(self):
#         # Car has an engine
#         # Car is composed of 4 wheels
#         self.wheels = FourWheels()
#         self.engine = Engine()
#
#     def something(self):
#         # Use engine and wheels
#         pass


"""Problem #2: Future Prediction!
● A fresh engineer designed a system with initial requirements 3 animals (cat, monkey, whale)
● What does this design imply?
● After a year, a new mammal was added to the system, but turned out this design is wrong
○ Find such a mammal
■ Think & Google
● Note
○ boolean/string is a C++ style design"""

"""- We wanna represent these 3 animals, which are mammals
- There are 3 common functions as in the class
- 2 of them are common behavior
- but the sound is unique for each element

- More importantly, the design means EVERY mammal should have these functionalities
- But Platypus lays eggs and doesn't give birth

- Why the designer made this mistake?
    - Initial requirements were to model these 3 animals.
    - As the 3 functionalities are common, they all were added in the mammal superclass

- Whenever you have a parent class, make sure it is VALID for all possible future sub-classes, not only current ones.
- Your teammates will extend your work in the future!

Optional Reading: https://www.clear.rice.edu/comp201/07-spring/lectures/lec06/"""

"""Problem #3: Irrelevant!
● Imagine we have 4 classes, each with 20 function
● There is a need for a new class that has a 
relationship of “is-a” with the 4 classes to a good 
extent
○ What is the problem we will face?
○ As more motivation, imagine we wanna Create a RobotDog 
from the classes on left
■ It is a robot, so it does what robots does
■ It looks like a dog and do its most of its functionalities
■ But it is not real dog, it is a made one"""


# class Robot:
#     def drive(self):
#         pass
#     def clean(self):
#         pass
#     def do_funny_actions(self):
#         pass
#
# class RealAnimal:
#     def go_toeilt(self):
#         pass
#     def make_sound(self):
#         raise NotImplementedError
#
# class Cat(RealAnimal):
#     def make_sound(self):
#         print('Meow')
#
# class Dog(RealAnimal):
#     def make_sound(self):
#         print("Bark")

"""- If we extended from the 4 classes, we will end up with a lot of functions that are irrelevant to the current class
- Usually, we do mistakes in design and even with a reasonable has-a relationship, a lot of functions just are in our new class that has no use!
- In the example, A robot dog won't go toilet, it is a made dog, not a real one. Sometimes the has-a relationship is not as strong as we wish"""

"""Problem #4: System Design
● In Medal of Honor game, there are millions of online players
○ Sometimes there is some message from the game to the players
● There are 2 ways to deliver the message:
○ Each app periodically contacts the server to see if there are new notifications or not
■ Then Game site provide an API to be contacted through it
■ Each mobile/desktop/tablet send/receive request/response
○ When user opens the application, a registration message is sent to the game
■ Whenever server has a new message, it iterates on whoever registered and send msg
○ Discuss the 2 options. Any notes on their implementations. """

# - Scalability is a critical key to the success of the business. Let's think about it for the following 2 choices
# - Assume we have 10 Million mobile users, say of 15 different types of mobiles
#
# Choice 1: Each app periodically contacts the server to see if there are new notifications or not
# - As mobiles are creating the requests, this means the server is receiving periodically millions of requests
# - 2 critical problems here
# - The server will be very slow to handle "concurrent requests" of such size
# - Most of the time there won't be messages to notify
#
# Choice 2: When a user opens his mobile game, he sends to the Game to register for messages to get notifications
# - The server provides an API for apps to register or de-register
# - When there is a message, the server loops on them and just notify
# - Each device type might need a special code to send notifications


"""Problem #5: A new Startup
● In every country there are banks where people have money and services where they wanna pay money (Mobile & Electricity bills)
● With every new service to pay (e.g. new mobile network), each bank wants to support paying the bills to this new service. 
● To implement that, a team per bank builds something on bank side and something on the service side so that they can communicate
● As an entrepreneur:
○ What are the current issues in this model?
■ E.g. How many software programs are built for N banks and M services?
○ Think in a startup proposal that can offers elegant solution to this problem?
○ How to validate your 
business model? Do most of startups fails or succeed?"""

# The problem:
# - For N banks and M services, we will build N*M software programs. This is Many to Many relationships.
# - With every new service, the banks need to wait a lot till the service provide solutions for the banks
# - With every new bank, it has to search the market for which services are available. Bank has to implement software per service to communicate
# - There will be a lot of time to discuss agreements on commission per transaction
# - Code wise, most of the codes will be implemented with several different teams, and there will be a lot of code duplications 
# The business opportunity:
# - Introduce a company that acts as middle player between banks and services
# - Each bank builds one software ONLY to contact the middle
#     - It asks to get the bills of a specific service to view them to the user
#     - If a customer asked to pay a bill, the bank verifies the balance, and sends it to the middle to mark the bill as paid
# - Each service builds one software ONLY to contact the middle
#     - It provides the bills to the middle and marks them paid if they are paid
# - Middle build N software for banks and M for services
#     - This means we now build 2N + 2M software projects not N*M
#     - N+M by the middle. As one company, a lot of code can be shared
# - If there is a new bank, it only needs to build one software from its side to get access directly to M services
# - This means the system scales very well
#     
#     
# Like any business
# - You don't only depend on your elegant solution if it is elegant even :D
# - Also a lot of effort to validate your business model, and market it


# Inheritance Homework 4

"""Problem #1: More Features
● Background. 
○ When we write some service (e.g. Email service), we might have some standard features
○ 1) Pure service, just normal
○ 2) Logging support: means the service log info/issues to some file
○ 3) Caching support: means some information are in memory for fast processing
○ 4) Thread-Safe support: it means several threads access shared resources in proper way
○ There might be some software guidelines to follow
○ 1) There is only a single reason to change a class, otherwise split the features somehow
■ E.g. you don’t create a single class with logging + caching + thread-safe support
● You have now 4 reasons to do a change to this class!
○ 2) Don’t play with others code. Consider it closed. Reuse/Extend what is available 
Problem #1: More Features
● When you joined an email service company they had code for the following
○ A basic email service that just sends/downloads email once
○ An extension that support multiple trials if there is failure (using inheritance)
○ An extension that support thread safe
○ An extension that support multiple trials if there is failure + thread safe
○ Note that, there are several cases in the system that make use of any of the 4 classes
Problem #1: More Features
● A new module implemented in the code base: 
Logger
● A new feature is requested: Logging feature to the overall Email service
● There is a need to able to use the current 4 classes:
○ Without logging feature (directly use available ones)
○ E.g. someone may need: basic service + retrials (no logging or thread safe)
○ E.g. someone may need: basic service + logging (no retrials or thread safe)
○ E.g. someone may need: basic service + logging + retrials + thread safe
● Draw the new class diagram that supports logging feature
○ Remember, you shouldn’t modify the current classes, but reuse them
Problem #2: More Features
● After a few months, there is a need to also support caching feature
● There is a need to be able to use the current classes (without caching):
○ E.g. with or without logging
● Now classes should support with or without caching
○ E.g. someone may need: basic service + caching + retrials (no logging or thread-safe)
○ E.g. someone may need: basic service + retrials + logging + caching (no thread-safe)
● Design a new UML
○ Use my solution for previous homework and modify it
○ There is a critical concern you should notice at the moment. What is it?"""

# This problem is known as an The Class Explosion Problem
#
# We could easily from the begin build one class and keep changing it so that it has boolean in the constructor for:
#     - is thread-safe? is logging? is caching?
#     
# - But this means we have a huge code with several reasons to change = mess
#
# - When we tried to follow design guidelines = every time we expanded the tree leaves with more classes to support a new feature
#
# - Here is another real case
# 	https://realpython.com/inheritance-composition-python/#the-class-explosion-problem   
# 	https://stackoverflow.com/questions/60540457/class-hierarchies-exploding
#
# - "Large inheritance hierarchies in general, and deep ones in particular, are confusing to understand and therefore difficult to maintain. "
# - "Inheritance is a design-time decision and trades off a lot of runtime flexibility."
#
# - Diagrams source: 			https://dzone.com/articles/is-inheritance-dead



# Inheritance Homework 4

"""Problem #1: IKea’s Items
● Manager said: “In our system, items are either simple or complex. A complex 
item consists of other items. Those items themselves could consist of other 
items, and so on. Items share name, id and price. Then some items might 
have more details like a chair’s color. Notice, a complex item price is actually 
the total price of its inner items. For example, one of our special chairs 
consists of 2 left legs (each for $65) and 1 right leg. This right leg is actually a 
base (for $30) and an extension (for $70). The total price of this special chair 
is 65+65+30+70 = $230”. 
● Implement a simple system that represents this logic
● Create some exceptions that might be useful"""


# it is totally ok to come up with other designs
# Read below and learn

# class IkeaRootException(BaseException):
#     pass
#
# class PriceError(IkeaRootException):
#     pass
#
# class Item:
#     def __init__(self, name, id, price = None):
#         self.name = name
#         self.id = id
#         self._price = price
#         self.parts = []
#
#     def add_part(self, item):
#         if self._price is not None:
#             raise PriceError("Item that has an initial price shouldn't have parts!")
#         self.parts.append(item)
#
#     @property
#     def price(self):
#         if self._price is not None:
#             return self._price
#
#         return sum([item.price for item in self.parts])   # deep price!
#
# class SpecialChair(Item):
#     def __init__(self, name, id, color, price=None):
#         super().__init__(name, id, price)
#         self.color = color
#
#     @staticmethod
#     def builder(color):
#         item1 = Item('Chair left leg', 1234, 65)
#         # item2.add_part(None)    PriceError
#
#         item2 = Item('Chair right leg', 1235)
#         item2.add_part(Item('Main Base', 123451, 30))
#         item2.add_part(Item('Main Extension', 123452, 70))
#
#         item_chair = SpecialChair('Chair', 1236, color)
#         item_chair.add_part(item1)
#         item_chair.add_part(item1)
#         item_chair.add_part(item2)
#
#         return item_chair
#
# # And so on
#
# if __name__ == '__main__':
#     item_chair = SpecialChair.builder('Black')
#     print(item_chair.price)

"""Problem #2: Package Delivery Service
● Design classes (no main) for a package delivery service (E.g. FedEx):
○ A standard package has a sender address, receiver address, weight in kg and price per kg
■ Total cost is: weight in kg x price per kg
■ Address is: name, string and city
○ A 2-day package is similar to standard package with an added fixed fee for the total cost
○ A heavy package is similar to standard package but with extra penalty for packages weight > 100 kg
■ If weight > 100 kg, then extra fees: (weight - 100) *  extra weight price in kg"""


# class Address:
#     def __init__(self, name, street_address, city):
#         super().__init__()
#         self.name = name
#         self.street_address = street_address
#         self.city = city
#
# class StandardPackage:
#     def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg):
#         super().__init__()
#         self.sender_address = sender_address
#         self.reciever_address = reciever_address
#         self.weight_kg = weight_kg
#         self.price_per_kg = price_per_kg
#
#     def total_cost(self):
#         return self.weight_kg * self.price_per_kg
#
# class TwoDayPackage(StandardPackage):
#     def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg, fixed_fee):
#         super().__init__(sender_address, reciever_address, weight_kg, price_per_kg)
#         self.fixed_fee = fixed_fee
#
#     def total_cost(self):
#         return self.fixed_fee + super().total_cost()
#
# class HeavyPackage(StandardPackage):
#     weight_limit = 100
#
#     def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg, extra_price_per_kg):
#         super().__init__(sender_address, reciever_address, weight_kg, price_per_kg)
#         self.extra_price_per_kg = extra_price_per_kg
#
#     def total_cost(self):
#         res  = super().total_cost()
#
#         if self.weight_kg > self.weight_limit:
#             res += (self.weight_kg - self.weight_limit) * self.extra_price_per_kg

"""Problem #3: Our Dictionary
● We would like to extend the built-in dict data structure to force any given key 
that is float to be an integer. For every conversion, print that
○ Please revise the dict lecture. There are several ways to add/change keys
■ Don’t try to cover compound operators like += 
■ Do extensive testing for the possible cases [according to what we learned]"""


# class MyDict(dict):
#     def __setitem__(self, key, value):
#         print(f'Update: {key} - {value}')
#         if type(key) is float:
#             print(f'\tDo Conversion to {key}')
#             key = int(key)
#         super().__setitem__(key, value)
#
#     # https://docs.python.org/3/library/stdtypes.html#dict.update
#     def update(self, dct_or_iterable = None, **kwargs):
#         if dct_or_iterable is not None:
#             kwargs.update(dct_or_iterable)
#
#         for key, value in kwargs.items():
#             self[key] = value
#
#     def update_longer(self, dct_or_iterable = None, **kwargs):
#         if isinstance(dct_or_iterable, dict):
#             iterable = dct_or_iterable.items()
#         else:
#             iterable = dct_or_iterable
#
#         if iterable is not None:
#             for key, value in iterable:
#                 self[key] = value
#
#         for key, value in kwargs.items():
#             self[key] = value
#
#     # https://docs.python.org/3/library/stdtypes.html#dict.setdefault
#     def setdefault(self, key, value = None):
#         if key in self:
#             return self[key]
#
#         self[key] = value
#         return value
#
# dct = MyDict()
# dct[10.5] = 20
# dct[(4, 5)] = 'Mostafa'
# print (10.5 in dct)
# print(dct)
#
# exit(0)
# dct = MyDict.fromkeys([1.5, 2.7])
# dct[10.5] = 20
# dct[(4, 5)] = 'Mostafa'
#
# dct.update({'name': 30, 0.7: [1, 2, 3]})
# dct.update(((7.5, 7),))
# dct.update([[8.5, 8]])
# dct.update(val=35)
# dct.update([(9.5, 9)], hey = 12)
# dct.update()
# print(dct.setdefault(11.3, 'belal'))
# print(dct.setdefault((4, 5), 'Ziad'))
#
# print(dct)
# # {1: None, 2: None, 10: 20, (4, 5): 'Mostafa', 'name': 30, 0: [1, 2, 3], 7: 7, 8: 8, 'val': 35, 'hey': 12, 9: 9, 11: 'belal'}
#
# print(dct[0])   # [1, 2, 3]
#
# #print(dct[9.5])   # KeyError: 9.5

