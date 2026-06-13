"""List of lists
● In this section, we won’t learn new Python Syntax
● We will stress how nesting lists can create strong representation!
● A list of list of integer can create what we call a matrix
○ In C++ and Java it is called array. It has a fixed view
○ In python, we also have the numpy arrays
○ But we will focus here on using list of list to emulate a 2D array"""

# # Nesting lists
#
# lst0 = [1, 2, 3]
# lst1 = [4, 5, 6]
# lst2 = [7, 8, 9]
#
# print(lst2[1])  # 8
#
# list_of_lists = [lst0, lst1, lst2]
#
# print(list_of_lists)
# # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(list_of_lists[2]) # [7, 8, 9]
# print(list_of_lists[2][1]) # 8


# # Indexing (think 2D array)
#
# mostafa_grades = [50, 33, 40, 30]
# asmaa_grades = [35, 50, 44, 17]
# belal_grades = [30, 35, 50, 37]
# ziad_grades = [50, 35, 44, 22]
# safa_grades = [50, 44, 50, 30]
# ashraf_grades = [50, 36, 18, 50]
# mona_grades = [35, 30, 47, 16]
#
# grades = [mostafa_grades, asmaa_grades, belal_grades,
#           ziad_grades, safa_grades, ashraf_grades, mona_grades]
#
# print(grades[6])        # [35, 30_oop, 47, 16]
# print(grades[6][2])     # 47


"""Why is that useful?
● Write a program that reads grades for students
○ 100 students
○ 20 subjects
● How can we code that? 
○ Create 20 lists grade1[100], grade2[100], …..grade20[100]?
○ So impractical!
○ Just create a list of lists representing the grades of each subject!"""

# Creation

# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# print(grades[6])        # [35, 30_oop, 47, 16]
# print(grades[6][2])     # 47


# grades = [  [1, 2, 3, 4],
#             [5, 6],
#             [7, 8, 9, 10, 11],   # observe the last comma is ok
#         ]
#
# print(len(grades))        # 3: the list has 3 items: each is a list
# print(len(grades[0]), len(grades[1]), len(grades[2]))   # 4 2 5
#
# # lists are mutable: we can change content
# print(grades[1][0])     # 5
# grades[1][0] = 100
# print(grades[1][0])     # 100


# Shallow copy



# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# # similar to slicing: this creates a new list
# # BUT items are just assigned
# # we call this: shallow copy
# lst2 = grades.copy()
#
# print(id(grades[0]))
# print(id(lst2[0]))
#
# # later we learn how to make deep copy

#
# # Of other data structs
#
#
# lst = ['mostafa', 'saad', 'ibrahim']
# print(lst[2])       # ibrahim
# print(lst[2][1])    # b
#
# lst2 = [lst, (5, 7, 2)]
# print(lst2[0][2][1])    # b
# print(lst2[1][1])       # 7
#
# lst.sort()
# print(lst)
# # ['ibrahim', 'mostafa', 'saad']
#
#
# lst = [[[[1]]]]
# print(lst)                  # [[[[1]]]]
# print(lst[0])               # [[[1]]]
# print(lst[0][0])            # [[1]]
# print(lst[0][0][0])         # [1]
# print(lst[0][0][0][0])      # 1


# # Printing
#
#
# def print1(lst_of_lsts):
#     for lst in lst_of_lsts:
#         print(lst)
#
#
# grades = [  [1, 2, 3, 4],
#             [5, 6],
#             [7, 8, 9, 10, 11],
#         ]
#
# print1(grades)
# """
# [1, 2, 3, 4]
# [5, 6]
# [7, 8, 9, 10, 11]
# """



# def print1(lst_of_lsts):
#     for lst in lst_of_lsts:
#         print(*lst) # unpack: print without []
#
#
# grades = [  [1, 2, 3, 4],
#             [5, 6],
#             [7, 8, 9, 10, 11],
#         ]
#
# print1(grades)
# """
# 1 2 3 4
# 5 6
# 7 8 9 10 11
# """


# def print2(lst_of_lsts):
#     for i, lst in enumerate(lst_of_lsts):
#         for j, item in enumerate(lst):
#             print(item, end=' ')
#         print()
#
# def print3(lst_of_lsts):    # for educational purposes
#     for i in range(len(lst_of_lsts)):
#         for j in range(len(lst_of_lsts[i])):
#             print(lst_of_lsts[i][j], end=' ')
#         print()
#
#
# grades = [  [1, 2, 3, 4],
#             [5, 6],
#             [7, 8, 9, 10, 11],
#         ]
#
# print2(grades)
# """
# 1 2 3 4
# 5 6
# 7 8 9 10 11
# """

# # Reading
# # ● Read integer (rows) on a line
# # ● Then read N lines, each has a group of integers
#
#
#
# def print_lst_of_lsts(lst_of_lsts):
#     for lst in lst_of_lsts:
#         print(lst)
#
# def read_lst_of_lsts_ints():
#     rows = int(input())
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return lst_of_lsts
#
# lsts = read_lst_of_lsts_ints()
# print_lst_of_lsts(lsts)
#
# """
# 3
# 1 2 3 4
# 5 6
# 7 8 9 10 11
#
# [1, 2, 3, 4]
# [5, 6]
# [7, 8, 9, 10, 11]"""


# Row-major order processing

"""Average per row!
● Let’s compute the average per 
student
● This requires a row order 
processing, as each row is a 
student.
● Take a minute to pythonic it?"""


# # 7 students x 4 subjects
# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# def compute_row_avg(lst_of_lsts):
#     row_avg = []
#
#     for lst in lst_of_lsts:
#         sum = 0
#         for item in lst:
#             sum += item
#         row_avg.append(sum / len(lst))
#     return row_avg
#
# print(compute_row_avg(grades))
# # [38.25, 36.5, 38.0, 37.75, 43.5, 38.5, 32.0]
#
# # can we pythonic it?


# Average per row!

# # 7 students x 4 subjects
# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# def compute_row_avg(lst_of_lsts):
#     return [sum(lst) / len(lst) for lst in lst_of_lsts]
#
# print(compute_row_avg(grades))
# # [38.25, 36.5, 38.0, 37.75, 43.5, 38.5, 32.0]

# Column-major order processing

"""Average Cols!
● We have 4 subjects. How to 
compute the average per 
subject?
● This requires column-based 
processing
● Take 10 min to make it 
pythonic in a single line"""


# # 7 students x 4 subjects
# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# # assume equal columns / at least 1 seq
# def compute_col_avg(lst_of_lsts):
#     # let's iterate column-major order
#     col_avg = []
#
#     for j in range(len(lst_of_lsts[0])):
#         sum = 0
#         for i in range(len(lst_of_lsts)):
#             sum += lst_of_lsts[i][j]
#         col_avg.append(sum / len(lst_of_lsts))
#     return col_avg
#
# print(compute_col_avg(grades))
# #[42.85, 37.5, 41.85, 28.85]
#
# # can we pythonic it?

# The * unpacking


# grades = [  [1, 2, 3, 4],
#             [5, 6],
#             [7, 8, 9, 10, 11]
#         ]
#
# for a, b, c in zip(*grades):
#     print(a, b, c)
#
# """
# 1 5 7
# 2 6 8
#
# unpacking + zip Allowing us to iterate on coulmns
# """


# Let’s unzip


# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# # assume equal columns / at least 1 seq
# def compute_col_avg(lst_of_lsts):
#     col_avg = []
#
#     for tup in zip(*lst_of_lsts):
#         col_avg.append(sum(tup) / len(tup))
#     return col_avg
#
# print(compute_col_avg(grades))
# #[42.85, 37.5, 41.85, 28.85]


# # Let’s unzip
#
#
# grades = [  [50, 33, 40, 30],
#             [35, 50, 44, 17],
#             [30, 35, 50, 37],
#             [50, 35, 44, 22],
#             [50, 44, 50, 30],
#             [50, 36, 18, 50],
#             [35, 30, 47, 16]]
#
# # assume equal columns / at least 1 seq
# def compute_col_avg(lst_of_lsts):
#     return [sum(tup) / len(tup) for tup in zip(*lst_of_lsts) ]
#
# print(compute_col_avg(grades))
# #[42.85, 37.5, 41.85, 28.85]
#
# """Tip
# ● Want to iterate row by row?
# ○ for row in lists
# ● Want to iterate col by col?
# ○ for col in zip(*lists)
# ○ Remember it stops based on the shortest"""


# # Flatten a list
#
#
# lst_of_lists = [[1, 2], [3], [4, 5, 6, 7, 8], [9, 10, 11]]
#
# # Flatten a list: make all the items in a single list with no inner list
# # we can do that easily with list comprehension
#
# # without comprehension
# lst1 = []
# for lst in lst_of_lists:
#     for item in lst:
#         lst1.append(item)
#
# print(lst1)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# lst2 = [item for lst in lst_of_lists for item in lst]
# # same list!


# # Add int to all
#
#
# # without
# def add_value(lst_of_lists, value):
#     # add the value to each item
#     new_lst_of_lists = []
#     for lst in lst_of_lists:
#         new_lst = []
#         for item in lst:
#             new_lst.append(item + value)
#         new_lst_of_lists.append(new_lst)
#     return new_lst_of_lists
#
# lst_of_lists = [[1, 2], [3], [4, 5, 6, 7, 8], [9, 10, 11]]
#
# value = 10
# print(add_value(lst_of_lists, value))
# # [[11, 12], [13], [14, 15, 16, 17, 18], [19, 20, 21]]
#
# # we get the lst, then transform it to a new list
# lst_of_lists2 = [ [item+value for item in lst] for lst in lst_of_lists]
# print(lst_of_lists2)
# # [[11, 12], [13], [14, 15, 16, 17, 18], [19, 20, 21]]


# Generating Pairs

# we know with zip we can create iterator over item from each
# what if we want all pairs

# lst1 = [1, 2]
# lst2 = [10, 20, 30]
#
# # without comprehension
# lst_pairs1 = []
# for item1 in lst1:
#     for item2 in lst2:
#         lst_pairs1.append((item1, item2))
# print(lst_pairs1)   # [(1, 10), (1, 20), (1, 30_oop), (2, 10), (2, 20), (2, 30_oop)]
#
#
# lst_pairs2 = [(item1, item2) for item1 in lst1 for item2 in lst2 ]


# # Creating simple grids!
#
#
# # How to create an 3x4 grid of some value (e.g. 0)?
#
# rows, cols = 3, 4
# lst = [[0] * rows] * cols
# print(lst)
# # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# lst[0][0] = 2
# print(lst)
# # [[2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0]]  hmmm
# print(id(lst[0]), id(lst[1]))   # 0x111 0x111
# # * cols just append the same object
#
# lst = [ [0] * rows for i in range(cols) ]
# lst[0][0] = 2
# print(lst)
# # [[2, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#
# lst = [[x for x in range(rows)] for y in range(cols)]
# print(lst)
# # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
#
# # Useful: https://blog.finxter.com/python-list-of-lists
# # https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html


"""Matrix (grid) Structure
● In menu scenarios, we consider data in 2D structure where we have same 
number of columns
● We call it matrix, grid, 2D array
● Let’s see one of the code tricks that simplifies coding when necessary
 Position neighbours
● For a position (i, j)
○ Sometimes we use 4 neighbours
■ up, right, down, left
○ Sometimes we use 8 neighbours
■ up, right, down, left, up right, up left, down right, down left
■ Given (i, j), can u use a loop of 8 steps and print theses 4 or 8 positions, elegantly?
Hint
● Think in position (0, 0)
○ What is its relationships between the 8 neighbours?
○ Create 2 1D lists
○ In each list record the differences such that from any (i, j) we get neighbours?
Let’s find the relation
● What is change from (r, c) to the down?
○ (r+1, c): row is changed by +1, col is not changed
● What is change from (r, c) to the Left?
○ (r+1, c): row is not changed, col is changed by -1
● We can create 2 arrays to encode these +1/-1/0 changes between locations!
○ Some guys call it the direction array"""
#
# # 4 Neighbours
#
# def get_neibghours(i, j):
#     # {down, right, up, left};
#     di = [1, 0, -1, 0]
#     dj = [0, 1, 0, -1]
#
#     return [(i+di[d], j+dj[d]) for d in range(4)]
#
# print(get_neibghours(0, 0))
# # [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# print(get_neibghours(3, 6))
# # [(4, 6), (3, 7), (2, 6), (3, 5)]


# # 4 or 8 Neighbours
#
# def get_neibghours(i, j, cnt = 4):
#     # {d, r, u, l, ul, dr, ur, dl};
#     di = [1, 0, -1, 0, -1, 1, -1, 1]
#     dj = [0, 1, 0, -1, -1, 1, 1, -1]
#
#     return [(i+di[d], j+dj[d]) for d in range(cnt)]
#
#
# print(get_neibghours(0, 0))
# # [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# print(get_neibghours(3, 6))
# # [(4, 6), (3, 7), (2, 6), (3, 5)]
#
# print(get_neibghours(3, 6, 8))
# # [(4, 6), (3, 7), (2, 6), (3, 5), (2, 5), (4, 7), (2, 7), (4, 5)]



"""2D and 1D Flatten Relationships
● Let’s say we have this 3x4 matrix
● We can flatten to
○ flst = [8, 16, 9, 52, 3, 15, 27, 6, 14, 25, 2, 10]
● We want to learn the indices relations
○ lst[0][3] = 52  ⇒ is same as  ⇒ flst[3]
○ lst[1][0] =   3  ⇒ is same as  ⇒ flst[4]
○ lst[1][2] = 27  ⇒ is same as  ⇒ flst[6]
● For an NxM grid:
○ Given index (i, j), convert to its corresponding 1D flat index? E.g. (1, 0) ⇒ 4
○ Given index i in 1D flat index, convert to its corresponding 2D (i, j)? 4 ⇒ (1, 0)"""

"""3 Equations
● flst = [8, 16, 9, 52, 3, 15, 27, 6, 14, 25, 2, 10]
● To convert from (i, j) in matrix to 1D array
○ i * COLS + j
○ (1, 2) ⇒ 1 * 4 + 2 = 6
● To convert from index in 1D array to (i, j) in matrix
○ i = idx//COLS           j = idx%COLS
○ Idx = 6      ⇒      (6//4, 6%4)   ⇒   (1, 2)
○ Why? Idx = i * COLS + j
■ Idx // COLS   = (i * COLS + j)//COLS   = i + 0, as j < COLS
■ Idx % COLS = (i * COLS + j)%COLS = 0 + j, as j < COLS and (i*COLS)%COLS = 0"""


# def from2d_to_1d(cols, i, j):
#     return i * cols + j
#
#
# def from1d_to_2d(cols, idx):
#     return idx//cols, idx % cols
#
#
# def list_relations(rows = 3, cols = 5):
#     idx = 0
#     for r in range(rows):
#         for c in range(cols):
#             print(f'({r}, {c}) ==> {idx}')
#
#             assert (r, c) == from1d_to_2d(cols, idx)
#             assert idx == from2d_to_1d(cols, r, c)
#
#             idx += 1
#
# list_relations(3, 5)


"""Practice: Find the mountains
● Read a matrix. Print all positions that are a mountain. 
○ Position (r,c) is mountain if its value > 8 neighbours
● Input
○ 3
○ 8 6  1
○ 3 2  9
○ 1 6  4
● Output
○ 0 0                (8 > 6, 3, 2)
○ 1 2                (9 > 1, 2, 5, 4, 6)
● Give a trial"""

#
# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# def is_within_grid(r, c, rows, cols):
#     return 0 <= r < rows and 0 <= c < cols
#
# def get_neibghours(i, j, rows, cols, cnt = 8):
#     # {d, r, u, l, ul, dr, ur, dl};
#     di = [1, 0, -1, 0, -1, 1, -1, 1]
#     dj = [0, 1, 0, -1, -1, 1, 1, -1]
#
#     # Filter the positions that are outside the grid
#     #return [(i+di[d], j+dj[d]) for d in range(cnt)
#         # if is_within_grid(i+di[d], j+dj[d], rows, cols)]
#     return [(r, c) for d in range(cnt)
#                 if is_within_grid(r := i + di[d], c:= j + dj[d], rows, cols)]
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     if rows == cols == 1:
#         print(0, 0)
#         exit(0)
#
#     for r in range(rows):
#         for c in range(cols):
#             positions = get_neibghours(r, c, rows, cols)
#             mx = max([matrix[i][j] for i, j in positions])
#             if matrix[r][c] > mx:
#                 print(r, c)
#
# # test a matrix with single value or single row

# Nested Lists Homework 1

"""Problem #1: Swap 2 columns
● Read an integer matrix
○ By that I mean read a line: integer N, then N rows of integers (all will have same number of 
columns).
● Then read 2 indices of columns. 
○ Swap the 2 columns together. Print as below
● Input:
○ 3
○ 8   16  9    52
○ 3   15  27  6
○ 14 25  2    10
○ 0 3                          [swap col0 and col 1]
● Output
○ [[52, 16, 9, 8], [6, 15, 27, 3], [10, 25, 2, 14]]"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#     c1, c2 = map(int, input().split())
#
#     for row in matrix:  # observe change in row change original matrix
#         row[c1], row[c2] = row[c2], row[c1]
#
#     print(matrix)

"""Problem #2: Triangular matrix
● Read an integer matrix (squared)
● Print the sum of the lower triangle matrix and the upper triangle.
● Input
○ 3
○ 8   16   9
○ 3   15   27
○ 14 25   29
● Output
○ 94              (8+15+29+3+25+14)
○ 104            (8+15+29+16+27+9)"""
#
# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     upper, lower = 0, 0
#     for idx, row in enumerate(matrix):
#         lower += sum(row[:idx+1])
#         upper += sum(row[idx:])
#
#     print(lower)
#     print(upper)

"""Problem #3: Filter empty rows
● Read a list of list of integers. First line is # of rows (N), then N lines
● AFTER reading the list, filter out all empty rows using list comprehension 
● Input
○ 5
○ 1 2 3
○
○ 4 5
○
○ 6
● Output (print the new list of lists
○ [[1, 2, 3], [4, 5], [6]]"""
#
# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     matrix = [row for row in matrix if row]
#     # if row is same as if len(row) > 0
#     print(matrix)


"""Problem #4: Max value
● Read an integer matrix
● Find the (i, j) position of the maximum value in the matrix. 
○ If there are several ones, find the last occurance
● Input:
○ 3
○ 1 5 1 10
○ 2 10 3 4
○ 1 10 10 7
● Output
○ Max value at position (2, 2) with value = 10"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     mx, mx_r, mx_c = None, None, None
#
#     for row_idx, row in enumerate(matrix):
#         for col_idx, value in enumerate(row):
#             if mx is None or mx <= value:       # <= for last occurrence. < for first occurrence
#                 mx, mx_r, mx_c = value, row_idx, col_idx
#
#     print(f'Max value at position {mx_r, mx_c} with value = {mx}')


"""Problem #5: Special print
● Read an integer matrix. Print the following 4 values
○ The sum of the last row & the sum of the last column
○ The sum of the left diagonal & the sum of the right diagonal
● Input:
○ 3
○ 8   16  9    52
○ 3   15  27  6
○ 14 25  2    10
● Output
○ 51 68                 [14+25+2+10 51 the last row          52+6+10 = 68 the last column
○ 25 104               [8+15+2=25 the left diagonal          52+27+25 = 104 the right diagonal"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     # for each case list the needed indices
#     # use list comprehension to extract the target position
#
#     last_row = sum(matrix[-1])
#     last_col = sum([row[-1] for row in matrix])
#     left_diag = sum([row[idx] for idx, row in enumerate(matrix)])
#     # -(idx+1) ==> -1, -2, -3, etc till #rows
#     right_diag = sum([row[-(idx + 1)] for idx, row in enumerate(matrix)])
#
#     print(last_row, last_col)
#     print(left_diag, right_diag)


"""Problem #6: Value in first column
● Read an integer matrix, then read a target integer value
● Find the first column that contains a given
○ If not available print: Not Found 
● Input:
○ 3
○ 8   16  9    52
○ 3   15  15  6
○ 14 25  2    10
○ 15
● Output
○ found in col 1
● Input:
○ 3
○ 8   16  9    52
○ 3   15  15  6
○ 14 25  2    10
○ 15
● Output
○ found in col 1"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#     target_val = int(input())
#
#     for idx, col in enumerate(zip(*matrix)):
#         if target_val in col:
#             print(f'found in col {idx}')
#             break
#     else:
#         print('Not found')


"""Problem #1: Implement our zip: v1"""

# class OurZip:
#     # receive varying numbers of iterables: assume only list, tuple, string
#     def __init__(self, *iterables):
#         self.iterables = iterables
#         self.cur_col_idx = 0
#
#     def has_next(self):
#         for seq in self.iterables:
#             if self.cur_col_idx >= len(seq):
#                 return False
#         return True
#
#     def get_next(self):
#         # append is slow. we know the target size
#         ret = [0] * len(self.iterables)
#         for idx, seq in enumerate(self.iterables):
#             ret[idx] =  self.iterables[idx][self.cur_col_idx]
#         self.cur_col_idx += 1
#
#         return tuple(ret)
#
# if __name__ == '__main__':
#     z = OurZip(list(range(10, 15)), list(range(100)), 'Mostafa')
#     while z.has_next():
#         print(z.get_next())
"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
"""

"""Problem #2: Implement our zip: v2
● In this variant, we will keep going up 
to the longest sequence. Replace 
missing values with None"""

# class OurZip:
#     # receive varying numbers of  iterables: assume only list, tuple, string
#     def __init__(self, *iterables):
#         self.iterables = iterables
#         self.cur_col_idx = 0
#
#     def has_next(self):
#         # if there is at least one: use it
#         for seq in self.iterables:
#             if self.cur_col_idx < len(seq):
#                 return True
#         return False
#
#     def get_next(self):
#         ret = [0] * len(self.iterables)
#
#         for idx, seq in enumerate(self.iterables):
#             if self.cur_col_idx < len(self.iterables[idx]):
#                 ret[idx] = self.iterables[idx][self.cur_col_idx]
#             else:
#                 ret[idx] = None
#         self.cur_col_idx += 1
#
#         return tuple(ret)
#
#
#
# if __name__ == '__main__':
#
#     z = OurZip(list(range(10, 15)),
#                list(range(10)), 'Mostafa')
#     while z.has_next():
#         print(z.get_next())
"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
(None, 5, 'f')
(None, 6, 'a')
(None, 7, None)
(None, 8, None)
(None, 9, None)
"""


"""Problem #3: How many primes
● Read a matrix. In next line, read integer Q, for Q queries. 
○ In the next lines: read queries: sr sj r c
○ Each queries is a grid with top left (sr, sc) and #rows & #cols 
○ For each query, print how many prime numbers in the requested sub-matrix.
● Input ⇒ Output
○ 3
○ 8 2 9 5
○ 3 2 27 6
○ 7 8 29 22
○ 2                   
○ 1 0 2 2          
○ 0 1  2 3         
⇒ 2 queries
⇒ 3 (primes 3, 2, 7 in rectangle (0, 1) (2, 1) )
⇒ 3 (primes 2, 5, 2 in rectangle (0, 1)  (1, 3) )"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# def is_prime(num):
#     if num <= 1:
#         return 0
#
#     for i in range(2, num):
#         if num % i == 0:
#             return 0
#
#     return 1
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#
#     # replace each value with 1 if prime 0 otherwise
#     # then with every query: we don't have to keep computing the slow is-prime!
#     is_prime_matrix = [[is_prime(value) for value in row] for row in matrix]
#
#     q = int(input())    # queries
#     while q > 0:
#         total_primes = 0
#         sr, sc, nr, nc = map(int, input().split())
#         # iterate on rows: slice the range and sum it
#         for r in range(sr, sr + nr):
#             total_primes += sum(is_prime_matrix[r][sc:sc + nc])
#         print(total_primes)
#         q -= 1
#
# # This code can be much more efficient, but beyond the scope
# # E.g. using image integral preprocessing, we can compute any 2D range in O(1)


"""Problem #4: Greedy Robot
● Read an integer matrix (all distinct values)
● A robot starts at cell (0, 0). 
● Take the value in the current cell and moves. 
○ It can move only one step to either: Right, Bottom or the diagonal. 
○ It always selects the destination cell that has maximum value. 
● Print the total values the robot collects
3
1 2 3
4 5 6
7 8 9
⇒ (0, 0) (1, 1),  (2, 2) ⇒ 15
3
1 2 3
5 4 9
7 6 8
⇒ (0,0)⇒(1,0)⇒(2,0)⇒(2,1)⇒(2,2)
⇒27
2
1 2 3 4 5
6 7 8 9 10
⇒ 35
"""

# def read_matrix():
#     # read and return: rows, cols, list of lists
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = list(map(int, input().split()))
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
#
# def is_within_grid(r, c, rows, cols):
#     return 0 <= r < rows and 0 <= c < cols
#
#
# def get_neibghours(i, j, rows, cols):
#     dir = [(1, 0), (0, 1), (1, 1)]
#     return [(r, c) for di, dj in dir
#             if is_within_grid(r := i + di, c:= j + dj, rows, cols)]
#
#
# def argmax(lst):
#     return lst.index(max(lst))
#
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix()
#     r, c, total_sum = 0, 0, 0
#
#     while True:
#         total_sum += matrix[r][c]
#         if not (positions := get_neibghours(r, c, rows, cols)):
#             break   # get the list: if empty, break
#         values = [matrix[i][j] for i, j in positions]
#         r, c = positions[argmax(values)]
#
#     print(total_sum)


"""Problem #5: Active Robot
● Read a line that starts with integer values N M
○ It represents a grid NxM, where a robot starts at (0, 0)
● Then the remaining of the line is several commands
● Each command is 2 values
○ Directio: up, right, down, left
○ Steps: the number of steps to take in the direction. Steps [1, 1000000000]
○ If the robot hits the wall during the move, it circulates in the matrix.
○ For every command, print where is the robot now
● Input
○ 3 4     
● Output
right 1          down 2         left 2        up 3
○ (0, 1)      (2,1)       (2, 3)     (2, 3)"""


# if __name__ == '__main__':
#     rows, cols, *commands = input().split()
#     rows, cols = int(rows), int(cols)
#
#     # up, right, down, left
#     rd = [-1, 0, 1, 0]
#     cd = [0, 1, 0, -1]
#     r, c = 0, 0
#
#     while commands:
#         dir, steps, *commands = commands
#         dir = ['up', 'right', 'down', 'left'].index(dir)    # index of direction
#         steps = int(steps)
#         # as we circulate, then the % can help removing unnecessary cycles, regardless how big
#         r = (r + rd[dir] * steps) % rows
#         c = (c + cd[dir] * steps) % cols
#         print(r, c)


"""Problem #6: Matrix pretty print
● Read a matrix of strings (no spaces, same # of columns)
● We would to pretty print the matrix such that
○ Each column is left justified based on the length of the longest string in the column
○ Seperate each 2 columns with ‘ # ‘
○ You will need to study: Python String ljust() Method
● Given the matrix, transform it to a new
list of  strings (one per row)
Using 2 lines of code
Hint: Use comprehension lists """

# def read_matrix_strings():
#     rows = int(input())
#     assert rows > 0
#     lst_of_lsts = [0] * rows
#
#     for row in range(rows):
#         lst_of_lsts[row] = input().split()
#     return rows, len(lst_of_lsts[0]), lst_of_lsts
#
# if __name__ == '__main__':
#     rows, cols, matrix = read_matrix_strings()
#
#     # for each column, get all words, compute their word length, get max of all
#     width_per_col = [max([len(word) for word in col]) for col in zip(*matrix)]
#
#     # for each word in a row, ljust based on its column max width
#     # then join all of them by ' # '
#     # logic: for every row => transform the row and merge
#     matrix = [' # '.join([word.ljust(width_per_col[idx]) for idx, word in enumerate(row)]) for row in matrix]
#     print('\n'.join(matrix))    # print rows newline seperated


"""Problem #7: Flatten 3D lists
● Read a line that starts with 3 numbers: DEPTH, ROWS, COLS the 
dimensions of 3D list
○ List of list of list
● Then the remaining of the line will be either:
○ 1 d r c ( means convert from 3D to 1D)   or
○ 2 idx   (means convert from idx to 3D)
○ Can you generalize to higher dimensions? E.g. 6D
● Input ⇒ Outputs
○ 3 4 5    1     1 0 0   ⇒ 20
○ 3 4 5    2     20       
⇒ 1 0 0
○ 3 4 5    1     1 1 1   ⇒ 26
○ 3 4 5    1     2 3 2   ⇒ 57
○ 3 4 5    1     2 0 0   ⇒ 40
○ 3 4 5    2     59       
⇒ 2 3 4"""


# def list_relations(depth = 3, rows = 4, cols = 5):
#     idx = 0
#     for d in range(depth):
#         for r in range(rows):
#             for c in range(cols):
#                 print(f'({d}, {r}, {c}) ==> {idx}')
#                 idx += 1
#
# if __name__ == '__main__':
#     depth, rows, cols, type, *remain = map(int, input().split())
#     db = rows * cols    # a single depth block
#     rb = cols           # a single r block (cols value)
#     cb = 1              # a single column block (single value)
#
#     if type == 1:
#         d, r, c = remain
#         idx = d * db + r * rb + c * cb
#         print(idx)
#     else:
#         idx = remain[0]
#         # r * Rb + c * 1 < Db
#         d = idx // db
#         # Remove d part, then extract r
#         r = (idx % db) // rb
#         c = (idx % db) % rb
#         print(d, r, c)


"""Application: NxN tic-tac-toe
● In this challenge, you will implement tic-tac-toe game
● However, the board can be an integer N >= 3
○ Same rules applied. Just bigger
● Read integer N for the dimension of tic-tac-toe.
● Then run a game of 2 users who keep playing till one of them wins or tie.
○ Assume user input is integer. Verify the cell location.
○ Make sure to test scenarios for row, col, left diagonal and right diagonal winning + tie
● Follow the next printing style
● Tip: Don’t write many ugly loops to verify the board
○ Use direction array thoughts to write short elegant code
○ Hard for you? Code it anyway"""

# def find_winner(board):
#     n = len(board)
    """
    We can write length code to verify N row, N every col and 2 diagonals
    Notice: the behaviour of all of them is SAME
        E.g. We have some starting point (e.g. 0 0) and we need to verify its row
    We can use a direction-array style to write an elegant code
    We will create a single list with the 2N+2 needed verifications
    For every verification we need 4 values:
        The starting point (r, c): we need startings for N rows, N cols, 2 Diagonals
        The direction to move in it for N steps

    For example, for the starting (0, 0)
        To verify its row, we need direction (1, 0)
        To verify its col, we need direction (0, 1)
        To verify its diagonal, we need direction (1, 1)
    To verify the right diagonal: we start from the last cell in first row (0, n-1) and moves (1, -1)
        1 means move to next row. -1 means move to the previous column

    Once done: we iterate over all such start/direction. 
        Loop n times to verify they all same play symbol 
    """
#     start_dir = [(r, 0, 0, 1) for r in range(n)]  # Add N row starting points/dir
#     start_dir.extend([(0, c, 1, 0) for c in range(n)])  # Add N col starting points/dir
#     start_dir.append((0, 0, 1, 1))  # Add left diagonal
#     start_dir.append((0, n - 1, 1, -1))  # Add right diagonal
#
#     for r, c, dr, dc in start_dir:
#         player = board[r][c]
#         if player == ' ':
#             continue
#         is_win = True
#         for s in range(n):
#             if board[r][c] != player:
#                 is_win = False
#                 break
#             r, c = r + dr, c + dc  # move to next position
#         if is_win:
#             return player
#     return None
#
#
# if __name__ == '__main__':
#     n = int(input('Enter grid size: '))
#     assert n >= 3
#     board = [[' '] * n for i in range(n)]
#     symbols = 'XO'
#     steps, turn = 0, 0
#
#     while True:
#         if steps == n * n:
#             print('Tie!')
#             break
#         r, c = map(int, input(f'Player {symbols[turn]}, make a move: ').split())
#         r, c = r - 1, c - 1
#         if not 0 <= r < n or not 0 <= c < n or board[r][c] != ' ':
#             print('Invalid location. Try again')
#             continue
#         board[r][c] = symbols[turn]
#         print('\n'.join(['|'.join(row) for row in board]))
#
#         if (winner := find_winner(board)) is not None:  # without parentheses, walrus is assigned boolean!
#             print(f'Play {winner} won!')
#             break
#         turn = 1 - turn  # switch 0 to 1 and 1 to 0
#         steps += 1

"""
3
1 1
1 2
2 2
1 3
3 3
X|O|O
 |X| 
 | |X
Play X won!

3
1 1
1 2
2 1
2 2
3 3
3 2
X|O| 
X|O| 
 |O|X
Play O won!

3
1 3
1 1
2 2
3 3
3 1
O| |X
 |X| 
X| |O
Play X won!

3
1 1
1 3
1 2
2 2
3 2
2 1
2 3
3 3
3 1
X|X|O
O|O|X
X|X|O
Tie!
"""



