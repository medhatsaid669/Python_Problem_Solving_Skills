# Polymorphism

"""What is Polymorphism?
● Polymorphism = many forms
● The ability to use Functions/Methods/Operators/Objects with different types
and potentially behave differently
○ Think + operators with numbers sum them, but with strings concatenate them (different
behaviour)
● In languages like C++, the concept
appears strongly when explaining!
● But python is polymorphic by design!"""


# # len functions receives many types(forms)
# print(len([1, 2, 3]))
# print(len(((6, 7), 'hey')))
# print(len("mostafa"))
#
# # + * operators can be used with several types
# # But behave differently!
# print(2 + 3 * 4)
# print('Most' + ' Saad' * 4)

"""Duck Typing
● If it walks like a duck, and it quacks like 
a duck, then it must be a duck
○ Methods matters much more than the object 
type!
■ Does it support the requested 
behaviour?
○ To call len(something), object needs to define 
__len__, Regardless the object type!
● Observe: Polymorphism even doesn’t 
need inheritance to exist!"""

# class Car:
#     def get_name(self):
#         return 'BMW'
#
# class Person:
#     def get_name(self):
#         return 'Mostafa'
#
# class Home:
#     pass
#
# def process(obj):
#     # any object that has
#     # get_name method is good
#     print(obj.get_name())
#
# process(Car())
# process(Person())
#
# # AttributeError: 'Home' object
# #  has no attribute 'get_name'
# #process(Home())

# Shape Example

# class Shape:
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @property
#     def area(self):
#         raise NotImplementedError
#
# class Rectangle(Shape):
#     def __init__(self, name, wid, height):
#         super().__init__(name)
#         self.wid = wid
#         self.height = height
#
#     @property
#     def area(self):
#         return self.wid * self.height
#
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius
#
#     @property
#     def area(self):
#         from math import pi
#         return 2 * pi * self.radius
#
# class Editor:
#     def __init__(self):
#         self.shapes = []
#
#     def process(self):
#         area_sum = 0
#         for shape in self.shapes:
#             print(shape.name, shape.area)
#             area_sum += shape.area
#         return area_sum
#
# if __name__ == '__main__':
#     editor = Editor()
#     editor.shapes.append(Rectangle('Rect1', 3, 5))
#     editor.shapes.append(Circle('MyCirc', 2))
#     editor.shapes.append(Rectangle('Rect2', 10, 2))
#     print(f'area sum = {editor.process()}')

"""Inverse of control
● Normal flow: child class knows parent class. But what if parent class is waiting for something from children?
● Method print is calling area property
● This is a case where high-level class is calling low-level class
● Core step in frameworks named Inverse of control"""

# class Shape:
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def print(self):
#         print(self.name, self.area)
#
# class Rectangle(Shape):
#     def __init__(self, name, wid, height):
#         super().__init__(name)
#         self.wid = wid
#         self.height = height
#
#     @property
#     def area(self):
#         return self.wid * self.height
#
# if __name__ == '__main__':
#     Rectangle('Rect1', 3, 5).print()

# Inverse of control: Example

# class GraphAlgorithm:
#     def __init__(self):
#         self.algorithms_steps = [self.step1_general,
#                                  self.step2_abstract,
#                                  self.step3_general]
#
#     def run(self):
#         return ''.join([step() for step in self.algorithms_steps])
#
#     def step1_general(self):
#         return 'G1'
#
#     def step3_general(self):
#         return 'G3'
#
# class Dijkstra(GraphAlgorithm):
#     def __init__(self):
#         super().__init__()
#
#     def step2_abstract(self):
#         return 'APQ'
#
# print(Dijkstra().run())

"""Inverse of control: Example
Composition over Inheritance
● In inheritance: we highlighted several issues in (multiple) inheritance
● Composition is the way to go
○ You avoid the “combination hell” of inheritance (RobotDog)
○ Built-in polymorphism (duck typing) make things intuitive
● Design patterns are typically needed
○ Delegate pattern to switch B inherits A to ⇒ B has delegate of A
○ Switch template pattern to strategy pattern
○ Decorator pattern to avoid the Exploding class hierarchy
● Cons
○ More code to do delegation of calls on composed objects
■ You may need to wrap/delegate some classes to remove irrelevant functions
○ More code to create instances of intermediate classes ⇒ use Factory Pattern"""


# Abstraction

"""What vs How
● Do you care how:
○ a TV/Car work? Google really search and find results? Browser access internet?
○ Python computes pow(2.0, -3.2)
○ Python handles OS to read/write from files using fstream?
● Most of time, the user cares with WHAT not HOW
○ What = Function takes and return
○ How = it is implemented. But
■ Some implementation can be slow (loop to sum 1 to n) or fast (sum = n * n+1 / 2)
■ Some might be buggy or stable (internet explorer vs Firefox)
■ Some might takes more memory (chrome vs Firefox)
○ We can change internal implementation of class independently without affecting the user.
■ User depends on limited visible functionalities of specific WHAT details"""


"""Abstraction Concept
● Abstraction is about hiding unwanted details while showing most essential in 
a given context 
○ The statement is easily explained & in administered C++/Java (public / private / separation)
● For now think:
○ Abstract = Focus on High level (what not how)
■ Implementation is hidden 
● Off-topic
○ Useful about 
abstraction in CS
○ Smart guys have high Abstract thinking skills
■ Algorithms, Problem solving, Management"""

"""Abstraction Concept
● Does shape class cares How area method is implemented?
○ No. Hide/Abstract this details. It cares about what"""

"""What is wrong?
● Shape class can’t provide implementation to the area method/property
● What if a user created object from shape?
○ In first solution, we handled that by raising exception. None in second code
● Shape is incomplete class. How to prevent object creation?
○ There must be a child class that implements missing methods (e.g. Rectangle) """

"""Abstract Classes (ABC)
● Describes the behavior of an incomplete class 
○ Future derived classes add their particular implementations
○ An abstract class should have at least one abstract method (e.g. shape area() )
● Python allows us to mark a class or method as abstract
○ You can’t create an object from an abstract class that has an abstract method
● In next session, we see how to code that!"""


# Abstract Classes

"""Abstract class
● Inheriting from ABC = marks class as abstract class
● Using decorator abstract method, we mark method abstract
● If an abstract class has a single 
abstract method, we can’t create object
● An abstract class can has non-abstract methods"""

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
# # TypeError: Can't instantiate abstract class .
# # Shape with abstract methods get_area
# Shape('')

"""A child class, but still abstract
● If the child class doesn’t provide implementation to ALL abstract method of an abstract class, then it is also abstract class
○ Even if the abstract method has default implementation
■ You can use super().something"""

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @abstractmethod
#     def get_area(self):
#         return -1
#
# class Rectangle(Shape):
#     def __init__(self, name, wid, height):
#         super().__init__(name)
#         self.wid = wid
#         self.height = height
#
# # # TypeError: Can't instantiate abstract class
# print(Rectangle('Rect', 3, 4).get_area())

"""Complete Class
● Now Rectangle class is a complete class
● It already provides impl"""

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, name, wid, height):
#         super().__init__(name)
#         self.wid = wid
#         self.height = height
#
#     def get_area(self):
#         return self.wid * self.height
#
# print(Rectangle('Rect', 3, 4).get_area())   # 12

"""With properties
● In python 3, just add abstract method decorator normally
● Follow this order:
○ @property  [FIRST]
○ @abstractmethod
● The same with @classmethod, @staticmethod"""

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     @property
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, name, wid, height):
#         super().__init__(name)
#         self.wid = wid
#         self.height = height
#
#     @property
#     def area(self):
#         return self.wid * self.height
#
# print(Rectangle('Rect', 3, 4).area)   # 12

"""Messages
● Abstract classes make code more cleaner
○ We avoid raise exceptionWe avoid not writing the method
● Communicate intentions
○ When we know the class is abstract, we understand this is incomplete
○ We need to provide ALL abstract methods to have a complete class"""

# from abc import ABC, abstractmethod
#
# class GraphAlgorithm(ABC):
#     def __init__(self):
#         self.algorithms_steps = [self.step1_general,
#                                  self.step2_abstract,
#                                  self.step3_general]
#
#     def run(self):
#         return ''.join([step() for step in self.algorithms_steps])
#
#     def step1_general(self):
#         return 'G1'
#
#     @abstractmethod
#     def step2_abstract(self):
#         pass
#
#     def step3_general(self):
#         return 'G3'
#
# class Dijkstra(GraphAlgorithm):
#     def __init__(self):
#         super().__init__()
#
#     def step2_abstract(self):
#         return 'APQ'
#
# print(Dijkstra().run()) # G1APQG3


# Interfaces and APIs

"""Interfaces
● If all abstract class methods are abstract, we call it interface
○ No state or implemented methods
○ It can give sense of views: This class is printable, comparable and runnable (3 interfaces)
○ More advanced points in Python Metaprogramming
● Culture in other programming language
○ More explicit referring/need for interface. 
■ Dependency on Interfaces with Polymorphism is a standard practice
○ Properties: In inheritance you think: Employee is a person 
■ With Interfaces: you might think also in properties as a parent class 
■ E.g. a class is Printable, Diskable(Savable, Loadable), Clonable, Comprable, etc
○ Due to duck typing, we don’t use interfaces frequently"""


# Interfaces: Device Driver

# from abc import ABC, abstractmethod
#
# class ICameraDevice(ABC):
#     @abstractmethod
#     def get_version(self):
#         pass
#
#     @abstractmethod
#     def start(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class UbuntuDriverOpenSource(ICameraDevice):
#     pass  # Override methods
#
# class UbuntuDriver3rdPart(ICameraDevice):
#     pass  # Override methods
#
# class Windows10Driver(ICameraDevice):
#     pass  # Override methods
#
#
# class UbuntuOS:
#     def get_app(self, app_name):
#         return UbuntuDriverOpenSource()
#
# if __name__ == '__main__':
#     os = UbuntuOS()
#     device = os.get_app('camera cheese')
#     device.start()
#     device.stop()


"""Coupling
● Coupling is the measure of the degree of interdependence between the 
modules/classes. [critical SWE concept]
○ Target: low coupling
● If the Camera App will code for a specific driver, then if you decided to change 
the driver which has its own methods (start() vs run() - stop() vs shutdown()), 
then the system is highly coupled, which is so bad
● But if we have a common interface and each driver is following it, our camera 
app doesn’t need to know which driver is installed
○ Thanks also for polymorphism. This is very visible in C++/Java
Interfaces Guidelines
● Interface = contract. Don’t break it. 
○ Changes may cause compilation errors. Consider backward compatibility.
○ Think deeply about method signature
● A minimal public interface
○ Doesn’t include your common or private functions
○ Avoid irrelevant functionalities / hard to get 
● Principle of Least Surprise
○ Most guys don’t read documentation. Expected resulting behaviour = match function name
● Think from client/user perspective: 
○ What are their needs? 
■ Make their life easy as possible
○ Intuitive/minimal usage for your interface = default/fair behaviour
Application programming interface (API)
● Software intermediary (interface) that allows two applications to talk to 
each other. 
○ Mobile apps like Facebook, Hangout, Weather are using an API.
○ Messenger ⇒ Facebook Messenger API ⇒ Facebook backend
■ Facebook backend provides this API to a few specific functionalities
○ They contact remote API
■ Communication + Request (function: param+return) + Response (e.g. JSON or XML)
○ Future readings: 
API design, 
Backend as API
Img 
Src
Application programming interface (API)
● Example: Payment API (top 
ones)
○ Many software we develop allows user payments (e.g. credit/debit cards)
○ It is waste of time to build several codes to contact/verify by yourself
○ We use payment APIs (e.g. Paypal or Stripe APIs)
○ They do the verifications, take user info + money to withdraw
■ We pay them some subscription (e.g. 0.1 dollar per transaction)
○ All the APIs will provide similar functionalities, but different style
■ E.g. different function names, parameters, call orders, authentication
● Example: Airlines API (top 
ones)
○ You want to go from Cairo to Vancouver
○ Go to expedia. Expedia call the API for different airlines
■ You can go through Toronto (AirCanada API), Istanbul (Turkish airlines API)
■ Also you can go through 3 cities in Germany (Lufthansa airlines API)
API vs Library vs SDK vs Framework
● Library: Functions/Classes ready to use (e.g. sorted / dict)
● Software development kit (SDK): Collection of tools in one installable 
package to make development and debugging easy (E.g. JDK, IOS SDK)
● Framework: High level - group of libraries, typically with inversion of control 
(IoC) pattern. Typically some abstract design, with more behavior built in. 
○ You insert your code in a few places (e.g. subclassing, let’s call it Class C)
○ The framework e.g. has specific pipeline: A, B, AbstractC, D, E
■ A, B, D are already implemented and fixed. You may override E.
■ Framework calls them in order, but for AbstractC calls your Class C (Polymorphism)
● E.g. Your class C prepare specific data for the web-page to view
○ Your code calls library, but Framework calls your code (inverse of the flow)
Relevant: User interface (UI) & User experience (UX)
● UI/UX is not CS job
○ Frontend dev use UI
○ Console / GUI not frequent now
○ Web & Mobile
○ UI design is all about how the product’s interfaces look and function.
○ UX design is all about the overall feel of the 
experience
○ Reading"""


# Polymorphism Homework 1

"""Problem #1: Explain ATM-Machine UML
● Like most of ATM Machine
○ You can check your balance
○ Withdraw or deposit money
■ E.g. from seperate parts"""

# In summary
#     ATM composed of 4 hardware components
#     It can execute a transaction (polymorphism), which can be one 3 types.
#         Deposit & Withdraw each is associated with a hardware
#     ATM need to interact with Database to verify the login account
#     Also transaction needs some database ID for operation + change balance

"""Problem #2: Square
● A fresh engineer designed the following diagram
○ Why do you think he thought this way?
○ Figure out a reason why it is a risky design?
■ Code this inheritance modeling
○ Figure out another way to design the same purpose"""

"""- The engineer thought: Square is a rectangle with all sides equal
- This is good for a Square class
- But in practice, some function might set length/witdth and corrupt the object status!

- Tip: Make sure your sub-class is really a valid superclass. This is related to the Liskov Substitution Principle

- The best way is composition
- Square class has an instance of type Rectangle
    - Delegate all calls to a rectangle
    - Now we are safe, without the need for inheritance between rectangle and Square

You can also do inheritance, but with careful coding and using properties. I don't feel it that good way"""

# class Shape:
#     def area(self):
#         raise NotImplementedError
#
# class Rectangle():
#     def __init__(self, height, width):
#         self._length = height
#         self._width  = width
#
#     def area(self):
#         return self._length * self._width
#
# class Square1(Rectangle):   # using inheritance
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     @property
#     def side(self):
#         return self._width
#
#     @side.setter
#     def side(self, x):
#         self._length = self._width = x
#
#     @property
#     def length(self, x):
#         raise NotImplementedError
#
#     @property
#     def width(self, x):
#         raise NotImplementedError
#
# sq = Square1(10)
# print(sq.side, sq.area())
# sq.side = 12
# print(sq.side, sq.area())
#
# class Square2:  # Using composition: like a wrapper class
#     def __init__(self, side):
#         super().__init__()
#         self.rect = Rectangle(side, side)   # Square has a rectangle object
#
#     @property
#     def side(self):
#         return self.rect.width
#
#     @side.setter
#     def side(self, side):
#         self.rect = Rectangle(side, side)
#
#     def area(self):
#         return self.rect.area() # Delegate the call
#
# sq = Square1(10)
# print(sq.side, sq.area())
# sq.side = 12
# print(sq.side, sq.area())

"""Problem #3: Package Delivery Service v2
● Recall our implemented packages: StandardPackage, TwoDayPackage, HeavyPackage
● Extend the system with the following:
○ The customer can create a shipment, which is set of packages of different types
■ Total shipment price = sum of each package price
■ Each shipment has information of card used for payment (debit or credit)
● Add a few new classes that represents the updated system"""

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
#     @property
#     def total_cost(self):
#         return self.weight_kg * self.price_per_kg
#
# class TwoDayPackage(StandardPackage):
#     def __init__(self, sender_address: Address, reciever_address: Address, weight_kg, price_per_kg, fixed_fee):
#         super().__init__(sender_address, reciever_address, weight_kg, price_per_kg)
#         self.fixed_fee = fixed_fee
#
#     @property
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
#     @property
#     def total_cost(self):
#         res = super().total_cost()
#
#         if self.weight_kg > self.weight_limit:
#             res += (self.weight_kg - self.weight_limit) * self.extra_price_per_kg
#
#         return res
#
# #############################
#
# class Card:
#     def pay(self, money):
#         pass
#
# class CreditCard(Card):
#     pass
#
# class DebitCard(Card):
#     pass
#
# class Shipment:
#     def __init__(self, card):
#         self.packages = []
#         self.card = card
#
#     @property
#     def total_cost(self):
#         return sum([package.total_cost for package in self.packages])

# Polymorphism Homework 2

"""Problem #1: Expedia Travel Site
● In expedia a user creates several itineraries, each itinerary consists of several reservations as following
○ 0 or more flights, hotels, cars, etc. E.g. 4 flights, 2 hotels and 2 cars. 
● Each reservation may has its own info
○ E.g. Hotel cost: total nights x price per night
● The itinerary cost = sum of its inner reservations
● Design the set of classes that help developing the system
○ Don’t go in the classes details. This is a high-level question
○ Keep it simple, but smart
○ For now: Model flights and hotels
○ Design needs to be extensible (e.g. in future we can add more types: cars / cruise)"""

# from abc import ABC, abstractmethod
#
# class Reservation(ABC):
#     @property
#     @abstractmethod
#     def total_cost(self):
#         pass
#
# class FlightReservation(Reservation):
#     def __init__(self, price):
#         self.price = price
#
#     @property
#     def total_cost(self):
#         return self.price
#
# class HotelReservation(Reservation):
#     def __init__(self, price_per_night, total_nights):
#         self.price_per_night = price_per_night
#         self.total_nights = total_nights
#
#     @property
#     def total_cost(self):
#         return self.price_per_night * self.total_nights
#
# class ItineraryReservation(Reservation):
#     def __init__(self, reservations=None):
#         self.reservations = [] if reservations is None else reservations
#
#     @property
#     def total_cost(self):
#         return sum([reservation.total_cost for reservation in self.reservations])
#
# if __name__ == '__main__':
#     iti = ItineraryReservation()
#     iti.reservations.append(FlightReservation(1001))
#     iti.reservations.append(FlightReservation(2001))
#     iti.reservations.append(HotelReservation(200, 5))
#     print(iti.total_cost)

"""Problem #2: Payment Services
● Craigslist website (classified-ads) is adding new feature for customers payment. 
○ There are a lot of API to use. Each API has fees in some style
■ E.g. 1 dollar per 25 payments
■ The rules might change from time to time
■ New APIs with new fees might be available on web
■ All APIs provide similar functionalities, but different interfaces
○ At the moment, developers want to support to payment methods: PayPal and Stripe
○ Coding tips:
■ The project code shouldn’t depend on one of the APIs. 
■ Otherwise, a lot of code has to be changed with every a change in the selected API
● Focus on high level. Develop simple main. Problem #2: Payment Services
● Paypal payment API. This is 3rd party we call. You can’t change methods namesProblem #2: Payment Services
● Stripe payment API"""

"""Every API has its own attributes and methods, although share same functionality

Our code base can't depend on one specific API. Otherwise, once we change it, we change all our code!

Define an interface to be unifed. Our codebase depends on it only. This is called loose coupling (means our code is not tight to something).
    Tip: This is very critical in other languages such as Java and C#"""

# from abc import ABC, abstractmethod
#
# class IPayment(ABC):  # I for interface
#     @abstractmethod
#     def set_user_info(self, name, address):
#         pass
#
#     @abstractmethod
#     def set_card_info(self, id, expire_date, ccv):
#         pass
#
#     @abstractmethod
#     def make_payment(self, money):
#         pass
#
# class PayPalCreditCard:
#     def __init__(self, name=None, address=None,
#                  id=None, expire_date=None, ccv=None):
#         self.name = name
#         self.address = address
#         self.id = id
#         self.expire_date = expire_date
#         self.ccv = ccv
#
# class PayPalOnlinePaymentAPI:
#     def __init__(self, card_info: PayPalCreditCard = None):
#         self.card_info = None
#
#     def pay_money(self, money):
#         print(f'PayPalOnlinePaymentAPI request')
#         return True  # Call PayPal backend
#
# class StripeUserInfo:
#     def __init__(self, name=None, address=None):
#         self.name = name
#         self.address = address
#
# class StripeCardInfo:
#     def __init__(self, id=None, expire_date=None):
#         self.id = id
#         self.expire_date = expire_date
#
# class StripePaymentAPI:
#     @staticmethod
#     def withdraw_money(user_info, card_info, money):
#         print(f'StripePaymentAPI request')
#         return True  # Call Stripe backend
#
# ##########
# # Implement our own classes that wrap the APIs and following the payment interface
#
# class PayPalPayment(IPayment):
#     def __init__(self):
#         self.paypal = PayPalOnlinePaymentAPI()
#         self.card = PayPalCreditCard()
#
#     def set_user_info(self, name, address):
#         self.card.name = name
#         self.card.address = address
#
#     def set_card_info(self, id, expire_date, ccv):
#         self.card.id = id
#         self.card.expire_date = expire_date
#         self.card.ccv = ccv
#
#     def make_payment(self, money):
#         self.paypal.card_info = self.card
#         return self.paypal.pay_money(money)
#
# class StripePayment(IPayment):
#     def __init__(self):
#         self.card = StripeCardInfo()
#         self.user = StripeUserInfo()
#
#     def set_user_info(self, name, address):
#         self.user.name = name
#         self.user.address = address
#
#     def set_card_info(self, id, expire_date, ccv):
#         self.card.id = id
#         self.card.expire_date = expire_date
#         self.card.ccv = ccv
#
#     def make_payment(self, money):
#         return StripePaymentAPI.withdraw_money(self.user, self.card, money)
#
# ############
# # Create our side code depending on the interface NOT on an API that may change soon
#
# class TransactionInfo:
#     def __init__(self, required_money_amount, name, address, id, expire_date, ccv):
#         self.required_money_amount = required_money_amount
#         self.name = name
#         self.address = address
#         self.id = id
#         self.expire_date = expire_date
#         self.ccv = ccv
#
# class Craigslist:  # This class depends on IPayment. No idea about Paypal/Stripe/Whatever
#     def __init__(self, payment: IPayment):
#         self.payment = payment
#
#     def do_payment(self, info: TransactionInfo):
#         self.payment.set_user_info(info.name, info.address)
#         self.payment.set_card_info(info.id, info.expire_date, info.ccv)
#
#         return self.payment.make_payment(info.required_money_amount)
#
# if __name__ == '__main__':
#     # site = Craigslist(StripePayment())
#     site = Craigslist(PayPalPayment())
#
#     info = TransactionInfo(20.5, "mostafa", "canada", "11-22-33-44", "09-2021", 333)
#
#     site.do_payment(info)


# Special Methods: Arithmetic, Compound, Comparison, Unary

"""Special Methods
● We know we can do A + B
○ Both can be strings or integers
● What if I have my user-defined class and want to support such behaviour?
○ E.g. Create vector or matrix class
● We do that through overriding specific dunder methods
○ We already studied some of them"""

"""Arithmetic Operator +
● By adding __add__ dunder, we can allow addition of our class’s object and something else (whatever class, no restriction) """

# class MyPair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def __repr__(self):
#         return f'({self.first}, {self.second})'
#
#     def __add__(self, other):
#         return MyPair(self.first  + other.first,
#                       self.second + other.second)
#
# if __name__ == '__main__':
#     p1 = MyPair(2, 3)
#     p2 = MyPair(4, 7)
#     p3 = p1 + p2
#     print(p3)       # (6, 10)

"""Arithmetic Operators
● You can do the same logic with the other operators
●-  ⇒   __sub__
● *  ⇒   __mul__
● /  ⇒   __truediv__
● //  ⇒  __floordiv__
● %  ⇒ __mod__
● **  ⇒  __pow__
● @ ⇒  __matmul__     (matrix multiplication, as in numpy)"""

"""Compound Operator += 
● In this operator, we change the object itself NOT create a new one
● You should return self to be assigned to the caller object again
● Tip: iadd = in-place add"""

"""Comparison operator <
● With __lt__ we can support less than between 2 objects
● This allows us to sort list of employees e.g. based on age & salary"""


# class MyPair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def __repr__(self):
#         return f'({self.first}, {self.second})'
#
#     def __lt__(self, other_pair):
#         return self.first < other_pair.first and \
#                self.second < other_pair.second
#
# if __name__ == '__main__':
#
#     p1 = MyPair(5, 10)
#     p2 = MyPair(7, 13)
#     p3 = MyPair(4, 12)
#
#     print(p1 < p1)  # False
#     print(p1 < p2)  # True
#     print(p1 < p3)  # False
#     print(p3 < p2)  # True

"""Comparison Operators
● You can do the same logic with the other operators
○ If you tried to compare without defining, you may get error
● <=  ⇒   __le__
● ==  ⇒   __eq__
● !=  ⇒   __ne__
● >  ⇒  __gt__
● >=  ⇒ __ge__"""

"""Comparison operator: lt and eq is enough
● Mathematically, with only < operator and eq, we can know for the other comparisons over objects
○ p1 != p2 is same as not (p1 == p2)
○ p1 > p2 is same as p2 < p1 and so on
● The functools module is for higher-order functions: functions that act on or return other functions. From it we have total_ordering
○ Class decorator that fills in missing ordering methods
○ That is you define a few, and all others are DONE for you
○ You can only support le. But default eq depends on membership (p1 is p2)
○ Practically: providing both lt and eq is enough to avoid mistakes!"""

# Comparison operator: Total Ordering Decorator

# from functools import total_ordering
#
# @total_ordering
# class MyPair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def __repr__(self):
#         return f'({self.first}, {self.second})'
#
#     def __lt__(self, other_pair):  # -pair
#         return self.first < other_pair.first and \
#                self.second < other_pair.second
#
#     def __eq__(self, other_pair):
#         return self.first == other_pair.first and self.second == other_pair.second
#
# if __name__ == '__main__':
#
#     p1 = MyPair(5, 10)
#     p2 = MyPair(5, 13)
#
#     print(p1 <= p2)  # False: Recall p1 <= p2: p1 < p2 or p1 == p2, both are false
#     print(p1 != p2)  # True

"""Override what u need
● If generating missing functions may break your semantic, just overwrite yours"""

# from functools import total_ordering
#
# @total_ordering
# class MyPair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def __repr__(self):
#         return f'({self.first}, {self.second})'
#
#     def __lt__(self, other_pair):  # -pair
#         return self.first < other_pair.first and \
#                self.second < other_pair.second
#
#     def __le__(self, other_pair):  # -pair
#         return self.first <= other_pair.first and \
#                self.second <= other_pair.second
#
#     def __eq__(self, other_pair):
#         return self.first == other_pair.first and self.second == other_pair.second
#
# if __name__ == '__main__':
#     p1 = MyPair(5, 10)
#     p2 = MyPair(5, 13)
#
#     print(p1 <= p2)  # True
#     print(p1 != p2)  # True

# Sorting list of objects!

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __repr__(self):
#         return f'({self.name}, {self.salary})'
#
#     def __lt__(self, other): # More pythonic style
#         return (self.name, self.salary) < (other.name, other.salary)
#
#     def __lt__V2(self, other):  # on name first, if tie on salary
#         # More of Old C++ Culture
#         if self.name != other.name:
#             return self.name < other.name
#
#         return self.salary < other.salary
#
# lst = [Employee('mostafa', 10),
#        Employee('Ziad', 100), Employee('mostafa', 7)]
# lst.sort()
# print(lst)  # [(Ziad, 100), (mostafa, 7), (mostafa, 10)]

# Unary Operators

# class MyPair:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def __repr__(self):
#         return f'({self.first}, {self.second})'
#
#     def __neg__(self):   # -pair
#         return MyPair(-self.first, -self.second)
#
# if __name__ == '__main__':
#     p1 = MyPair(2, 3)
#     print(-p1)       # (-2, -3)

# Special Methods Reflection

