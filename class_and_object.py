# Class Homework 1

"""Rectangle and Circle
● Create these 2 classes and test
them
● Assume PI = 3.14"""

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#
# r = Rectangle(2, 5)
# print(r.get_area())     # 10
#
# c = Circle(5)
# print(c.get_area())     # 78.5


"""Editor
● Class editor has 2 objects: 
rectangle and circle
● Create methods initialize 
these 2 objects
● Change method add a 
factor to the data
○ E.g. if Rect = (3, 5)
○ Factor 2 ⇒ (3+2, 5+2)
● Print just print
● See the screenshot"""

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#
# class Editor:
#     def __init__(self):
#         self.rect = None
#         self.circle = None
#
#     def create_rectangle(self, width, height):
#         self.rect = Rectangle(width, height)
#
#     def create_circle(self, radius):
#         self.circle = Circle(radius)
#
#     def change_rectangle(self, factor):
#         if self.rect == None:       # we should use is None (soon)
#             return
#
#         width, height = self.rect.width + factor, self.rect.height + factor
#         self.create_rectangle(width, height)
#
#     def change_circle(self, factor):
#         if self.circle == None:       # we should use is None (soon)
#             return
#
#         self.create_circle(self.circle.radius + factor)
#
#     def change(self, factor):
#         self.change_rectangle(factor)
#         self.change_circle(factor)
#
#     def print(self):
#         if self.rect != None:
#             print('Rectangle area', self.rect.get_area())
#
#         if self.circle != None:
#             print('Circle area', self.circle.get_area())
#
#
#
# editor = Editor()
# editor.create_rectangle(3, 5)
# editor.print()
# #Rectangle area 15
# editor.create_circle(5)
# editor.change(2)
# editor.print()
# #Rectangle area 35
# #Circle area 153.86

"""Homework 1: Our MyRange Class
● Remember:
○ range(5, 10, 1) ⇒ 5 6 7 8 9
○ range(5, 10, 2) ⇒ 5 7 9
● We will implement something that give us thoughts how such things work 
internally"""
#
# class MyRange:
#     def __init__(self, start, end, step):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     # we will assume user will be nice won't do illegal get_next
#
#     def has_next(self):
#         return self.start < self.end
#
#     def get_next(self):
#         ret = self.start
#         self.start += self.step
#         return ret
#
#
# rng = MyRange(5, 10, 1)
#
# while rng.has_next():
#     print(rng.get_next(), end=' ')  # 5 6 7 8 9
# print()
#
# rng = MyRange(5, 10, 2)
# while rng.has_next():
#     print(rng.get_next(), end=' ')  # 5 7 9

"""Homework 2: Our MyRange Class (Flexible)
● You will re-implement to allow to extra points:
○ Step can be positive or negative
○ get_next return 2 items: idx and value  (like enumerate)"""

# class MyRange:
#     def __init__(self, start, end, step):
#         self.start = start
#         self.end = end
#         self.step = step
#         self.idx = 0
#
#     def has_next(self):
#         if self.step > 0:
#             return self.start < self.end
#         return self.start > self.end
#
#     def get_next(self):
#         ret = self.idx, self.start
#         self.start += self.step
#         self.idx += 1
#
#         return ret
#
#
# rng = MyRange(10, 5, -1)
#
# while rng.has_next():
#     print(rng.get_next())






