# Datetime
"""Datetime Module
● Python has several standard/built-in modules that we use in practice
○ Such as datetime and time modules
● datetime module has 4 commonly used classes
○ date Class
○ time Class
○ datetime Class
○ timedelta Class
● Common mistake:
○ To import datetime module and use it as the class (you have to import the internal class)"""


"""Date and Time classes
● In this code we shows the internal time and date classes"""
#
# import datetime
# # Constructor: hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0
# dt = datetime.time(14, 7)    # 2:07 pm
# print(dt)               # 14:07:00
# print(dt.hour)          # 14
# print(dt.minute)        # 7
# print(dt.second)        # 0
# print(dt.microsecond)   # 0
# print(type(dt))         # <class 'datetime.time'>
# print(datetime.time(14, 7, 59, 300))    # 14:07:59.000300
# dt = datetime.date.today()
# print(dt, type(dt))     # 2021-01-11 <class 'datetime.date'>: yyyy-mm-dd
# # we can access dt.year or month or day
# print(dt.ctime())       # Mon Jan 11 00:00:00 2021


"""Datetime and Timedelta Classes
● Datetime can represent both info for time and date
● We can also get the difference between 2 dates"""

# import datetime
# dt = datetime.datetime(2021, 1, 11, 14, 7, 59, 300)
# # or use
# print(dt.ctime())       # Mon Jan 11 14:07:59 2021
# newdt = dt.replace(year=1990, day=25, second=13)
# print(newdt)    # 1990-01-25 14:07:59.000300
# delta = dt - newdt
# print(delta, type(delta))   # 111309 days, 0:00:46 <class 'datetime.timedelta'>
# print(delta.seconds)            # 46
# print(delta.total_seconds())    # 977097646
# # immutables


"""Passing Arguments
● Be careful from this 
common mistake
● The default arguments 
first values are used
○ C++ is different in that """


# from datetime import datetime
#
# def hello1(curdate = datetime.now()):
#     print(curdate)
#
# for i in range(10):
#     hello1()  # ALL of them are SAME!
#     # 2021-01-11 21:36:03.142533
#
# def hello2(curdate=None):
#     if curdate is None:
#         curdate = datetime.now()
#     print(curdate)  # ALL of them are Different!
#
# for i in range(10):
#     hello2()
# # Never use mutable or varying values as default arguments!


"""Passing Arguments
● More clear with mutable objects"""
#
# def hello(lst = []):
#     lst.append(1)
#     print(lst)
#
# hello() # [1]
# hello() # [1, 1]
# hello() # [1, 1, 1]


"""Time Module
● With time module, we can do several things
● Get localtime and its date/time components
● Compute time difference between points
○ Helps in benchmarking: assess the relative performance of a part of code / program
○ We have 3 ways to code a function. There is 2 3rd party packages to install. Which one?
● Printing functionalities for a flexible output
● The computed time is relative: from a starting point named epoch
○ Which is platform dependent"""

# Time
# import time
#
# if __name__ == '__main__':
#     # Convert seconds since the Epoch to a time tuple expressing UTC (GMT)
#     # The epoch is the point where the time starts
#     # Platoform dependent: Unix, the epoch is January 1, 1970, 00:00:00 UTC (GMT)
#     print(time.gmtime(0))
#
#     print(time.localtime())
#     # time.struct_time(tm_year=2021, tm_mon=1, tm_mday=17, tm_hour=9, tm_min=43,
#     #   tm_sec=7, tm_wday=6, tm_yday=17, tm_isdst=0)
#     print(time.localtime().tm_hour)  # 9
#     print(time.localtime()[3])       # 9 - access the object using index
#
#     print(time.time())  # 1610905180.9765534
#     # [we are in 2021 - 1970 = 51 years => ~51*365*24*60*60


"""Sleep and time difference
● Sleeping is a common functionality in practice
● For example, each 5 minute check if there is an update in a specific web page"""

# import time
#
# start_time = time.time()
#
# for i in range(5):
#     print(i)
#     time.sleep(1)   # hang for 1 second
#
# end_time= time.time()
# time_dif = end_time - start_time
# print(time_dif)    # 5.003431558609009


# From date to a formatted string
# import time
#
# if __name__ == '__main__':
#     tm = time.localtime()
#
#     # method returns a string representing date and time
#     print(time.strftime('%m/%d/%Y, %H:%M:%S', tm))  # 01/17/2021, 11:03:55
#     print(time.strftime('%H-%M-%S', tm))            # 11-03-55
#     print(time.strftime('%M', tm))                  # 03
#     print(time.strftime('%c', tm))                  # Sun Jan 17 11:07:55 2021
#
#     cur_time = time.time()
#     print(time.strftime('%S', time.localtime(cur_time)))    # 55
#
#     print(time.strftime('%R', tm))  # time in 24 hour notation
#     # It is also available from datetime object
#     # There are more options: read docs strftime

# From formatted string to a date
# import time
#
# if __name__ == '__main__':
#     # strptime() method creates a datetime object from the given string.
#     tm = time.localtime()
#     string = time.strftime('%c', tm)
#     print(string)       # Sun Jan 17 11:07:55 2021
#
#     tm2 = time.strptime(string)
#     print(tm2.tm_hour)  # 11
#
#     # strptime is short for "parse time"
#     # strftime is short for "formatting time".
#     # They are opposite functionalities


"""What is wrong with time()?
● time() provides real-world time (kind of) relative to a starting point
○ Good we can understand intuitively
○ It is maintained by the dedicated hardware on most computers
● The major issue with it is adjustable!
○ The clock can be changed by the system administrator
○ This makes it unreliable. Suddenly the time can decrease!
● Python has several other paths
○ clock (deprecated), perf_counter, monotonic
● The recommended one is perf_counter
● Future readings: 
link 
link
perf_counter
● It provides a relative time and has no reference time point
● It can be used only to measure time intervals
○ For more accurate results, we use timeit module (future)
■ Run a code like 1000000 times and average to know how much does it it takes
● It is not adjustable and administrator can’t affect it!"""

# import time     # for .sleep
# from time import perf_counter
#
# start_time = perf_counter()
#
# for i in range(5):
#     print(i)
#     time.sleep(1)   # hang for 1 second
#
# end_time= perf_counter()
# time_dif = end_time - start_time
# print(time_dif)    # 5.003786797984503
#
# # perf_counter_ns(): Py3.7: return time as nanoseconds

"""Future
● Some more extra functionalities in 
time module
● Proper handling for timezone  (pytz module)
○ Datetime and Time modules are poor for timezone
○ Time Zones and 
Daylight savings time (DST)
● Datetime or time class?
○ If you are dealing with time zones issues, go 
● Reading 
Reading
datetime+pyt"""

