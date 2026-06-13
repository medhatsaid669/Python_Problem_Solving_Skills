# Files
"""From Console to Files
● So far we read & write to console (the black screen / IDL screen)
○ IO stream from keyboard using input() and print()
● In practice, we want to save data in disk
not memory
● We should stream (read/write) to files
● Files can be used to store the data.
○ We use Files all the time
○ Data.txt, mostafa.jpg, python.exe
● Databases are an advanced
mechanism to store the data
○ rdbms, nosql
Img
src
File Structure & Types
● File is typically 3 parts
○ Header: metadata such as file name and its type
○ Data: for the content (encoded binary or text)
○ End of file (EOF): A special character to mark the file end
Binary file vs Text file
● Storing data as sequence of bytes rather than text (a..z, 0, 1, 2…#%...)
○ Not readable in editors
○ You need to read the content according to the way it was wrote.
Binary file vs Text file
● Text files
○ Limited to natural text
○ If some letter is corrupted, file is still opening, You even spot with eyes
○ Buy file size is bigger, and vary in size based on platform
● Binary files
○ Allow text and binary data
○ A minor corruption = probably failure to get back data
○ File size is smaller
File name and path
● Each file has a name + usually an extension
○ customers_info.txt (Name: customers_info and Extension: .txt)
○ data.tar.gz   (extension .tar.gz)
○ data (no extension)
● Directory (Folder): where the files exist
● Full Path: The whole path to access a file on the OS
○ /home/moustafa/workspaces/myfile.txt     [unix]
○ C:\\moustafa\\workspaces\\myfile.txt        [windows]
● Relative path
○ Relative to a current directory. Let’s say you are at /home/moustafa
■ Then on relative path is workspaces/myfile.txt    [or ./workspaces/myfile.txt]
○ Our code refers typically to relative, never to full path. [your code will be moved]
. and ..
● . refers to the current directory
● .. refers to the parent director
● Let’s say we have the following path
● code/cpp_skills/z/../../cpp_skills/z/y/mydir/x
○ .. means move up level so let’s simulate
○ code/cpp_skills/z/../../cpp_skills/z/y/mydir               [cancel z/..]
○ code/cpp_skills/../cpp_skills/z/y/mydir                     [cancel cpp_skills/..]
○ code/cpp_skills/z/y/mydir
● You should always be careful about path with spaces
○ In commands, in project workspaces, etc
○ Use “” for CL commands
Line Endings
● Not straightforward due to historical reasons
● Reading and writing may be different from an Operating system to another
○ Careful for moving files between windows and unix
○ Don’t be shocked if moved files and opened them to find them displayed differently!
● Info
○ Carriage Return (CR or \r)
○ Line Feed (LF or \n)
● In windows lines end uses \r\n
● In Unix and the newer Mac use \n
Character Encodings
● It is used to represent a repertoire of characters by some kind of encoding
system that assigns a number to each character for digital representation
● Common encodings:
○ ASCII: only 128 characters
○ UNICODE: designed to cover all the world's major living languages
■ UTF-8: Very popular
■ UTF-16: Much bigger, but less used in practice, so far
● Opening a file with a lower encoding capabilities, you will face problem
○ E.g. opening UTF-8 file using ASCII
● In python: The default encoding is platform dependent
○ So be careful. If you should use UTF-8, then pass it as parameter
UTF-8 File content"""


# Reading from files
path = 'data.txt'   # relative path (to running point)
file = open(path, 'r')  # r is the mode argument for reading
for line in file:   # iterate on files
    # notice, each line has \n in its end
    print(line, end='')
file.close()
"""
Observe printed as lines
hello
I am
mostafa
saad ibrahim
12345
"""

"""readline and readlines Methods
● Readlines method read all the file content!"""

# path = 'data.txt'   # relative path (to running point)
# file = open(path, 'r')
# string = file.readline()
#
# print(string)   # hello
#
# lines = file.readlines()
# print(lines)
# # ['I am\n', 'mostafa\n', '\n', '\n', 'saad ibrahim\n', '12345\n']
#
# #FileNotFoundError: [Errno 2] No such file or directory: 'notexist.txt'
# #open('notexist.txt', 'r')


"""Pythonic way
● The with statement guarantees for us the file close
○ Stick to use it. Many guys forget to close or wrongly handle the close with exceptions
○ Leaving too many files not closed may cause problems"""

# # pythonic way: use with statement
# # no need for file.close
#
# path = 'data.txt'
# lines = []
# with open(path, 'r') as file:
#     lines = file.readlines()
#
# #['hello\n', 'I am\n', 'mostafa\n', '\n', '\n', 'saad ibrahim\n', '12345\n']
# print(lines)


""".read().splitlines
● One of the very common ways to read the file content
● read() return whole file as a string, then you can do whatever
○ E.g. split based on commas"""

# path = 'data.txt'
# lines = []
# with open(path, 'r') as file:
#     lines = file.read().splitlines()
#
# # removing the end of line
# #['hello', 'I am', 'mostafa', '', '', 'saad ibrahim', '12345']
# print(lines)
#
# # you can then do whatever on list
# # strip, iterate in reversed way, etc

# # Encoding: UTF-8
# path = 'data_utf8.txt'
#
# with open(path, 'r', encoding='utf-8') as file:
#     lines = file.read().splitlines()
#     print(lines)
#     # ['Dürst. ˈmaʳkʊs', '∑∀x∈ℝ H₂ ði ὅ Σὲ ὅτ แผ่']
#
# # UnicodeDecodeError: 'ascii' codec can't decode
# # byte 0xc3 in position 1: ordinal not in range(128)
# with open(path, 'r', encoding='ASCII') as file:
#     lines = file.read().splitlines()
#     print(lines)


# Writing to files
"""Let’s Write!
● The write method doesn’t add new line. If you want it, you have to provide it
● If the file doesn’t exist, it will be created
○ Error if not possible: e.g. invalid path or security permission issues!
● By default, the old content will be overwritten"""

# path = 'output1.txt'
#
# with open(path, 'w') as file:
#     file.write('Hey')
#     file.write('Your name?')
#
# # let's run this code twice.
# # observe: file will be created if not exist


"""Printing lines
● Just add \n to force printing new lines"""

# path = 'output2.txt'
#
# lines = ['Hey', 'Your name?']
#
# # w for write but overwrite
# with open(path, 'w') as file:
#     for line in lines:
#         file.write(line + '\n')
# import os
# print('*' + os.linesep + '*')


"""Appending mode
● The append mode just keep adding things to the end of the file
○ Each run will add new content, not overwriting"""

# path = 'output3.txt'
#
# lines = ['Hey', 'Your name?']
#
# # a for write but append
# with open(path, 'a') as file:
#     for line in lines:
#         file.write(line + '\n')
#
# # let's run this code twice.

"""Read and Write
● In same with statement, we can open several files"""

# input_path = 'input.txt'
# output_path = 'output.txt'
#
# with open(input_path, 'r') as reader, \
#      open(output_path, 'w') as writer:
#     lines = reader.readlines()
#     writer.writelines(reversed(lines))
#     # writelines doesn't add \n

"""Fail if exists
● Sometimes, you want your code works well only if you are creating
○ Neither overwriting nor appending is expected"""


# path = 'output4.txt'
#
# lines = ['Hey', 'Your name?']
#
# # x: if exist = errio
# with open(path, 'x') as file:
#     for line in lines:
#         file.write(line + '\n')
#
# # let's run this code twice.
# # second time error:
# # FileExistsError: [Errno 17] File exists:
# #   'output4.txt'

"""Mix reading and writing
● We can mix reading/writing use r+ and w+ but this might be problematic
● There is also .seek functionalities 
○ You may study this later in file structures course 
os.linesep
● Import os
● os.linesep is the line separator (e.g. \n linux or \r\n windows)
● One might think to add \r\n during writing for windows
● However, behind the scene these conversions in reading/writing are done
○ Specifically for the normal text mode
■ E.g. when you print the line, it will always have \n regardless the platform
○ Note: in binary mode such conversions doesn’t occur
● Tip: Stick to \n in writing in text mode"""


# Pickle Module
"""Little about binary mode
● rb and wb modes are for reading and writing binary
○ It writes bytes (8 0s/1s).
● It is not so convenient, so we use modules that makes our life easier"""

# lst = [120, 255, 100]
#
# with open("data.binary", "wb") as writer:
#     binary_format = bytearray(lst)  # must be in range(0, 256)
#     writer.write(binary_format)
#     str_encoded = bytearray('abc', 'utf-8')
#     writer.write(str_encoded)
#
# with open("data.binary", "rb") as reader:
#     lst2 = list(reader.read())
#     print(lst2)     # [120, 255, 100, 97, 98, 99]
#     # a integer code is 97

"""Pickle module
● We can use to trivially create binary files of arbitrary objects
● We can also use it with our user-defined classes
○ Future: we can use special methods __setstate__, __getstate__ or __reduce__
■ E.g. Pickle don’t know how to handle your opened file!"""

# import pickle
# # Pickle serializes objects in a file.
# # Serialization is the process of converting an object into a stream of bytes
#
# data = (2021, '4444', ((7, 'wow'), [4, 5]))
# lst = [1, 251221, 30000]    # > 256
#
# with open("data.pickle", "wb") as pickle_file:
#     pickle.dump(data, pickle_file)
#     pickle.dump(lst, pickle_file)


"""Reading pickle file
● We can read in a trivial way
● Just remember rb mode
● Overall, easy read & write"""

# import pickle
#
# with open("data.pickle", "rb") as pickle_file:
#     data = pickle.load(pickle_file)
#     lst = pickle.load(pickle_file)
#     print(data)
#     print(lst)

"""
(2021, '4444', ((7, 'wow'), [4, 5]))
[1, 2, 3]
"""

# Observe: we read/write full thing
# Always overwrite
# Try to corrupt and read
"""What is wrong with pickle?
● Performance: Full file loading, which is not efficient for huge files
● Security: if a hacker replaced your pickle file (or give), his pickle file can 
contain commands to be run (e.g. os.system to delete your system files)
● If your class variables restructured ⇒ old pickle file is useless!
● No control on how to serialize things that might be saved in different ways
● It seralizes everything by default, which might be a problem (e.g. File object)
○ You need to be more careful or do workarounds
● __init__ isn’t called for objects creation
● Mainly a python binary file (dependent). Also as binary = Unreadable
● When to use? Personnel local projects. Security issue is very critical one
● There are other alternatives (shelve, json, etc). Each has pros/cons"""


# Shelve Module
"""Writing
● It is like-dictionary. Values are pickled / unpickled
● Behind the scene, like a database based on key-value (key is string)"""

# import shelve
#
# data = (2021, '4444', ((7, 'wow'), [4, 5]))
# lst = [1, 251221, 30000]    # > 256
#
# # By default, the underlying database
# # file is opened for reading and writing
# with shelve.open('data.shelve') as shelf:
#     # Think like a dictionary. Key/value
#     shelf['data'] = data
#     shelf['lst'] = lst
#     #Use strings as keys
#     #shelf[10] = 20 # 'int' object has no attribute 'encode'


"""Reading
● You can get keys similar to a dictionary
● Use it to access all or a specific keys
○ Only accessed values are loaded = memory efficient
○ Recall: Pickle loads all"""

# import shelve
#
# with shelve.open('data.shelve', 'r') as shelf:
#     for key in shelf.keys():
#         # load this specific value
#         print(key, shelf[key])
#
# """
# data (2021, '4444', ((7, 'wow'), [4, 5]))
# lst [1, 251221, 30000]# """

"""Updating shelve
● To update, just use the shelf[key] = value
○ Now these entries are updated/added"""

# import shelve
#
# data = (2021, '4444', ((7, 'wow'), [4, 5]))
# lst = [1, 251221, 30000]    # > 256
#
# # let's open the same file.
# # but we will use different keys
# with shelve.open('data.shelve') as shelf:
#     # Think like a dictionary. Key/value
#     shelf['data_cusomter'] = data
#     shelf['numbers'] = lst

# Mistake 1: Updating shelve the wrong way

# import shelve
#
# with shelve.open('data.shelve') as shelf:
#     shelf['numbers'].append(1111)
#
# with shelve.open('data.shelve', 'r') as shelf:
#     for key in shelf.keys():
#         print(key, shelf[key])
#
# """data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
# numbers [1, 251221, 30000]
# NO UPDATE
# Right way: get the list. update. assign"""

# # Mistake 2: Only new items are there!

# import shelve
#
# # let's read again
#
# with shelve.open('data.shelve', 'r') as shelf:
#     for key in shelf.keys():
#         # load this specific value
#         print(key, shelf[key])
#
# """data (2021, '4444', ((7, 'wow'), [4, 5]))
# lst [1, 251221, 30000]
# data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
# numbers [1, 251221, 30000]
#
# Surprise! Old keys exist
# - the open command in writing one, load the saved files
# - It doesn't remove them. just load. so old keys exist!"""


"""Deleting keys
● Explicitly delete the keys"""

# import shelve
#
# # let's open and delete
# with shelve.open('data.shelve') as shelf:
#     del shelf['data']   # make sure it exists!
#     del shelf['lst']
#
# with shelve.open('data.shelve', 'r') as shelf:
#     for key in shelf.keys():
#         # load this specific value
#         print(key, shelf[key])
#
# """data_cusomter (2021, '4444', ((7, 'wow'), [4, 5]))
# numbers [1, 251221, 30000]"""


"""● Explicitly delete the keys
Shelve Cons
● Shelve files also have the same security issue as pickle
● They might be slower: pickle and unpickle the values
● It shouldn’t be used with concurrent access
○ Don’t open the same file with 2 apps in same time, probably may fail
○ Databases are the way to go (You should study later)
● Might be convenient for your local apps
● Overall, very similar limitations to pickle, 
○ but more flexible access
○ It doesn’t load whole data in memory. 
○ Behind the scene, file-based like a database"""


# Files Homework

"""Problem #1: Max * Sum of a file
● Given a file of integers, each on a seperate line (data.txt)
● We need to read and postprocess them by converting all 
to positive
● After that: print their sum * their max
● Purpose: Mix reading the file with list comprehension
● Output for this file
○ 1200"""

# path = 'data.txt'
# with open(path) as file_reader:
#     lst = [abs(int(num)) for num in file_reader]
#     print(sum(lst) * max(lst))


"""Problem #2: Compute Differences V1
● Background
● As a udemy instructor, you would like to keep information about your 
competitors relevant courses
● When you access a course page, there are 2 numbers: total reviews / total 
users: We can use python to read URL and extract this information
■ Sometimes Udemy server rejects the request (stop crawlers)
Problem #2: Compute Differences V1
● You have the URLs of several courses. You developed a script that does:
○ Each 30 minutes, for each url it queries the udemy page and extract the 2 numbers
○ Then it appends a single line in the file as following 
■ date#r1 s1#r2 s2#r3 s3
■ (r1, s1) is the rating & total students for the first course and so on
■ Each entry is tab separated (viewed above with #)
Problem #2: Compute Differences V1
● Below is a sampled example of a file at the moment for 5 courses
○ E.g.on 18th Nov: the #of reviews of 2nd course are 62239 and total # of students 253423
Problem #2: Compute Differences V1
● Your task: we need to generate a new file with the following
● 1) A single line per day: the latest valid day in the file
● 2) Append extra value per course info: the total number of increased 
students from a day to another
● Assumptions
○ If a row is invalid, it will have the word NA as part of it
○ There will be no missing days in the middle, though it doesn’t matter!
○ The data otherwise will be correct
● Find in the section resources: Input and expected output files
○ Generate output file named: courses-output-current datatime
○ E.g. courses-output-2021-01-24 11:05:58.txt
Problem #2: Compute Differences V1
● Below is an output exampl"""

# from datetime import datetime
#
#
# def get_numbers(string):
#     items = string.split(' ')
#     return int(items[0]), int(items[1])
#
#
# def compute_increment(lst):
#     for row in range(1, len(lst)):
#         cur_lst = lst[row].split('\t')
#         cur_line = cur_lst[0]
#         for col in range(1, len(cur_lst)):
#             prev_lst = lst[row - 1].split('\t')
#             prev_rating, prev_reg = get_numbers(prev_lst[col])
#             cur_rating, cur_reg = get_numbers(cur_lst[col])
#
#             dif = max(0, cur_reg - prev_reg)
#             cur_line += '\t{} {} +{}'.format(cur_rating, cur_reg, dif)
#
#         lst[row] = cur_line
#     return lst
#
#
# def compress(path):
#     with open(path) as f:
#         lines = f.read().splitlines()
#
#     # iterate on the file to filter it
#     # skip all invalid lines
#     lines = [line for line in lines if 'NA' not in line]
#
#     # For valid lines; per day, keep only the last day
#     result = []
#     for idx, line in enumerate(lines):
#         day = line.split('\t')[0].split(' ')[0]
#
#         if idx == len(lines) - 1:   # last line in the file: add it
#             result.append(line)
#         else:                       # extract day of the next entry
#             next = lines[idx+1].split('\t')[0].split(' ')[0]
#             if day != next:         # different day: so I am last
#                 result.append(line)
#
#     # given a filtered file, compute the differences!
#     return compute_increment(result)
#
#
# if __name__ == '__main__':
#     input_path = 'courses.txt'
#
#     now = datetime.now()
#     cur_date = now.strftime("%Y-%m-%d %H:%M:%S")
#     output_path = f'courses-output-{cur_date}.txt'
#
#     lst = compress(input_path)
#
#     with open(output_path, 'w+') as f:
#         for line in lst:
#             f.write(line + '\n')


