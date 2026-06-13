"""Modules & Packages
● In practice, real projects are so big!
○ We can’t keep all code in a single file
○ We keep breaking the project to smaller tasks.
○ This is called Modular programming
■ Why: Simplicity, Maintainability, Reusability, etc
● Python way
○ The smallest task in python is called a module
○ Module: A single .py file focusing on a specific task(s)
○ Package: Group of modules (py files), so a bigger sub-problem scope
○ Scoping: Each module has a different namespace ⇒ No name collision
■ E.g. If same variable name in 2 modules, no problem at all
Hospital System ⇒ Sub-Tasks
● We wrote the code as all in a single file. Here is a split to 4 modules:
● utlities.py
○
def
input_valid_int(msg, start = 0
● patient.py
○
class
Patient:
● hospitalmgr.py
○
class
HospitalManger:
● frontendmgr.py
○
class
FrontendManager:
, end =
None)
● Now: Assign to different team members different tasks
○ This is how we work as a team. Take a subtask and develop a module / package
Modules: Develop, use or install
● In practice we may:
● 1) develop our own modules (like the hospital system)
● 2) make use of the built-in modules
○ We already used built-in functions (builtins.py) such as max, len, dir
○ Python has more built-in modules that are focused on specific tasks
● 3) install external packages to use its modules
○ Python has a great community!"""



# # please we wanna use math module
# import math
#
# print(math.sqrt(16))        # 4
# print(math.factorial(5))    # 120
# print(math.pi)              # 3.141592653589793
# print(math.cos(math.pi/2))  # 0 - don't cos(90)
#
# # More: Google python math module Or control over math
#
# import math as XXX
# print(XXX.pi)
#
# from math import pi, factorial
# print(pi)
# print(factorial(5))
#
# from math import *  # all is now visible: avoid



# def f():
#     from math import pi, factorial
#     print(pi)
#     print(factorial(5))
#
#     #SyntaxError: import * only allowed at module level
#     #from math import *
#
# if __name__ == '__main__':
#     f()


"""Environment Variables
● Environment variable: (name ⇒ value) that a process may access to get/set 
some info (e.g. for configuration)
○ Some popular ones in linux: HOME, USER, PWD (for current working directory)
■ E.g. echo $PWD  ⇒ /home/moustafa/workspaces/
● PYTHONP
ATH: is an Environment variable, its value are list of directories
○ Soon
■ It is used to ADD PATHS for the user-defined modules 
■
●
Its directories are added to 
sys.path
Through 
os module
 directory list
[primary reason]
, we can access 
environment variables from python
●
Practical usages: 
Future reading"""


# # os module
# import os   # operating system
#
# print(list(os.environ.keys()))
# # ['PATH', 'HOME', 'USER', 'PWD', ..... ]
#
# print(os.environ['HOME'])
# print(os.environ['USER'])
# print(os.environ['PWD'])
# # location of the standard Python libraries
# print(os.environ.get('PYTHONHOME'))
#
#
# # careful if key !exist
# print(os.environ.get('nnnnn'))  # Always None in new session
# os.environ['nnnnn'] = 'Only in this session'
#
# # os.environ doesn’t overwrite the system vars
# # to overwrite: use shell environment, such as Bash
# # Future reading: python-dotenv

#
# # os Directories!
# import os
#
# # directories where EXECUTABLE programs are located
# print(os.environ.get('PATH'))   # e.g. some <>/bin paths
#
# # Most important for us
# print(os.environ.get('PYTHONPATH'))
#
#
# import sys  # parameters specific to the system
#
# # Search path for modules (coming).
# # 1) Script's directory (or current for interactive)
# # 2) Initialized from the environment variable PYTHONPATH,
# # 3) plus an installation-dependent default.
# print(sys.path)


# # sys module
# import sys
#
# print(sys.version)
# print(sys.version_info)
#
# print(sys.platform)
#
# print(len(sys.modules.keys()))
#
# print(sys.prefix)
#
# sys.stdout.write('Hi')
#
# for inp in sys.stdin:
#     print(inp, end = '')

"""Changing PYTHONPATH from OS level
● Consider the following in the future
● We can change pythonpath from OS itself
○ It could be changed per session or permanently
○ It is common question, google it if facing issues
● For Ubuntu/Linux
○ printenv command: print all the environment variables
○ echo $PYTHONPATH ⇒ print current value
○ export PYTHONPATH=$PYTHONPATH:/home/moustafa/misc    [change in session]
● We may also want to change permanently: check out for different OSes
○ Windows - 
Mac/Linux - 
More ways"""



"""Modules
● As we learned, module = python file
● Today, we will create a module and use it by others"""

"""Using our module from file1.py
● We can now create another module
● Run file1.py
● Import the ‘ourlib’ module
● Call its 2 functions as below
● Observe __file__ to print the module path"""

# import ourlib
#
# print(ourlib.sq(5))     # 25
# print(ourlib.sum1n(5))  # 15
#
# # /home/moustafa/workspaces/pycharm/latest/ourlib.py
# print(ourlib.__file__)


# # Using our module from file2.py
#
# from ourlib import  sq  # only sq is visible
#
# print(sq(5))
# # NameError: name 'sum1n' is not defined
# #print(sum1n(5))
#
# #NameError: name 'ourlib' is not defined
# #print(ourlib.__file__)


# Using our module from file3.py
# from ourlib import  *  # all content
#
# print(sq(5))
# print(sum1n(5))
#
# import math
# print(math.pi)


"""Running from line command
● We can run our modules also from CL
● Observe the 2 ways of running the file
○ Make sure to have python visible: python3 --version
○ Try it"""

# def sq(n):
#     return n*n
#
# def sum1n(n):
#     return n * (n+1) // 2


"""The Module Search Path
● When the interpreter executes import ourlib, it searches in order one of these 
3 locations:
○ 1) The script’s directory  (e.g. <>/pycharm/latest for running <>/pycharm/latest/file1.py
■ Observe not the current directory (unless interactive session).
The Module Search Path
● When the interpreter executes import ourlib, it searches in order one of these 
3 locations:
○ 2) list of directories contained in the PYTHONPATH
○ 3) installation-dependent list of directories
● Observe, these 3 things are actually what in sys.path in order"""


"""Missing module
● We have current directory: 04_search
● We have the following directory structure
○ 2 main modules: ourlib and and ourmath
■ Observe ourmath at: somewhere/mycode
○ 2 scripts program1, program2"""

# import ourlib
#
# print(ourlib.sq(5))     # 25
#
#
# # ModuleNotFoundError: No module named 'mymath'
# import mymath
# print(mymath.sum1n(5))
#
# # mymath is not visible
# # neither on script directory (04_search)
# # nor on pythonpath nor installation dirs!
#
# # one way: let's add to sys.path


# import ourlib
#
# print(ourlib.sq(5))     # 25
#
# import sys
# sys.path.append('somewhere/mycode')     # bad / (linux) not windows
#
# import mymath   # now is visible on the path
# print(mymath.sum1n(5))      # 15
#
# # Note: sometimes u want to add in the top of the list

"""Common mistake
● One of the very annoying common mistakes is to name your module similar 
to built-in or installed module. 
● Then when you mean to import the built-in, it may actually importing yours 
(earlier on search path)
○ Tip: Think twice in your file naming.
● Tip: Similar error if you merged several projects without caution"""

"""Module vs Script
● From python perspective: same thing - somefile.py
● Modules are intended to be imported as a library (e.g. ourlib.py)
● Scripts are 
top level files acting like an application (e.g. program1)
○ Usually has printing/logging messages"""

# def sq(n):
#     return n*n
#
#
# print(f'__file__ {__file__}')
# print(f'__name__ {__name__}')
#
#
# if __name__ == '__main__':
#     # It will never be true if we did not
#     # rune ourlib.py ITSELF
#     print('Script from ourlib')


# import ourlib
# print('After importing ourlib')
#
# print(f'__file__ {__file__}')
# print(f'__name__ {__name__}')
#
# # No effect. Loaded once!
# import ourlib
# import ourlib
# import ourlib
#
# if __name__ == '__main__':
#     # Only the script you run has:
#     # __name__ = '__main__'
#     # Otherwise: file name
#     print('Script from program1')


"""Circular Imports
● We learned python imports a module only once!
● The interpreter checks the module registry in sys.modules
○ Is it cached? 
■ Yes ⇒ Use it
■ No ⇒ 1) Mark in the registry. 2) initialize it
● Observe it will be marked although it is partially initialized so far
● But when if module A is importing module B which is importing module A?
○ A ⇒ B ⇒ A Cycle: Circular Import
○ It can be a bigger tricky cycle: A ⇒ B ⇒ C ⇒ D ⇒ A
● This cycle typically causes problems
○ Python itself won’t reimport (stops normally - doesn’t go forever)
○ But some functions/classes might not be defined"""


# Let’s run c.py
""" ● c.py
● c.py: line 1
○ …
○ a.py: line 1
■ …
■ b.py line 1
■ b.py line 2
■ b.py line 3
○ a.py: line 2
○ a.py: line 4
○ a.py: line 3
● c.py: line 2
● Run as a script
● import a
○ Is initialized? No. Mark it & initize
○ import b
■ Is initialized? No. Mark it & initize
■ Import a: in-progress - skip
■ x = 1
■ def bf():
○ def af()
○ call af()
○ b.x: [get from the module] ⇒ 1"""

# import b
# def af():
#     return b.x
# af()

# import a
# x = 1
# def bf():
#     print(a.af())


"""● d.py
● d.py: line 1
○ …
○ b.py: line 1
■ …
■ a.py line 1
■ a.py line 2
■ a.py line 4
■ a.py line 3
● Run as a script
● import b
○ Is initialized? No. Mark it & initize
○ import a
■ Is initialized? No. Mark it & in
■ Import b: in-progress - skip
■ def af()
■ call af()
■ b.x: Error! partially initialized 
module 'b' has no attribute 'x'
● Observe:
○ Running b.py itself won’t cause error
○ As b.py in first run is not marked
■ Script here / NOT imported"""

# import y
#
# def f1():
#     y.f2()
#
# def f3():
#     pass

# import x
#
# def f2():
#     # Move the above import here
#     x.f3()

# import x
#
# x.f1()
#
# import y
# y.f2()


# Same last codes but check in sys
# def check(m):
#     import sys
#     return str(m in sys.modules)
#
# print(f"in top a.by: a {check('a')}")
# print(f"in top a.by: b {check('b')}")
#
# import b
# def af():
#     return b.x
# af()
#
# print(f"in bottom a.by: a {check('a')}")
# print(f"in bottom a.by: b {check('b')}")

# def check(m):
#     import sys
#     return str(m in sys.modules)
#
# print(f"in top b.by: a {check('a')}")
# print(f"in top b.by: b {check('b')}")
#
# import a
#
# x = 1
# def bf():
#     print(a.af())
#
# print(f"in bottom b.by: a {check('a')}")
# print(f"in bottom b.by: b {check('b')}")


"""Handling Cycles
1. This is a bad design. Redesign it
2. Otherwise: consider the following workarounds
3. Merge files together if makes sense (try to respect single responsibility)
4. Delay imports as possible if that breaks cycle (e.g. move inside function)
5. Use TYPE_CHECKING / 
Conditional imports"""

"""Reloading
● Sometimes we may want to reload a module during running
● E.g. it was updated during running
○ import importlib
○ importlib.reload(my_module)"""

# print(dir())    # dir() returns a list of defined names in a namespace
# # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
#
# import ourlib
# print(dir())
# # ['__annotations__', '__builtins__', ... 'ourlib']
#
# print(dir(ourlib))
# # [, 'sq', 'sum1n']
#
# from ourlib import sq
# print(dir())
# # ['__annotations__', '__builtins__', ... 'ourlib', 'sq']
#
# from ourlib import *
# print(dir())
# # ['__annotations__', '__builtins__', ... 'ourlib', 'sq', 'sum1n']



# Homework 1: Employees System as modules
"""Employees System
● We already developed the employees system project in a single file
● Use my provided solution
● Divide to separate module (py) files
● Provide a script that imports and runs the system"""


# Packages 1
"""Packages
● A group of modules structured in the hard disk 
● Practically: 
○ Big projects might be split to different packages
○ We download, install and import modules from 3rd party 
packages
● The example on right:
○ A package named library
■ 2 sub-packages: backend and frontend
● Each package has some files
○ The scripts want to use the package
■ We can import modules from package to use"""

# Importing from a package

"""from library.backend import utilities
print(utilities.sq(10))"""

"""from library.backend.utilities import sq
print(sq(10))"""

"""# you should import module or something in a module
import library
# AttributeError: module 'library' has no attribute 'backend'
print(library.backend.utilities.sq(10))"""


"""Package Initialization
● If you created __init__.py file, it will be called if
○ package or one of its modules is imported
● It can be used to 
○ perform some intializations on the package level
○ assign global variables to be used by the modules
● This is an optional file:
○ History: Before python 3.3, this file was a must
■ It marks a directory as a package"""

"""Init content
● It can be empty file, global things or whatever initialization
● On left the library init, on right backend init"""


# Importing a package with init
"""# Access package global vars
import library
print(library.lib_x)

from library.backend import backend_x
print(backend_x)"""


"""Importing sibling subpackage
● What if a subpackage wants to import from another subpackage branch?
● It is typically source of confusion / errors
● 2 approaches
○ Import the normal way in a proper way!
■ Use the full path from the top directory (root) in the package
■ But this is inflexible with directories changes: names or hierarchy
○ A more proper way: relative imports
■ Recall in command line: . refers to current dir and .. to parent dir
● Common mistake: trying to run a module with such import as script
○ It fails as it looks only in its directory"""

# Importing sibling subpackage (1)
# from library.backend import utilities1
# print(utilities1.sq_f1(10))

# from library.backend import utilities2
# print(utilities2.sq_f2(10))


"""Import * with packages
● We can also import * with packages
● But we must use __init__ file
● Specifically provide __all__: a list of modules names to imported with *
○ Only those in the list imported
○ Btw: it is also applicable for modules to force what is returned with *"""

# # Import * with packages
# print(dir())
# # ['__file__', '__name__', ...]
#
# from library import *
# print(dir())
# # ['__file__', '__name__', ..., 'backend', 'frontend']
#
# from library.backend import *
# print(dir())
# # ['__file__', '__name__', ..., 'backend', 'frontend', 'utilities']
#
# print(utilities.sq(5))
# # Again: avoid import *

# print(dir())
# # ['__file__', '__name__', ...]
#
# from library.frontend.web import *
# print(dir())
# # ['__file__', '__name__', ..., , 'f1', 'f2']
#
# f2()    # 2
#
# #NameError: name 'f3' is not defined
# #f3()

# print(__file__)
#
# __all__ = [
#         'backend',
#         'frontend',
#         ]


# Homework 2: Employees System as package
"""Employees System
● We will rearrange the modules as a packages
● Follow the structure in the screenshoot
● Use relative imports
● Script create and run: app = FrontendManager()"""

