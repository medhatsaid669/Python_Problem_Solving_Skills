
"""Pyramid of Object Oriented
The pyramid of OO (Object Oriented)
OO Programing Paradigm
● Programing paradigm: Way of
thinking/viewing/structuring for a
software
● OOP is a programing paradigm
○ View: Objects + Functions + Interactions
○ V
ery centralized around object concept
● Procedural programming is another one
○ Bunch of files and functions + linear flow of
instructions
● Other paradigm
○ Declarative, Functional, etc
OO Programing Paradigm: WHY!
● Close correspondence between real-world objects and OOP classes.
● Help in Handling complexity of software products
● Seems one of best ways to deal with
Software Crisis
○ Complex projects ⇒ Over-budget, over-time, buggy, !meet requirements, never delivered
● OOP languages are good to an extent for handling complex projects
● On the other side
○ Some people criticize a lot OOP itself
○ Others criticize the current designs/focus of current OOP relative the old
● Why not procedural?
intentions
○ No owner for data / data integrity issue / Many functions may modify the building block
○ Harder debugging if data is corrupted
OO Concepts
OO Principles
● The most important skills we need in design!
● SOLID Principles
○ Single Responsibility Principle (SRP)
○ Open/Closed Principle (OCP)
○ Liskov Substitution Principle (LSP)
○ Interface Segregation Principle (ISP)
○ Dependency Inversion Principle (DIP)
● DRY (Don’t Repeat Yourself)
● KISS (Keep it simple, Stupid!)
● YAGNI (You ain't gonna need it)
● Several design principles will be embedded implicitly in the homework
Design Patterns
● The best practices for some repetitive design sub-tasks
● Fatal Mistakes: Overstress in study & Overuse in projects
● Skill: Use it in the right situation for the right reasons
● Some patterns are
○ so
important (e.g. Singleton / Factor)
○ others are less faced
● From a domain to another, some patterns are more used
● Several design patterns will be embedded implicitly in the homework
OOA, OOD, OOP
● Let’s say we have customer requirements for a specific product
● OOA is an analysis phase to these requirements
○ Output: analysis models (use cases & object conceptual model - technology independent)
● After software analysis, we design the system (OOD)
○ Considers: hardware and software platform, availability, scalability, budget, etc
○ Designing is a skill. It takes time to build elegant designs
● Then, we implement & test the system, using an OOP language
○ We coding a specific OOP language
● Company Culture + Scale of project + team size ⇒ Decide how the 3 are
applied
○ Small projects: all of that can be done in a unified way by a small team
○ Large projects may have: business analyst, system analyst, architects, tech leads and devs
Misc
● Reading
○ OOD: After course read: Head First Object-Oriented Design and Analysis book
○ More in
future / Also Designing Data-Intensive Applications book
● Coding Style
○ https://github.com/isocpp/CppCoreGuidelines
○ https://google.github.io/styleguide/cppguide.html"""

# Class and Object
"""So far
● So far we learned what is class and object
○ Class: group relevant data and methods in a single unit (e.g. Student/Book/Admin)
○ Object: we instantiate/create many objects from the class blueprint
● We studied built-in classes: int, float, list, str, tuple, dict, set
○ We learned about (im)mutability, in-place changes and memory name-value binding
● We learned how to
○ Create our own class and create several objects
○ Magic/Dunder methods
■ __init__ for constructing a new object
■ __str__ and __repr__ for string representation of an object
○ To create our own attributes
○ To create our own methods and the difference with function
__init__
● A special (dunder/magic) method for assigning the class attributes
● emp = Employee()
● Behind the scene, automatically:
○ Python creates memory for the new object  (like new in C++)
○ Python calls __init__ method if exists
● It should not return anything (or technically None)
○ Otherwise: TypeError
● We can use default arguments, like any function
Naming Conventions
● Class Name  follow camel casing
● Attributes and Methods follow snake casing 
● Class name and attributes are typically nouns
○ UsersManager, total_users
● Methods typically indicates actions (verbs)
○ compute_result, find_user...
Encapsulation
● Encapsulation is the grouping of variables and functions of a specific concept 
in a single component, named class
○ Reduce system complexity 
● In next section, we will highlight more about data-hiding in Python
Real-World as set of interacting objects"""

# Classes Homework 1
"""Problem #1 - Shapes
●  Think in Rectangle, Triangle, Circle in a Drawing application
○ What are common things between them? What is special in each of them?
○ Think in terms of attributes, methods names & behaviour"""

# We have different shapes to draw
# Common:
#     Data: Color
#     Methods: Draw & Compute area, but each one has different behaviour
# Special:
#     Triangle need 3 sides (or points).
#     Rectangle needs 4.
#     Circle needs center and radius
# Soon we will learn about inheritance

"""Problem #2: What vs How
● 1) Task:
○ What: Sum from 1 to N in 2 ways
○ How: Explain 2 approaches to implement above task
● 2) Snapseed is an app for Image Manipulation (e.g. crop, rotate, draw, etc)
○ It is available for Android, IOS, IPAD
○ In terms of what & how: provide some insights
■ E.g. method to fill color in rectangle?
■ E.g. method to read image from device?
○ Imagine we found a bug in some function
■ Or faster way to do it
■ How to structure our app code base 
    to do the minimum code changes?"""

# 1) We can sum from 1 to N in 2 ways
# A) Loop to sum from 1 to N. Easy to code, but slow. E.g. for N = 10^10
# B) Use formula (N * (N+1))/2. Now this is very efficient
# In many cases, the same task can be done in several ways
# - Some are clearly written and some are not
# - Fast or slow
# - Memory hungry or reasonable
# - Heavy computations (your mobile became hot) or more efficient
# - Consume your mobile data package (video call) or save it!
# It is not easy to build efficient software!
# ////////////////////////////////////////////////
# 2) Like most of the provided systems, we know what the service provides us NOT how it works
#  E.g. you use messenger to chat. You care what are the possible things to do
#   You don't care about how it is done or scaled to support 1 Billion user
#   
#  Same logic in your TV & Car. 
# As we provide support for Android, IOS, IPAD, we should be very careful from code duplication (DRY).
# - Most of the system will be actually common code, e.g. fill rectangle color
# - Some functionality will be more system dependency, e.g. loading an image from the storage
# - DRY (Don’t Repeat Yourself)
#  - Whatever common, design the system to reuse it
#  - E.g. Has a library class of handling shapes that is common
#  - A separate one for functions with the same name but different, such as load image
# Soon we will learn about abstraction

"""Problem #3: Datetime review
● Your college designed and 
implemented DateTime Class
○ Jointly supports the Date & Time
● The code passed all unit testings
● Think in a critical design tip
○ Provide your feedback!
● Introduce a better design"""

# class DateTime:
#     def __init__(self, day, month, year,
#                  hours, minutes, second):
#         self.day = day
#         self.month = month
#         self.year = year
#         self.hours = hours
#         self.minutes = minutes
#         self.second = second

    # Many methods about date
    # Many methods about time
"""The problem with above class it is responsible for 2 things
    Date and all its complications
    Time and all its complications

Always focus a class on a specific functionality (single responsibility)
    Then, each class is easier to code
    Easy to give different developers different tasks

This is called single responsibility principle! Better approach"""

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
# class Time:
#     def __init__(self, hours, minutes, second):
#         self.hours = hours
#         self.minutes = minutes
#         self.second = second
#
# class DateTime:
#     def __init__(self, day, month, year,
#                  hours, minutes, second):
#         self.date = Date(day, month, year)
#         self.time = Date(hours, minutes, second)
#         # This is called composition
#         # Datetime class is composed of other 2 objects: date and time
#         # Other example: Car is composed of an enginer


"""Problem #4: Handling Debates
● Assume in a given tasks, your colleges did not agree with your design/code
● Think in tips & thoughts how to handle technical debates"""

# In a debate with a college:
# Be open for different views (e.g, 2 ways for the data members)
# Defend your choices with logical reasons
# Also understand your college choices & reasons
# A lot of areas are just vague. We may not know which direction is definitely the right way
# Minor design concerns are not like big ones. System design is more risky than a class design
# Find someone with more experience to help you make decisions
# Or put time limit: discuss for an hour, then vote.
# Red flag if discussions are very lengthy with a few "action items"


"""Problem #5: Future Features
● A fresh developer approached the team leader with the following suggestion
○ From an informal discussion with a customer, it seems after 6 months we will need:
■ Several printing styles & streams (file, console) for our data
■ Maintaining statistics about every used method
○ He suggests to implement these extensions now to save future time for other features
● As a leader
○ Do you accept? Or Reject? Or Suggest an alternative?
○ Why?"""

# - One of the popular principles is You aren't gonna need it (YAGNI)
# - Always implement things when you actually need them, never when you just foresee that you need them
# - Otherwise, they might be actually useless features and the team just lost resources for nothing
# - Side note: It is good that the design allows extensions, but implement when need
# Reading: https://martinfowler.com/bliki/Yagni.html
# 	artin Fowler is a British software developer, author and international public speaker on software development,
# 	specialising in object-oriented analysis and design, UML, patterns, and agile software development methodologies, including extreme programming

# Name Mangling
# Underscores!
# class Book:
#     def __init__(self):
#         self.att1 = 1
#         self._att2 = 2
#         self._att3_ = 3
#         self.__att4 = 4
#         self.___att5 = 5
#         self.__att6_ = 6
#         self.__att7__ = 7
#         self.____att8_ = 8
#         self.____att9__ = 9
#
# if __name__ == '__main__':
#     book = Book()
#     print(book.att1)            # 1
#     print(book._att2)           # 2
#     print(book._att3_)          # 3
#     #print(book.__att4)         # AttributeError
#     #print(book.___att5)        # AttributeError
#     #print(book.__att6_)        # AttributeError
#     print(book.__att7__)        # 7
#     #print(book.____att8_)      # AttributeError
#     print(book.____att9__)      # 9

# Not that strict!

# class Book:
#     def __init__(self):
#         self.att1 = 1
#         self.__att4 = 4
#         self.___att5 = 5
#         self.__att6_ = 6
#         self.____att8_ = 8
#
# if __name__ == '__main__':
#     book = Book()
#     # __dict__ : contains all the attributes of the object
#     print(book.__dict__)
#     #{'att1': 1, '_Book__att4': 4 , '_Book___att5': 5,
#     #            '_Book__att6_': 6, '_Book____att8_': 8}
#     print(book._Book__att4)     # 4
#     # Observe: in run-time, interpreter changed the attributes names
#     # by prefixing with: _Book

"""Name Mangling
● Prefixing specific attributes with _classname
● If they have 
○ at least 2 leading (before) underscores __
○ and at most 1 trailing (after) _
● Examples, for a book class:
○ __var    ⇒ _book__var
○ __var_  ⇒ _book__var_ 
● So by default, the user can't access them
○ unless the coder wanna really use them ⇒ then use the mangled name
● Same rules for functions!"""
# With functions!

# class Book:
#     def __init__(self):
#         pass
#     def __f1(self):
#         print('__f1')
#     def __f2_(self):
#         print('__f2_')
#     def _f3(self):
#         print('_f3')
#
# book = Book()
# #book.__f1()   # AttributeError
# #book.__f2_()  # AttributeError
# book._f3()     # _f3
#
# print(dir(book))    # return the names in the current scope
# # ['_Book__f1', '_Book__f2_', '__class__', ... , '_f3']

# Visible from inside!

# class Book:
#     def __init__(self):
#         self.__att4 = 4  # _Book__att4
#
#     def hello(self):
#         print(self.__att4)  # visible from INSIDE!
#         print(self._Book__att4)  # visible from inside!
#
# if __name__ == '__main__':
#     book = Book()
#     # print(book.__att4)          # NOT visible from OUTSIDE
#     print(book._Book__att4)  # we still can access indirectly
#     book.hello()

"""Next ● We will know more about Data-hiding and why do mangling?"""

# Data-Hiding
"""Name mangling
● In the last video we learned about this process
● Some attributes/methods are not directly accessible from outside
○ The are meant to be used internally (inside the class)
○ But python doesn’t prevent you from really forcing an access
● So it is kind of data-hiding, but not so strict (weakly-private)
● Useful to avoid name collisions in inheritance hierarchy
● It is educative to introduce another perspective from languages like C++/Java

C++ Class: Private vs Public
● Similar to python, but is divide to 2 parts
● Public section:
○ Outsider can see/access its attributes/methods
● Private section:
○ Outsider can’t access
○ Insiders only can see/access

C++ Data Hiding Concept
● The private section hides some data members & member function from user
○ Users (outside code) are either other classes in same project or client using final project
○ A good design: reveal 
as little as possible of the data members & functions

C++ Data Hiding: WHY?
● To prevent corruption of data by other entities (outside code).
○ Such changes might be 
unintended or intended
● Protect object’s data ⇒ protects object integrity
○ Imagine you have a computer desktop (mobile/car) that has a problem
■ You figured out there is problem in xxx (e.g. adapter of laptop)
■ You bought new cheap yyy similar to xxx but not right model
■ EIther it won’t work or work temporarily then fails soon (e.g. voltage problem)
■ Integrity fails as whole system components are not proper now
● Data hiding also reduces system complexity
● Better code readability (less complex code is viewed).

Back to Python
● Python takes the opposite direction. 
○ By default, we leave things public/accessible. The last resort is to restrict
○ We assume responsibility
○ Is it language limitation as not a compiled language? Or culture?
● Cases:
○ In doubt: leave it public / no mangling
○ Share intention of ‘please don’t touch’? Just use single underscore  (_name) 
○ Some disaster might happen if was abused? Use __
● Python vs C++: which is better approach? Controversial 
● Future reading

Coming from C++/Java
● All programming languages share a lot of things
● But still there are different philosophies/cultures
● Your mind is tuned to C++/java, you need time to do 
● Don’t do things as you used to do in them. 
○ Take a step back. 
○ Think/Search how to make things Pythonic 
mentality shift
● Be open to different philosophies/cultures. Give a series trial.
● Moving later from Python to C++/Java
○ You will write much more code!
○ Different mind set
○ Much more language constructs such in modern C++ (seriesly a complex language)
"""

# Property Class 1

# Our infrastructure class!

# class Person:
#     def __init__(self, full_name):
#         # for simplicity: 2 words space separated
#         # e.g. Mostafa Ibrahim
#         self.full_name = full_name.lower()
#
# # After some time, many teams used our class!
# def f1():
#     person = Person('Mostafa Saad')
#     print(person.full_name)
#     person.full_name = 'Mostafa Ibrahim'
#
# def f2():
#     person = Person('Ziad Mostafa')
#     print(person.full_name)

# Incompatibility
#
# class Person:
#     def __init__(self, full_name):
#         self.first_name, self.last_name = full_name.lower().split()
#
# # After some time, We found it is a wrong design
# # more flexible, we has explicit first name and last name
# # we can use same arguments for init, but the attribute is gone!
#
# # Now all of the hundreds of dependency fail!
# def f1():
#     # AttributeError: No full_name'
#     person = Person('Mostafa Saad')
#     print(person.full_name)
#
# def f2():
#     person = Person('Ziad Mostafa')
#
# if __name__ == '__main__':
#     f1()

"""The property class
● It allows us to provide an attribute to the outsiders, although it doesn’t exist
● 1) Provide a getter method (accessor)
○ A function that return a value of the target attribute
● 2) Provide a setter method (mutator)
○ It takes a value and set it
● 3) Create a property object
○ Give it one or both of these 2 methods 
● Code is better :) """

# Property Class 2

# The property class
# class Person:
#     def __init__(self, full_name):
#         # DRY Principle: DON'T repeat yourself!
#         self.set_full_name(full_name)
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def set_full_name(self, full_name):
#         self.first_name, self.last_name = full_name.lower().split()
#
#     # Create property object
#     # On class level. No self.
#     full_name = property(get_full_name, set_full_name)  # NOT set_full_name()
#
# def f1():
#     person = Person('Mostafa Saad')
#     # Now can see some attribute named full_name
#     print(person.full_name)             # calls get
#     person.full_name = 'Hello world'    # calls set
#     #person.full_name = 'Helloworld'    # not enough values to unpack
#
# def f2():
#     person = Person('Ziad Mostafa')
#     print(person.full_name)
#
#
# if __name__ == '__main__':
#     f1()


#
# class Person:
#     def __init__(self, full_name):
#         # DRY Principle: DON'T repeat yourself!
#         self.set_full_name(full_name)
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     full_name = property(get_full_name)
#
# def f1():
#     person = Person('Mostafa Saad')
#     # Now can see some attribute named full_name
#     print(person.full_name)              # calls get
#     #person.full_name = 'Hello world'    # no attribute 'set_full_name'
#
# def f2():
#     person = Person('Ziad Mostafa')
#     print(person.full_name)
#
#
# if __name__ == '__main__':
#     f1()

# class Person:
#     def __init__(self, full_name):
#         # DRY Principle: DON'T repeat yourself!
#         self.set_full_name(full_name)
#
#     def set_full_name(self, full_name):
#         self.first_name, self.last_name = full_name.lower().split()
#
#     full_name = property(fset=set_full_name)
#
# def f1():
#     person = Person('Mostafa Saad')
#     # Now can see some attribute named full_name
#     #print(person.full_name)             # AttributeError: unreadable attribute
#     person.full_name = 'Hello world'    # calls set
#
# def f2():
#     person = Person('Ziad Mostafa')
#     print(person.full_name)
#
#
# if __name__ == '__main__':
#     f1()

"""Issues in the property class
● You typically have to call the set method from __init__
○ To do some common verifications / changes
○ E.g. if salary, make sure it is > 0
● The outsiders now see 2 ways to change a variable
○ Bad design. There should be one way!
■ We may mangle to reduce the issue
● The elegant and recommended way is Property Decorator
○ We haven't study decorators yet. We will later"""

# Property Decorator

# class Person:
#     def __init__(self, full_name):
#         self.full_name = full_name
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @full_name.setter
#     def full_name(self, value):
#         self.first_name, self.last_name = value.lower().split()
#
# def f1():
#     person = Person('Mostafa Saad')
#     # Now can see some attribute named full_name
#     print(person.full_name)             # calls get
#     person.full_name = 'Hello world'    # calls set
#
# if __name__ == '__main__':
#     f1()

# Set calls itself forever! … Be careful!

# class Person:
#     def __init__(self, salary):
#         self.salary = salary    # calls set
#
#     @property
#     def salary(self):
#         return self.salary
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.salary = value # calls salary.setter again for ever!
#
# def f1():
#     person = Person(100)
#  #   print(person.salary)
#    # person.salary = -200
#    # print(person.salary)
#
# if __name__ == '__main__':
#     f1()

# Get calls itself forever!
#
# class Person:
#     def __init__(self, salary):
#         self.__salary = salary    # calls set
#
#     @property
#     def salary(self):
#         return self.salary   # calls salary.getter again for ever!
#
#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             value = 0
#         self.__salary = value #
#
# def f1():
#     person = Person(100)
#     print(person.salary)
#    # person.salary = -200
#    # print(person.salary)
#
# if __name__ == '__main__':
#     f1()

"""Proper way
● You typically need a different variable name
○ In general, you need to make sure no cycles in calling
● Note: Recursive issue is same with Property class
● Observe: Getter Property with mangled name might also share intentions
○ Get, but don’t set
○ Or provide controlled set/get"""

# class Person:
#     def __init__(self, salary):
#         self.salary = salary    # Fixed
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
# def f1():
#     person = Person(100)
#     print(person.salary)    # 100
#     person.salary = -200
#     print(person.salary)    # 0
#
# if __name__ == '__main__':
#     f1()

"""Background
● The setter/getter methods are fundamental functions in C++/Java
● Why?
○ As these languages hides data as possible in their private section
○ Then users use the set/get to get info about the properties
○ This results in many written methods to just get/set
○ And a lot of debate about setters/getters being evil
● Python
○ By default we make things public
○ Typically no getters/setters
○ Have a good reason? Use Property Decorator, the most pythonic treatment """

# Classes Homework 2

"""Problem #1: Time Class - Code Review
● As a team leader, you are requested to review the previous code
● Figure out all possible concerns in the previous code. E.g.
○ Code Readability?
○ Printing?
○ Can the user create a valid Timers and get unexpected answer?"""


# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours, self.minutes, self.seconds = hours, minutes, seconds
#
#     def get_total_minutes(self):
#         return self.hours * 60 + self.minutes
#
#     def get_total_seconds(self):
#         return self.hours * 60 * 60 + self.minutes * 60 + self.seconds
#
#     def __str__(self):
#         return f'{self.hours}:{self.minutes}:{self.seconds}'
#
# if __name__ == '__main__':
#     time = Time(0, 0, 10 * 60 + 3)
#     print(time)
"""
1- Code Readability: In line 5: it might be better to make line for each.

2- get_total_seconds better call get_total_minutes: e.g. return self.get_total_seconds() * 60 + self.seconds

3- You should provide repr method at least. This covers calls from repr and str. If intend different printings, provide both

4- In str: we better format the output in 2 digits. E.g. 02:03:37 rather than 2:3:37

5- In line 18: what if more seconds are provided? User will expect a handling?

6- The user might provide a negative value, but we may assume some responsibility. The important part our code doesn't crash."""


"""Problem #2: Time Class - Change Request
● All the time we do code changes. 
○ The best code is one that will be changed the minimum or flexible for changes
● Moving to a mobile environment, where memory is limited, we want to move 
to only a single integer only (total_seconds) instead of 3 variables
● However, There are a lot of code base that depends on our code
○ We need to provide combitable changes
■ Old construction should be working: e.g. Time(5, 12, 37)
■ Old attributes should (virtually) be accessible
○ Consider also my solution guidelines for the last Question"""

# class Time:
#     def __init__(self, hours_or_total_seconds, minutes = None, seconds = None):
#         # We can utilize None to figure out which constructor style!
#
#         if minutes is None:
#             self.total_seconds = max(0, hours_or_total_seconds)
#         else:
#             self.total_seconds = 0  # Still outsiders can put -ve value. We can make it property
#             self.seconds = seconds  # observe: same name but no cycles, as they depends on total_seconds
#             self.minutes = minutes
#             self.hours = hours_or_total_seconds
#
#     def get_total_minutes(self):
#         return self.minutes
#
#     def get_total_seconds(self):
#         return self.total_seconds
#
#     @property
#     def seconds(self):
#         return self.total_seconds % 60
#
#     @property
#     def minutes(self):
#         return (self.total_seconds % (60 * 60)) // 60
#
#     @property
#     def hours(self):
#         return self.total_seconds // (60 * 60)
#
#     @seconds.setter
#     def seconds(self, seconds):
#         seconds = max(seconds, 0)
#         self.total_seconds += seconds - self.seconds
#
#     @minutes.setter
#     def minutes(self, minutes):
#         minutes = max(minutes, 0)
#         self.total_seconds += (minutes - self.minutes ) *60
#
#     @hours.setter
#     def hours(self, hours):
#         hours = max(hours, 0)
#         self.total_seconds += (hours - self.hours) * 60 * 60
#
#     def __str__(self):
#         return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'
#
#     def __repr__(self):
#         return f'Time({self.total_seconds})'
#
# if __name__ == '__main__':
#     time = Time(2, 5, 10 + 7 * 60)
#
#     print(str(time))
#     print(repr(time))
#
#     print(time.get_total_minutes())
#     print(time.get_total_seconds())

# Static Variables

"""Static Variables
● What if we need a shared variable among all objects?
● So defined once and used by all? 
● This is called static attribute
○ Created on class level and aren't instantiated. 
○ With any change ⇒ all objects see the effect"""

# Creating static variables

# class Employee:
#     total_employees = 0     # static var: shared
#
#     def __init__(self, name):
#         self.name = name
#         Employee.total_employees += 1
#
# if __name__ == '__main__':
#     emp1 = Employee('Mostafa')
#     emp2 = Employee('Belal')
#     emp3 = Employee('Ziad')
#
#     print(emp1.total_employees)         # 3: instance can access static
#     print(Employee.total_employees)     # 3

"""Confusion is coming!
● Static variables are nice as long as you used them carefully
● As long as you use the Class to access/modify the static  var ⇒ Perfect
● Once you use the object to modify the static var issues may occur
○ We need to understand instance namespace vs class namespace
○ We need to take into consideration: mutable vs immutable objects
● Similar issue if you have an attribute with same name as static var!
● Before next session
○ Practice what we learned
○ Take a few minutes min to guess the behaviour of the next 2 slides
■ No need to play with code or Google"""

# Mixing the usage

# class Employee:
#     total_employees = 0
#     def __init__(self, name):
#         self.name = name
#         Employee.total_employees += 1
#
# if __name__ == '__main__':
#     emp1 = Employee('Mostafa')
#     emp2 = Employee('Belal')
#
#     emp1.total_employees = 10           # Re-bind  : this is now your own attribute! Be careful
#     print(emp1.total_employees)         # 10: refers to its attribute
#     print(emp2.total_employees)         # 3: shared static
#     print(Employee.total_employees)     # 3

# Deleting attributes and vars

# class Employee:
#     total_employees = 0
#     def __init__(self, name):
#         self.name = name
#         Employee.total_employees += 1
#
# if __name__ == '__main__':
#     emp1 = Employee('Mostafa')
#     emp2 = Employee('Belal')
#
#     emp1.total_employees = 10           # Re-bind
#     print(emp1.total_employees)         # 10: refers to its attribute
#     del emp1.total_employees
#     print(emp1.total_employees)         # 3 now: I see shared static
#
#     # del emp1.total_employees           # AttributeError
#     del Employee.total_employees
#
#     # print(emp1.total_employees)         # AttributeError
#     # print(emp2.total_employees)         # AttributeError
#     # print(Employee.total_employees)     # AttributeError

# Class vs Instance namespace

"""Last session: Confusion is coming!
● Static variables are nice as long as you used them carefully
● As long as you use the Class to access/modify the static  var ⇒ Perfect
● Once you use the object to modify the static var issues may occur
○ We need to understand instance namespace vs class namespace
○ We need to take into consideration: mutable vs immutable objects
● Similar issue if you have an attribute with same name as static var!
● Before next session
○ Practice what we learned
○ Take 5-10 min to guess the behaviour of the next 2 slides
■ No need to play with code or Google"""

"""Namespace
● A namespace is a mapping from names to objects
○ No relation between names in different namespaces
○ Typically implemented using dictionary
● When we define a class blueprint ⇒ we have a class namespace for it
● When we create object1 ⇒ we have an instance (1) namespace
● When we create object2 ⇒ we have an instance (2) namespace
● 3 namespaces with maybe common names, but no relations"""

# Class vs Instance namespace

# class Employee:
#     """Class Employee is TODO"""
#     total_employees = 0
#     def __init__(self, name):
#
#         self.name = name
#         Employee.total_employees += 1
#
#     def print(self):
#         pass
#
#     @classmethod
#     def our_f(cls):
#         pass
#
# if __name__ == '__main__':
#     obj = Employee('Mostafa')
#     print(obj.__dict__)
#     # {'name': 'Mostafa'}
#
#     print(Employee.__dict__)
#     # '__doc__': 'Class Employee is TODO',
#     # 'total_employees': 1,
#     # '__init__': <function Employee.__init__>,
#     # 'print': <function Employee.print>,
#     # 'our_f': <classmethod object>

# Deleting attributes and vars

# class Employee:
#     total_employees = 0
#     def __init__(self, name):
#         self.name = name
#         Employee.total_employees += 1
#
# if __name__ == '__main__':
#     emp1 = Employee('Mostafa')
#     emp2 = Employee('Belal')
#
#     emp1.total_employees = 10           # Re-bind
#     print(emp1.total_employees)         # 10: refers to its attribute
#     del emp1.total_employees
#     print(emp1.total_employees)         # 3 now: I see shared static
#
#     # del emp1.total_employees           # AttributeError
#     del Employee.total_employees
#
#     # print(emp1.total_employees)         # AttributeError
#     # print(emp2.total_employees)         # AttributeError
#     # print(Employee.total_employees)     # AttributeError

# Mutable static var

# class Employee:
#     lst = [2, 5]    # mutable
#     def __init__(self, name):
#         self.name = name
#
# if __name__ == '__main__':
#     obj1 = Employee('obj1')
#     obj2 = Employee('obj2')
#
#     print(Employee.lst) # [2, 5]
#     print(obj1.lst)     # [2, 5]
#     print(obj2.lst)     # [2, 5]
#
#     obj1.lst = [10, 20]
#     print(Employee.lst)  # [2, 5]
#     print(obj1.lst)      # [10, 20]
#     print(obj2.lst)      # [2, 5]
#
#     obj2.lst += [3]
#     print(Employee.lst)  # [2, 5, 3]
#     print(obj1.lst)      # 10, 20]
#     print(obj2.lst)      # [2, 5, 3]

"""When to use class attributes (static vars)?
● Constants
● Defining default values
● Tracking (e.g. you want to keep list of all employees names)
● Statistics (total object creations, total number of function calls, etc)
● Tips
○ Access/modify the class attributes using the Class name
○ Don’t use instance attributes same as class attributes
○ Avoid mutable data for class attributes, or be so careful
● About __dict__ is a dictionary: key/value
○ You may add/remove attributes to it, and this will affect the actual object"""

# Class and Static Methods

"""Static Methods
● So far we used Instance Methods
○ def something (self). 
■ Self is an instance of object. We can access/change the attributes
● Static methods are defined at the class level not the object
○ They don’t get self object ⇒ they can’t change object attributes
○ You shouldn’t use to alter class static variables
● Best usage: as a 
utility that neither depend on the object or the class
○ filter_duplicates(lst)
○ is_even(n)
○ get_position_neigbours(x, y, cnt)"""

# Static Methods

# class Person:
#     def __init__(self, name):
#         self.first, self.last = Person.process(name)
#     def __repr__(self):
#         return f'Person first name: {self.first}  -  last name: {self.last}'
#
#     @staticmethod
#     def process(name):  # No self - no interaction with class/objects
#         """Convert to lower, get first word as first name, remaining as last"""
#         first, *last = name.lower().split()
#         last = ' '.join(last)
#         return first, last
#
# if __name__ == '__main__':
#     print(Person('Mostafa Saad Ibrahim Mohamed'))
#     # Person first name: mostafa  -  last name: saad ibrahim mohamed

"""Class Methods
● Class methods are at the class level not the object
○ They don’t get self object ⇒ they can’t change object attributes
○ They get an object of the class type
■ They may access/modify the class attributes
● Best usage: 
○ A factory method to generate objects from the class
■ This is a popular simple design pattern to create objects
○ A shared method among objects to manipulate attributes"""

# Class Methods

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first, self.last = first_name, last_name
#
#     def __repr__(self):
#         return f'Person first name: {self.first}  -  last name: {self.last}'
#
#     @classmethod
#     def get_person_from_full_name(cls, full_name):
#         first, last = cls.process(full_name)
#         return cls(first, last)
#
#     @staticmethod
#     def process(name):  # No self - no interaction with class/objects
#         """Convert to lower, get first word as first name, remaining as last"""
#         first, *last = name.lower().split()
#         last = ' '.join(last)
#         return first, last
#
# if __name__ == '__main__':
#     per = Person.get_person_from_full_name('Mostafa Saad Ibrahim Mohamed')
#     print(per)
#     # Person first name: mostafa  -  last name: saad ibrahim mohamed

"""Class Methods
● A few remarkable things about it
○ The method depends on passed argument cls for the class itself
■ If the class name changed, the method won’t :)
■ DRY principle
○ Soon, we learn about inheritance
■ If you implemented the method at the parent the level, it is visible for the child too!
■ Static method doesn’t have this great feature. It only can use Person.somestatic"""

# For educational purpose
# ● Similar to the property class, we can create without the decorator

# class Person:
#     def __init__(self, name):
#         self.first, self.last = Person.process(name)
#     def __repr__(self):
#         return f'Person first name: {self.first}  -  last name: {self.last}'
#
#     def myprocess(name):
#         first, *last = name.lower().split()
#         last = ' '.join(last)
#         return first, last
#
# if __name__ == '__main__':
#     # staticmethod: Convert a function to be a static method.
#     Person.process = staticmethod(Person.myprocess)
#
#     print(Person('Mostafa Saad Ibrahim Mohamed'))
#     # Person first name: mostafa  -  last name: saad ibrahim mohamed

# Nested Classes

"""Nested Classes
● Nested if
● Nested loops
● Nested functions
● Nested classes (Aka inner classes)!
○ Mainly a class inside a class (inside a class inside a class)
○ But why?
■ For example, to weakly hide a class from outsiders
■ But, Python culture is not to hide
● That is why rarely used
■ Or maybe group 2 very relevant things togther"""

# Inner

# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.engine = self.Engine(model)
#     def __repr__(self):
#         return f'Name: {self.name} - {self.engine}'
#
#     class Engine:
#         def __init__(self, model):
#             self.model = model
#         def __repr__(self):
#             return f'{self.__class__.__name__} Model: {self.model}'
#             #return f'{type(self).__name__} Model: {self.model}'
#
# if __name__ == '__main__':
#     car = Car('bmw', 'LD1102334')
#     print(car)      # Name: bmw - Engine Model: LD1102334
#
#     engine = Car.Engine('NEWXX')
#     print(engine)   # Engine Model: NEWXX
#
#     setattr(engine, 'release_year', 2021)
#     print(engine.release_year)  # also there is getattr

# Len special method

# Iterating using len and getitem

# class EmployeesManager:
#     def __init__(self):
#         self.employees_names = []
#
#     def add_employee(self, name):
#         self.employees_names.append(name)
#
#     def __len__(self):
#         return len(self.employees_names)
#
#     def __getitem__(self, idx):
#         return self.employees_names[idx]
#
# if __name__ == '__main__':
#     mgr = EmployeesManager()
#     mgr.add_employee('Mostafa')
#     mgr.add_employee('Belal')
#     mgr.add_employee('Ziad')
#
#
#     for name in mgr:    # recall our get next / has next?
#         print(name, end=' ')    # Mostafa Belal Ziad
#
#     print(list(zip(mgr, mgr)))

# Del Special Method

# Dunder Del

# class Employee:
#     def __init__(self, name):
#         self.name = name
#         print(f'Init {self.name}')
#         self.employees_names = []
#
#     def __del__(self):
#         # is called on object when
#         # garbage collector destroys it
#         print(f'Deleting {self.name}')
#         # Don't provide unless very strong reasons
#
#
# if __name__ == '__main__':
#     m = Employee('Mostafa')
#     b = Employee('Belal')
#     z = Employee('Ziad')

"""Memory leak
● In languages like C++, you can create the memory by yourself
○ Then you must free also by yourself
○ If you forgot, they will be there as long as the program is running
○ We call this memory leak: neither used or released
○ If your program allocated a lot of it, the machine memory will be consumed ⇒ Machine hangs
● In python, garbage collector handles the memory for us
○ E.g. using Reference counting, as we learned before
● Most of the cases, your python code is good in terms of memory
○ If you are calling some other language (e.g. C++), there could be memory leak in it
○ In python: be careful from creating dictionary/lists that hold many references without clearing
■ GC won’t clear, as there is a reference"""

"""Cyclic References
● Python's standard reference counting mechanism cannot free cycles
○ Supplemental garbage collection facility does (maybe to some extent)
○ Future reading: weakref
● Future readings: 
● In some special scenarios, we may disable GC link link link"""


# class A:
#    def __init__(self, b):
#        self.b = b
#
#    def __del__(self):
#        print('deleting A')
#
# class B:
#    def __init__(self, a):
#        self.a = a
#
#    def __del__(self):
#        print('deleting B')
#
# a = A(None)
# b = B(a)
# a.b = b
#
# import sys
# print(sys.getrefcount(a)-1)     # 2
# print(sys.getrefcount(b)-1)     # 2
# # deleting A deleting B

# Classes Homework 3


# Answer
# class StudentGradesInfo:
#
#     """
#     It seems developer wants to keep track of how many times this function is called
#     Proper way to maintain a static counter inside the class
#     Side note: in real life, we applications keep track of what users do and analyze it
#     This allows discovering what users do/don't so that we improve their experience
#     """
#     statistics_total_prints = 0
#     MAX_COURSE_GRADE = 100
#
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     """
#     Several mistakes:
#     - It uses a magic number: numeric literal (for example, 8080 , 2048 ) that is used in the middle of a block of code without explanation
#         - Define a const MAXS_COURSE_GRADE on class level
#             - Imagine what happens of 100 changed? In old code, you make a lot of changes
#     - This method has nothing to do with the object attributes
#         - As it needs the course grade, we can make it class method
#
#     - Bug in first if condition: it should return 0
#     """
#
#     @classmethod
#     def adjust_grade(cls, grade):
#         if grade < 0:
#             return 0
#         if grade > cls.MAX_COURSE_GRADE:
#             return cls.MAX_COURSE_GRADE
#         return grade
#
#     def add_grade(self, grade, course_name):
#         """
#         This function adds a new course IFF the course is not already added
#         If added, course old value is not overwritten!
#         """
#         # Docs should be AFTER not before the method/class
#
#         if course_name in self.courses_names:
#             return False
#
#         # Critical bugL append the grades before the condition!
#         self.grades.append(self.adjust_grade(grade))
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         self.__class__.statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         # Don't use magic number. Don't use class name explicitly (avoid future code changes)
#         return (sum(self.grades), self.__class__.MAX_COURSE_GRADE * len(self.grades))
#
#
# if __name__ == '__main__':
#     student = StudentGradesInfo('ID1234')
#
#     student.add_grade(70, "Math")
#     student.add_grade(70, "programming 1")
#     student.add_grade(85, "programming 2")
#
#     student.print()



"""Problem #1: Students Grades - Code Review
● Requirements:
● Class for a student and his grades per course
● Add grade Don’t update if exists
● Grade max is 100 e.g. 76.5/100
● Printing functionality Track # of calls"""

# statistics_total_prints = 0
#
# class StudentGradesInfo:
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     def adjust_grade(self, grade):
#         if grade < 0:
#             return grade
#         if grade > 100:
#             return 100
#         return grade
#
#     """
#     This function adds a new course IFF the course
#     is not already added
#     If added, course old value is not overwritten!
#     """
#     def add_grade(self, grade, course_name):
#         self.grades.append(self.adjust_grade(grade))
#
#         if course_name in self.courses_names:
#             return False
#
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         global statistics_total_prints
#         statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         return (sum(self.grades), 100 * len(self.grades))
#
# if __name__ == '__main__':
#     student = StudentGradesInfo('ID1234')
#
#     student.add_grade(70, "Math")
#     student.add_grade(70, "programming 1")
#     student.add_grade(85, "programming 2")
#
#     student.print()
#     print(student.get_total_grades_sum())


"""Software Testing: Background
● “Software testing proves the existence of bugs not their absence.” – Anonymous
● “If you don’t like unit testing your product, most likely your customers won’t like to test it either.” –  Anonymous
● Blackbox testing: we test the public functionality of a class Focus on what not how No care of internals
● Whitebox testing: we care about really what happens internally inside our methods.
● Let’s do some testing :) """

"""Problem #2: Students Grades - Testing
● Develop a class that test our previous class
○ Try the old code
○ Then the fixed code
● You may go beyond these tests
○ For print: feel free to only sketch the approach and don’t implement"""

# statistics_total_prints = 0
#
# class StudentGradesInfo_OLD:
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     def adjust_grade(self, grade):
#         if grade < 0:
#             return grade
#         if grade > 100:
#             return 100
#         return grade
#
#     """ This function adds a new course IFF the course
#     is not already added
#     If added, course old value is not overwritten!"""
#
#     def add_grade(self, grade, course_name):
#         self.grades.append(self.adjust_grade(grade))
#
#         if course_name in self.courses_names:
#             return False
#
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         global statistics_total_prints
#         statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         return (sum(self.grades), 100 * len(self.grades))
#
#
# class StudentGradesInfo_FIXED:
#
#     """It seems developer wants to keep track of how many times this function is called
#     Proper way to maintain a static counter inside the class
#     Side note: in real life, we applications keep track of what users do and analyze it
#     This allows discovering what users do/don't so that we improve their experience"""
#
#     statistics_total_prints = 0
#     MAX_COURSE_GRADE = 100
#
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     """     Several mistakes:
#     - It uses a magic number: numeric literal (for example, 8080 , 2048 ) that is used in the middle of a block of code without explanation
#         - Define a const MAX_COURSE_GRADE on class level
#             - Imagine what happens of 100 changed? In old code, you make a lot of changes
#     - This method has nothing to do with the object attributes
#         - As it needs the course grade, we can make it class method
#     - Bug in first if condition: it should return 0"""
#
#     @classmethod
#     def adjust_grade(cls, grade):
#         if grade < 0:
#             return 0
#         if grade > cls.MAX_COURSE_GRADE:
#             return cls.MAX_COURSE_GRADE
#         return grade
#
#     def add_grade(self, grade, course_name):
#         """
#         This function adds a new course IFF the course is not already added
#         If added, course old value is not overwritten!
#         """
#         # Docs should be AFTER not before the method/class
#
#         if course_name in self.courses_names:
#             return False
#
#         # Critical bugL append the grades before the condition!
#         self.grades.append(self.adjust_grade(grade))
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         self.__class__.statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         # Don't use magic number. Don't use class name explicitly (avoid future code changes)
#         return (sum(self.grades), self.__class__.MAX_COURSE_GRADE * len(self.grades))
#
# # switch between old and new to test
# # StudentGradesInfo = StudentGradesInfo_OLD
# StudentGradesInfo = StudentGradesInfo_FIXED
#
# class StudentGradesInfoTester:
#
#     @classmethod
#     def test_total_courses_cnt(cls):
#         student = StudentGradesInfo('ID1234')
#
#         assert len(student.grades) == len(student.courses_names) == 0
#
#         student.add_grade(70, "Math")
#         assert len(student.grades) == len(student.courses_names) == 1
#         student.add_grade(70, "programming 1")
#         assert len(student.grades) == len(student.courses_names) == 2
#         student.add_grade(85, "programming 2")
#         assert len(student.grades) == len(student.courses_names) == 3
#         student.add_grade(10, "programming 2")
#         student.add_grade(20, "programming 2")
#         student.add_grade(30, "programming 2")
#         assert len(student.grades) == len(student.courses_names) == 3
#
#     @classmethod
#     def test_grades_sum(cls):
#         student = StudentGradesInfo('ID1234')
#
#         assert student.get_total_grades_sum() == (0, 0)
#
#         f = 100
#         input = [(5, "Math"), (-2, "programming 1"), (3, "programming 2"), (4, "programming 2")]
#         output = [(5, 1 * f), (5, 2 * f), (8, 3 * f), (8, 3 * f)]
#
#         for idx, args in enumerate(input):
#             student.add_grade(*args)
#             assert student.get_total_grades_sum() == output[idx], idx
#
#     @classmethod
#     def test_printing(cls):
#         """
#         This function is writing to console! How to test?
#         1) redirect print output to a text file: https://www.kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python#:~:text=Use%20sys.,or%20more%20times%2C%20use%20file.
#         2) read file content
#         3) compare to what you expect!
#         """
#         pass
#
#     @classmethod
#     def test_all(cls):
#         calls = [cls.test_grades_sum, cls.test_grades_sum]
#
#         for call in calls:
#             call()
#
# if __name__ == '__main__':
#     StudentGradesInfoTester.test_all()
#
# """Problem #3: Students Grades - Code Extension
# ● We would like to support iterations functionality, which is more practical than
# the limited print functions
# ○ Force a print / Print only to a console / Print all content! .. Bad design!
# ● For some reasons, we can’t change the code
# ○ Another idea is to extend its functionality!
# ● Your team lead asked to develop a class that satisfy the following main
# ○ Mainly a new class that works on an object from StudentGradesInfo
# ○ The new class allows us to iterate over an info object
# ○ See screenshoot"""

# class StudentGradesInfo:
#
#     """
#     It seems developer wants to keep track of how many times this function is called
#     Proper way to maintain a static counter inside the class
#     Side note: in real life, we applications keep track of what users do and analyze it
#     This allows discovering what users do/don't so that we improve their experience
#     """
#     statistics_total_prints = 0
#     MAX_COURSE_GRADE = 100
#
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     """ Several mistakes:
#     - It uses a magic number: numeric literal (for example, 8080 , 2048 ) that is used in the middle of a block of code without explanation
#         - Define a const MAXS_COURSE_GRADE on class level
#             - Imagine what happens of 100 changed? In old code, you make a lot of changes
#     - This method has nothing to do with the object attributes
#         - As it needs the course grade, we can make it class method
#     - Bug in first if condition: it should return 0"""
#
#     @classmethod
#     def adjust_grade(cls, grade):
#         if grade < 0:
#             return 0
#         if grade > cls.MAX_COURSE_GRADE:
#             return cls.MAX_COURSE_GRADE
#         return grade
#
#     def add_grade(self, grade, course_name):
#         """
#         This function adds a new course IFF the course is not already added
#         If added, course old value is not overwritten!
#         """
#         # Docs should be AFTER not before the method/class
#
#         if course_name in self.courses_names:
#             return False
#
#         # Critical bugL append the grades before the condition!
#         self.grades.append(self.adjust_grade(grade))
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         self.__class__.statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         # Don't use magic number. Don't use class name explicitly (avoid future code changes)
#         return (sum(self.grades), self.__class__.MAX_COURSE_GRADE * len(self.grades))
#
# class StudentGradesInfoIterator:
#     def __init__(self, student_info):
#         self.student_info = student_info
#
#     def __len__(self):
#         return len(self.student_info.grades)
#
#     def __getitem__(self, idx):
#         return (self.student_info.grades[idx], self.student_info.courses_names[idx])
#
# if __name__ == '__main__':
#     student = StudentGradesInfo('ID1234')
#     myiter = StudentGradesInfoIterator(student)
#
#     student.add_grade(70, "Math")
#     student.add_grade(70, "programming 1")
#     student.add_grade(85, "programming 2")
#
#     for grade, course in myiter:
#         print(f'Course: {course} - Grade: {grade}')


"""Problem #4: Students Grades - Wrapper
● StudentGradesInfo is from an open source library. Good to save time
○ Your team lead is afraid from hidden bugs or maintenance stop
○ What if we have 20 classes that use it and then we decided to replace or write our own!
■ Any change in this StudentGradesInfo => change in all of them!
● Your team lead suggested building a wrapper
○ The idea is create another class StudentGradesInfoWrapper
■ It provides the same functionality as StudentGradesInfo
■ It is based on a StudentGradesInfo object
○ With every call to StudentGradesInfoWrapper, just call same method in ur local object
○ Now all your code depends on the wrapper not on the open source code that may change
○ Provide also iteration cabailities """

# class StudentGradesInfo:
#     """
#     It seems developer wants to keep track of how many times this function is called
#     Proper way to maintain a static counter inside the class
#     Side note: in real life, we applications keep track of what users do and analyze it
#     This allows discovering what users do/don't so that we improve their experience
#     """
#     statistics_total_prints = 0
#     MAX_COURSE_GRADE = 100
#
#     def __init__(self, id):
#         self.id = id
#         self.grades = []
#         self.courses_names = []
#
#     """
#     Several mistakes:
#     - It uses a magic number: numeric literal (for example, 8080 , 2048 ) that is used in the middle of a block of code without explanation
#         - Define a const MAXS_COURSE_GRADE on class level
#             - Imagine what happens of 100 changed? In old code, you make a lot of changes
#     - This method has nothing to do with the object attributes
#         - As it needs the course grade, we can make it class method
#     - Bug in first if condition: it should return 0
#     """
#
#     @classmethod
#     def adjust_grade(cls, grade):
#         if grade < 0:
#             return 0
#         if grade > cls.MAX_COURSE_GRADE:
#             return cls.MAX_COURSE_GRADE
#         return grade
#
#     def add_grade(self, grade, course_name):
#         """
#         This function adds a new course IFF the course is not already added
#         If added, course old value is not overwritten!
#         """
#         # Docs should be AFTER not before the method/class
#
#         if course_name in self.courses_names:
#             return False
#
#         # Critical bugL append the grades before the condition!
#         self.grades.append(self.adjust_grade(grade))
#         self.courses_names.append(course_name)
#         return True
#
#     def print(self):
#         self.__class__.statistics_total_prints += 1
#
#         print(f'Grades info for Student ID {self.id}')
#         for idx in range(len(self.grades)):
#             print(f'Course: {self.courses_names[idx]} - Grade: {self.grades[idx]}')
#
#     def get_total_grades_sum(self):
#         # Don't use magic number. Don't use class name explicitly (avoid future code changes)
#         return (sum(self.grades), self.__class__.MAX_COURSE_GRADE * len(self.grades))
#
# class StudentGradesInfoWrapper:
#     def __init__(self, id):
#         self.student_info = StudentGradesInfo(id)
#
#     def add_grade(self, grade, course_name):
#         self.student_info.add_grade(grade, course_name)
#
#     def print(self):
#         self.student_info.print()
#
#     def get_total_grades_sum(self):
#         return self.student_info.get_total_grades_sum()
#
#     def __len__(self):
#         return len(self.student_info.grades)
#
#     def __getitem__(self, idx):
#         return (self.student_info.grades[idx], self.student_info.courses_names[idx])
#
# def f_our_many_functions():
#     StudentGradesInfoWrapper('')
#
# if __name__ == '__main__':
#     student = StudentGradesInfoWrapper('ID1234')
#
#     student.add_grade(70, "Math")
#     student.add_grade(70, "programming 1")
#     student.add_grade(85, "programming 2")
#
#     for grade, course in student:
#         print(f'Course: {course} - Grade: {grade}')
#
#     print(student.get_total_grades_sum())


# Classes Homework 4

"""Problem #3: AutoTrader Class - Code Review
● The following code is working properly in production
● Find all design issues and fix them! """

# Question 1.

# class CarSpecs:
#     def __init__(self):
#         self.trim = None
#         self.engine_type = None
#         self.horsepower = None
#         self.steering_ratio = None
#         # Expected more to be added in future
#
# class AutoTrader:
#     def __init__(self):
#         self.db_cars_specs = []
#
#     def load_database(self):
#         car1 = CarSpecs()
#         car1.engine_type = 'EG12121'
#         car1.horsepower = 10
#         self.db_cars_specs.append(car1)
#
#         car2 = CarSpecs()
#         car2.engine_type = 'EG12121'
#         car2.horsepower = 12
#         self.db_cars_specs.append(car2)
#         # Load More
#
#     def get_matches(self, car_specs):
#         found = []
#         for db_car in self.db_cars_specs:
#             if car_specs.trim is not None and car_specs.trim != db_car.trim:
#                 continue
#             if car_specs.engine_type is not None and car_specs.engine_type != db_car.engine_type:
#                 continue
#             if car_specs.horsepower is not None and car_specs.horsepower != db_car.horsepower:
#                 continue
#             if car_specs.steering_ratio is not None and car_specs.steering_ratio != db_car.steering_ratio:
#                 continue
#             found.append(db_car)
#
#         return found
#
#
# if __name__ == '__main__':
#     trader = AutoTrader()
#     trader.load_database()
#
#     query = CarSpecs()
#     query.engine_type = 'EG12121'
#
#     ans = trader.get_matches(query)
#     print(len(ans))     # 2
#
#     query.horsepower = 10
#     ans = trader.get_matches(query)
#     print(len(ans))     # 1

# Answer 1

# class CarSpecs:
#     def __init__(self, **kwargs):
#         # Now the init is both useful and more generic
#         self.__dict__.update(kwargs)
#         # Reading: https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python
#
#     # It was bad to force other classes to keep get/compare the class field
#     # “Don’t ask for the information you need to do the work; ask the object that has the information to do the work for you.” Allen Holub
#     # is_match is better encapsulation
#     # from Future code changes perspective: with more attributes, outsiders has minimum to zero changes
#     def is_match(self, query_car):
#         # iterate on the available query attributes and compare over them
#         for key, value in query_car.__dict__.items():
#             if self.__dict__[key] != value:
#                 return False
#         return True
#
#
# class AutoTrader:
#     def __init__(self):
#         self.db_cars_specs = []
#
#     def load_database(self):
#         self.db_cars_specs.append(CarSpecs(engine_type='EG12121', horsepower=10))
#         self.db_cars_specs.append(CarSpecs(engine_type='EG12121', horsepower=12))
#         self.db_cars_specs.append(CarSpecs(horsepower=15))
#         # Load More
#
#     def get_matches(self, query_car_specs):
#         # short, elegant and doesn't depend on # of features
#         return [db_car for db_car in self.db_cars_specs if db_car.is_match(query_car_specs)]
#
# if __name__ == '__main__':
#     trader = AutoTrader()
#     trader.load_database()
#
#     ans = trader.get_matches(CarSpecs(engine_type = 'EG12121'))
#     print(len(ans))     # 2
#
#     ans = trader.get_matches(CarSpecs(engine_type='EG12121', horsepower = 10))
#     print(len(ans))     # 1

# Question 2.
#
# class ConfigurationManger:
#     def __init__(self, configuration_path):
#         self.configuration_path = configuration_path
#         # Other attributes
#         self._load()
#
#     def _load(self):
#         # takes 30 minutes to load data
#         print('Loading the Configuration')
#         self.servers_ips = ["10.20.30.40",
#                             "10.20.30.41", "10.20.30.42"]
#         self.aws_service_url = "amazon-aws.com"
#         # load heavy data
#         import time
#         time.sleep(1)
#
# def f1():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# def f2():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# def f3():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# if __name__ == '__main__':
#     f1()
#     f1()
#     f1()
#     f2()
#     f3()

# Answer 2.
"""
Our goal is the load happens only once: All objects see the same loaded data?
This should trigger static variables.

Let's formulate the problem in another way
Can we have only a single instance loading the data, and every new object is just using the old instance?
This is solved using the singleton design pattern! It is a very common problem.

It is hard to provide both simple and elegant solutions.

Below is one ok way to do that(mainly easy to understand)

We rename our old class and make it an inner class inside another one
The outer class will have a static instance from the inner class
With every request to init, we create only the inner object in the first call
I used @property to delegate calls for attributes
If there are methods, we can call the corresponding ones in the inner class

This should trigger questions about why this way and not this way?
    Please play with the code.
    Feel free to think in different ways

Future readings:
    https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons
    https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    https://refactoring.guru/design-patterns/singleton/python/example

"""


# class ConfigurationManger:
#     __instance = None
#
#     # Push the whole old class as inner one
#     class ConfigurationMangerInner:
#         def __init__(self, configuration_path):
#             self.configuration_path = configuration_path
#             # Other attributes
#             self._load()
#
#         def _load(self):
#             # takes 30 minutes to load data
#             print('Loading the Configuration')
#             self.servers_ips = ["10.20.30.40",
#                                 "10.20.30.41", "10.20.30.42"]
#             self.aws_service_url = "amazon-aws.com"
#             # load heavy data
#             import time
#             time.sleep(2)
#
#     def __init__(self, configuration_path):
#         # If no instances created before, create one. This way we make it one for callers
#         if not ConfigurationManger.__instance:
#             ConfigurationManger.__instance = ConfigurationManger.ConfigurationMangerInner(configuration_path)
#
#     # Delegate methods/attributes calls
#     @property
#     def configuration_path(self):
#         return ConfigurationManger.__instance.configuration_path
#
#     @configuration_path.setter
#     def configuration_path(self, value):
#         ConfigurationManger.__instance.configuration_path = value
#
#
# def f1():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# def f2():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# def f3():
#     mgr = ConfigurationManger('disk/config.json')
#     print(mgr.configuration_path)
#
# if __name__ == '__main__':
#     f1()
#     f1()
#     f1()
#     f2()
#     f3()



















