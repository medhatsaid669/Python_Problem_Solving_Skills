"""Practice: Reverse in place
● Read a line of N integers
● Recall: list.reverse()
○ It performs in-place reverse for the list
○ In-place: Change the current list, don’t create another one
● We will implement our own reverse function in an iterative style
● def our_reverse(list)
○ It doesn’t have a return
● Stop and think!"""

# def our_reverse(lst):
#     for pos1 in range(len(lst) // 2):
#         pos2 = len(lst) - pos1 - 1  # the opposite in the list
#         lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
#
#
# def main():
#     lst = list(map(int, input().split()))
#
#     our_reverse(lst)
#
#     print(lst)
#
#
# main()


"""Practice: Find pair values of maximum sum
● Read a line of N integers (N > 1)
● Find a pair of indices whose values’ sum is maximum
● Input ⇒ output
○ 2 15 10 3 50           
⇒ 65         (from 50 + 15)
● Stop the video and code it
○ Do it with nested loops
○ Can you do with a linear loop?
■ e.g. not nested but can be several different 1 loop"""


# def pair_maxsum_slow(lst):
#     pos1, pos2 = 0, 1
#
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
#                 pos1, pos2 = i, j
#
#     return pos1, pos2
#
# def main():
#     lst = list(map(int, input().split()))
#     assert len(lst) > 1
#
#     pos1, pos2 = pair_maxsum_slow(lst)
#
#     print('idx1', pos1, 'value', lst[pos1])
#     print('idx2', pos2, 'value', lst[pos2])
#     print('Max sum', lst[pos1] + lst[pos2])
#
# main()


"""Practice: Find the index of the top 2 maximum values
● Read a line of N integers (all on same line)
● Find the index of the the maximum and 2nd maximum values
○ If there are more than an answer: find the first match
● Input: 
○ 10 20 3 30 7
■ idx1 3 value 30
■ idx2 1 value 20
○ 10 20 30 25 30 17
■ idx1 2 value 30
■ idx2 4 value 30
● Stop the video and code it"""


# def top2_argmax_v2(lst):
#     # Given a list: return the indices of the first and second maximum
#     if len(lst) < 2:
#         return None, None
#
#     # Use the first 2 positions for the top 2 max
#     max1_pos, max2_pos = 0, 1
#     if lst[max1_pos] < lst[max2_pos]:
#         max1_pos, max2_pos = 1, 0
#
#     # Iterate and update the indices based on current element if bigger
#     for cur_pos in range(2, len(lst)):
#         if lst[max1_pos] < lst[cur_pos]:
#             max1_pos, max2_pos = cur_pos, max1_pos
#         elif lst[max2_pos] < lst[cur_pos]:
#             max2_pos = cur_pos
#
#     return max1_pos, max2_pos
#
#
# def main():
#     lst = list(map(int, input().split()))
#
#     max1_pos, max2_pos = top2_argmax_v2(lst)
#
#     if max1_pos is not None:
#         print('idx1', max1_pos, 'value', lst[max1_pos])
#         print('idx2', max2_pos, 'value', lst[max2_pos])
#
#
#
# main()


"""Practice: Find most frequent number
● Read a line of N integers. Each integer is 0 <= value <= 150
● Find the value that repeated the most number of times.
○ If there are many solutions: find the smallest value
● Input ⇒ output
○ 1 2 1 3 1 5 5 ⇒ Value 1 repeated 3
■ Observe:
■ 1 repeated 3 times: the largest
■ 2 repeated 1 time
■ 5 repeated 2 times
○ 5 5 5 5 2 3 3 3 3 ⇒ Value 3 repeated 4
● Stop video and think
○ Do it with nested loops
○ Can you do it with a single loop?"""


# def most_frequent_fast(lst):
#     # it actually work well. max here is flexible
#     freq_lst  = [0] * (150+1)
#
#     for value in lst:
#         freq_lst[value] += 1
#
#     # argmax - Observe: the tie is also handled!
#     most_value = freq_lst.index(max(freq_lst))
#
#     return most_value, freq_lst[most_value]
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#     most_value, frequency = most_frequent_fast(lst)
#     print('Value', most_value, 'repeated', frequency)


"""Homework 1: Is increasing array?
● Read a line of N integers
● Print YES if the list is increasing. 
○ List is increasing if every element is >= the previous number
● Inputs  
○ 1 2 2 5     
⇒ YES
○ 1 0 7 8 9  ⇒ NO   [0 is < 1, the previous number]
○-10 10      
⇒ YES """

# def is_increasing(lst):
#     # compare every element to the last one
#     for pos in range(1, len(lst)):
#         if lst[pos] < lst[pos-1]:
#             return False
#     return True
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     status = is_increasing(lst)
#
#     if status:
#         print('YES')
#     else:
#         print('NO')



# can we make it more pythonic without explicit loop

# def is_increasing(lst):
#     # let's make it more pythonic
#     # we create a list that allows us to compare element by element
#
#     last_item = lst[len(lst) - 1]
#     shifted_lst = lst.copy()
#     shifted_lst.pop(0)  # we don't compare first with previous
#     shifted_lst.append(last_item)
#
#     # for input      [10 20 30_oop 40]
#     # shifted_lst is [20 30_oop 40 40]
#
#     print(lst)
#     print(shifted_lst)
#
#     # You will learn this style soon. Lecture video is not fully correct
#     return all(lst[idx] <= shifted_lst[idx] for idx in range(len(lst)))
#
#
# def is_increasing_v2(lst):
#     # We can write above logic in a single line too.
#     # But you did not learn zip yet
#
#     return all(x < y for x, y in zip(lst, lst[1:]))
#
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     status = is_increasing(lst)
#     print(status)
#
#     if status:
#         print('YES')
#     else:
#         print('NO')


"""Homework 2: Replace MinMax
● Read a line of N integers
● Print the numbers after doing the following operations:
○ Find minimum number in these numbers.
○ Find maximum number in these numbers.
○ Replace each minimum number with maximum number and Vise Versa.
● Input ⇒ Output
○ 4 1 3 10 8  10 10 ⇒  4 10 3 1 8 1 1 
● Create function 
def 
replace_min_max_inplace(lst):
○ The function doesn’t return a list. It makes in-place modification"""


# def replace_min_max_inplace(lst):
#     mn = min(lst)
#     mx = max(lst)
#
#     for idx, item in enumerate(lst):
#         if item == mn:
#             lst[idx] = mx
#         elif item == mx:
#             lst[idx] = mn
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     replace_min_max_inplace(lst)
#     print(lst)


"""Homework 3: Search for a number
● Read a line of N integers, where 0 <= value in a list <= 500
● Then read a line of Q integer, each one is a query: [0, 500]
○ For each integer, print the index of the last occurance in the list or -1 if it doesn’t exist
● Output Explanation
○ 4      [7 exists in 2 positions  (2 and 4). The last is 4)
○-1     [9 doesn’t exist)
○ 1      [2 exists only in position 1] 
● Do it first in 2 loops
● Can you do it in 1 loop using the Frequency Trick?"""


# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#     queries = list(map(int, input().split()))
#
#     # As values are 0-500, we can make list of 501 mark the last value in it
#     # Then we answer the queries directly
#
#     last_value_pos = [-1] * 501     # 501 values that are -1 (default for not exist)
#
#     # mark in the list where the item appear
#     # as we process in order: the last occurrence overwrite previous values
#     for idx, item in enumerate(lst):
#         last_value_pos[item] = idx
#
#     for q in queries:
#         assert q < len(last_value_pos)
#         print('Query', q, 'answer', last_value_pos[q])
#
# # Linear time solution! O(N)


"""Homework 4: Unique Numbers of unordered 
● Read a line of N integers. They are not ordered.
● Print the unique list of the numbers, but preserve the given order
● Input:    1 5 5 2 5 7 2 3 3 3 5 2 7
● Output: 1 5 2 7 3
○ Observe: input is not sorted list
○ Observe: output preserves the original order: e.g. 5 appears before 2"""


# def uniqe_not_sorted_lst(lst):
#     lst_ret = []
#
#     for item in lst:
#         if item not in lst_ret:
#             lst_ret.append(item)
#
#     return lst_ret
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     lst = uniqe_not_sorted_lst(lst)
#     print(lst)


"""Homework 5: Unique Numbers of ordered 
● Read a line of N integers. They are ordered.
○ Previous solution can work. But can we make a faster code?
● Print the unique list of the numbers, but preserve the given order
● Input:    1 1 2 2 2 5 6 6 7 8 9 9
● Output: 1 2 5 6 7 8 9
○ Observe: input is sorted list"""


# def uniqe_not_sorted_lst(lst):
#     lst_ret = []
#
#     for idx, item in enumerate(lst):
#         # In a sorted list: if the previous number != me ==> I am a new one
#         if idx == 0 or lst[idx] != lst[idx-1]:
#             lst_ret.append(item)
#
#     return lst_ret
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     lst = uniqe_not_sorted_lst(lst)
#     print(lst)


"""Homework 6: Smallest pair
● Read a line of N integers.
● Print the smallest possible result of A[i] + A[j] + j - i
○ where 0  ≤  i < j  ≤  N-1.
● Input ⇒ Output
○ 20 1 9 4    ⇒     7"""


# def smallest_pair(lst):
#     # calculate Ai+Aj+j-i for every pair (i,j)
#
#     ans = None
#     for pos1, item1 in enumerate(lst):
#         for pos2 in range(pos1+1, len(lst)):
#             item2 = lst[pos2]
#
#             cur = item1 + item2 + pos2 - pos1
#
#             if ans is None or ans > cur:
#                 ans = cur
#     return ans
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     ans = smallest_pair(lst)
#     print(ans)


"""Homework 7: Find the 3 minimum values
● Read a line of N integers.
● Find the 3 lowest numbers. If there are less than 3, just consider them.
○ Don’t change the list content or create equivalent memory (e.g. .copy)
○ Don’t iterate on the list more than once
● Input ⇒ Output
○ 4 1 3 10 8  ⇒  1 3 4
○ 7 9 -2         
○ 1 -5            
⇒ -2 7 9 
⇒ -5 1           [< 3 nums: just use them, print sorted]"""


# def find_3_min(lst):
#     mn_lst = []
#     # the idea: keep aading to this list
#     # sort and remove the 4th item
#     # then the list always have the min 3 numbers
#
#     for item in lst:
#         mn_lst.append(item)
#
#         if len(mn_lst) > 3:
#             mn_lst.sort()
#             mn_lst.pop()
#
#     mn_lst.sort()
#     return mn_lst
#
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     mn_lst = find_3_min(lst)
#     print(mn_lst)


"""Homework 1: Find most frequent number
● Read a line of N integers. Each integer is -500 <= value <= 270
● Find the value that repeated the most number of times.
○ If there are many solutions: find the smallest value
● Input ⇒ output
○-1 2 -1 3 -1 5 5 ⇒ Value -1 repeated 3"""


# def most_frequent_fast(lst):
#     # With simple change we can use the practice code
#     # we will shift all the data to start from ZERO (so we can index normally)
#     # then later undo the effect
#     # to do that: just subtract the minimum
#     # e.g. if input is -10 20 -2 9 20
#     # the min is -10
#     # subtract it from all: 0 30_oop 8 19 30_oop
#     # Find max 30_oop. Undo with -10 ==> 20
#     mn, mx = min(lst), max(lst)
#     freq_lst  = [0] * (mx - mn +1)
#
#     for value in lst:
#         print(value - mn)
#         freq_lst[value - mn] += 1
#
#     # argmax - Observe: the tie is also handled!
#     most_value = freq_lst.index(max(freq_lst))
#
#     return most_value + mn, freq_lst[most_value]
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#     most_value, frequency = most_frequent_fast(lst)
#     print('Value', most_value, 'repeated', frequency)


"""Homework 2: Digits frequency
● Read a line of N integers.
● Compute the digits [0 to 8] frequency of all the N numbers
○ Input     78  307            [compute digits frequency of 7  8  3  0  7 ]
○ Output:
○ 0 1
○ 1 0                [digit 1 never appeared]
○ 2 0
○ 3 1
○ 4 0 
○ 5 0
○ 6 0
○ 7 2               [digit 7 appeared twice]
○ 8 1
○ 9 0"""

# More pythonic - Readable code
# Less prone to error
# Shorter!
#
# def digits_frequency(lst):
#     freq = [0] * 10
#
#     for value in lst:
#         # Convert the number to a string and add it
#         string = str(abs(value))
#         for char in string:
#             freq[int(char)] += 1
#
#     return freq
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#     freq = digits_frequency(lst)
#
#     for idx in range(10):
#         print(idx, freq[idx])


"""Homework 3: Is subsequence
● Read a line of N integers. Let’s call it list1
● Then Read a line of M integers. Let’s call it list2
● Print YES if list2 is a subsequence of list1. Otherwise print NO
● Input ⇒ Output
○ [1 2 3 4]   [1 4]          
○ [1 2 3 4]   [4 1]          
⇒ True
⇒ Fase          (items exist but NOT in order)
○ [10 -10 20 25 2 7 2 3]   [-10 2 2 3]    ⇒ True
○ [10 -10 20 25 2 7 2 3]   [-10 2 2 2 3]    ⇒ False
● Can you do it in a single loop?"""

#
# def is_subseuence(lst_main, lst_check):
#     if len(lst_check) == 0:
#         return True     # special case
#
#     # Iterate on the main list, for every number
#     # if it the FIRST number in lst_check
#     # then lst_check so far in order
#     # we remove it
#     # if all lst_check is empty: we found them: consective and in order
#     for item in lst_main:
#         if item == lst_check[0]:
#             lst_check.pop(0)    # pop(0) is efficient
#
#         if len(lst_check) == 0:		# Fix
#             return True
#
#     return False
#
#
# if __name__ == '__main__':
#     lst1 = list(map(int, input().split()))
#     lst2 = list(map(int, input().split()))
#
#     status = is_subseuence(lst1, lst2)
#
#     if status:
#         print('YES')
#     else:
#         print('NO')


"""Homework 4: Recamán's 
sequence
● The first terms of this sequence are 0, 1, 3, 6, 2, 7, … 
○ So last term value is 7 and its index is 5 (zero based)
○ The next value is either:
■ LastValue - LastIndex - 1 if the following 2 conditions are satisfied:
● value > 0 and It did not appear before
● E.g. 7 (last value) - last index (5) - 1 = 7-5-1 = 1   (> 0  but already exists)
■ Or LastValue + LastIndex + 1 = 7+5+1 = 13
● Read integer zero-based index ([1, 200]) and print the value of this index
○ E.g. (6 ⇒ 13), (9 ⇒ 21), (17 ⇒ 25)
● Don’t use nested loops
● The series is: 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43"""


# def recaman(n):
#     if n == 0:
#         return 0
#
#     # For N, probably an upper bound value is n * 10
#     occurrence = [0] * n * 10   # empty for n = 0
#     last_value, occurrence[0] = 0, 1  # first term
#
#     for i in range(1, n+1):
#         last_idx = i - 1
#
#         val = last_value - last_idx - 1
#
#         if val < 0 or occurrence[val]:
#             val = last_value + last_idx + 1
#
#         occurrence[val], last_value = 1, val
#
#     return last_value
#
# if __name__ == '__main__':
#     n = int(input())
#
#     print(recaman(n))


"""Homework 5: Remove evens inplace
● Read a line of N integers.
● Implement function: 
def remove_evens_inplace(lst):
○ It finds all the even numbers and remove them in place
○ Try to do it without creating new memory
● Input ⇒ Output
● 1 2 3 4 5 6 ⇒ 1 3 5
●-6 6 ⇒ Empty output
● Empty input ⇒ Empty output"""



# The key to remove properly is to remove from the end to the begin
# if you tried to remove from the begin the list will be corrupted
#
# def remove_evens_inplace1(lst):
#     # iterate backward
#     for pos in range(len(lst)-1, -1, -1):
#         if lst[pos] % 2 == 0:
#             del lst[pos]
#     return lst
#
#
# def remove_evens_inplace2(lst):
#     # iterate on revered but get the right index
#     sz = len(lst)   # important. take it here as list will be updated
#     for pos, item in enumerate(reversed(lst)):
#         if item % 2 == 0:
#             pos = sz - pos - 1    # idx in original list
#             # recall pos will be reassigned in every iteration
#             del lst[pos]
#     return lst
#
#
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     remove_evens_inplace2(lst)
#
#     print(lst)

# [First index to include, first index to exclude : step]
# step can be +ve or -ve
# range can be increasing or decreasing based on step

# print(type(range(5)))
#
# print(list(range(5)))               # [0, 1, 2, 3, 4]
#
# print(list(range(2, 5)))            # [2, 3, 4]
#
# print(list(range(1, 21, 4)))        # [1, 5, 9, 13, 17]
#
# print(list(range(5, 0, -1)))        # [5, 4, 3, 2, 1]
#
# print(list(range(10, 0, -2)))       # [10, 8, 6, 4, 2]
#
# print(list(range(5-1, -1, -1)))     # [4, 3, 2, 1, 0]

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# # 2 is the start
# # 6 is end (exclusive): ends actually at 5
# sub_list = my_list[2:6]     # 2 3 4 5
#
# sub_list[0] = 100           # my_list is NOT changed
#
# sub_list = my_list[5:6]     # 5 a single element
#
# sub_list = my_list[5:1000]  # 5 6 7 8
#
# # syntax: my_list[start : end+1



# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# sub_list = my_list[0:5]  # 0 1 2 3 4
# # If you did not provide start: then 0
# sub_list = my_list[ :5]  # 0 1 2 3 4
#
# # 9 = len(my_list)
# sub_list = my_list[4:9]  # 4 5 6 7 8
# # similarly: if not end: it is len
# sub_list = my_list[4: ]  # 4 5 6 7 8
#
# # observe:
# # my_list[4] is the 5th element (index 4)
# # my_list[4:] is slice from index 4 to last element
# # my_list[:4] is slice from 0 to 3
#
# same_values = my_list[:4] + my_list[4:]
# # 0 1 2 3 4 5 6 7 8
# print(same_values is my_list)   # False
#
# # both start and end are empty: WHOLE list
# same_values = my_list[:]
#
# print(same_values)


# Slice with a positive step


# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# sub_list = my_list[1:8  ]    # 1 2 3 4 5 6 7
# sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7
# sub_list = my_list[1:8:2]    # 1 3 5 7
# sub_list = my_list[1:8:3]    # 1 4 7
#
# # Missing step: default = 1
# sub_list = my_list[1:8: ]   # [1, 2, 3, 4, 5, 6, 7]

# class Employee:
#     pass
#
# obj1 = Employee()
# obj2 = Employee()
# obj3 = Employee()
#
# lst1 = [obj1, obj2, obj3]
# lst2 = lst1[0:2]    # create a NEW list
#
# print(lst1 is lst2)         # False
# print(lst1[0] is lst2[0])   # True
#
# # List is new - items are just assigned (same memory)

# Slice with a positive step

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# sub_list = my_list[1:8  ]    # 1 2 3 4 5 6 7
# sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7
# sub_list = my_list[1:8:2]    # 1 3 5 7
# sub_list = my_list[1:8:3]    # 1 4 7
#
# # Missing step: default = 1
# sub_list = my_list[1:8: ]   # [1, 2, 3, 4, 5, 6, 7]
#
# # Positive step: Missing end: default is len(seq)
# sub_list = my_list[1:9:2]   # 1 3 5 7
# sub_list = my_list[1: :2]   # 1 3 5 7
#
# # Positive step: Missing start: default is 0
# sub_list = my_list[0:6:2]   # 0 2 4
# sub_list = my_list[ :6:2]   # 0 2 4
#
# sub_list = my_list[0:9:2]   # 0 2 4 6 8
# sub_list = my_list[ : :2]   # 0 2 4 6 8
#
# sub_list = my_list[0:9:1]   # [0, 1, 2, 3, 4, 5, 6, 7, 8]
# sub_list = my_list[ : : ]   # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# # Slice with a negative step
#
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7
#
# sub_list = my_list[8:1:-1]   # 8 7 6 5 4 3 2: high to low
#
# sub_list = my_list[7:0:-1]   # 7 6 5 4 3 2 1
# sub_list = my_list[7:0:-2]   # [7, 5, 3, 1]
#
# sub_list = my_list[2:5:-1]   # [] must be high to low
#
# # Negative step: Missing start: default is len
# sub_list = my_list[9:2:-1]      # [8, 7, 6, 5, 4, 3]
# sub_list = my_list[ :2:-1]      # [8, 7, 6, 5, 4, 3]
#
# # Negative step: Missing end: default is hmm
# # starts from index 0 INCLUSIVE (NOT default)
# sub_list = my_list[5: :-1]      # [5, 4, 3, 2, 1, 0]
#
# sub_list = my_list[5:0:-1]      # [5, 4, 3, 2, 1]
#
# sub_list = my_list[::-1]        # reversed list
# # [8, 7, 6, 5, 4, 3, 2, 1, 0]

# another perspective

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# # Positive step: Missing start: iterate from the begin
# print(my_list[ :5:1])       # [0, 1, 2, 3, 4]
#
# # Positive step: Missing end: iterate till the end (inclusive)
# print(my_list[2: :1])       # [2, 3, 4, 5, 6, 7, 8]
#
# # Negative step: Missing start: iterate from the end
# print(my_list[ :5:-1])      # [8, 7, 6]
#
# # Negative end: Missing start: iterate till the begin (inclusive)
# print(my_list[2: :-1])      # [2, 1, 0]
#
# # covers from the end till the begin inclusive
# print(my_list[ : :-1])      # [8, 7, 6, 5, 4, 3, 2, 1, 0]
#
# # kind of: cover all values in the missing direction
#
# # practice makes perfect :)


# lst = [1, 2, 3, 4, 5, 6, 7]
# lst[2] = 100    # 1 2 100 4 5 6 7
#
# lst[3:6] = [982]    # 1 2 100 982 7
#
# lst[1:3] = [10, 11, 12, 13]    # 1 10 11 12 13 982 7
#
# # you need to replace 3 times with LIST OF THREE
# #lst[1:6:2] = [1]   # ValueError
# lst[1:6:2] = [-1, -2, -3]    # 1 -1 11 -2 13 -3 7
# #lst[6:2:-2] = [0]   # ValueError
#
# lst[3:] = [123]     # 1 -1 11 123
#
# lst = [1, 2, 3, 4, 5, 6, 7]
#
# del lst[1:3]            # 1 4 5 6 7
#
# del lst[1:5:2]        # 1 5 7

#        #  -7  -6 -5 -4 -3 -2 -1    # 7 + neg_pos
# my_list = [0, 1, 2, 3, 4, 5, 6]
#
# ln = len(my_list)
#
# print(my_list[ln-1])    # 6 = last number
# print(my_list[ln-2])    # 5 = 2nd last number
#
# # Negative indexing
# print(my_list[-1])    # 6 = last number
# print(my_list[-2])    # 5 = 2nd last number
#
# print(my_list.pop(-1))  # 6
# print(my_list.pop(-1))  # 5
#
# #my_list: [0, 1, 2, 3, 4]

# Slice with negative indexing

#          #-9 -8 -7 -6 -5 -4 -3 -2 -1    # 9 + neg_pos
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
#
# sub_list = my_list[3:7]     # 3 4 5 6
# # we can rewrite by finding the matched -ve indices
# sub_list = my_list[-6:-2]   # 3 4 5 6
# sub_list = my_list[-6:7]    # 3 4 5 6
# sub_list = my_list[3:-2]    # 3 4 5 6
#
# # observe: -6 < -2
# #sub_list = my_list[-2:-6]   # Empty list!


# Slice with a negative step
#
#          #-9 -8 -7 -6 -5 -4 -3 -2 -1    # 9 + neg_pos
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
# sub_list = my_list[1:8:1]    # 1 2 3 4 5 6 7
#
# sub_list = my_list[-8:-2:1]    # 1 2 3 4 5 6
# sub_list = my_list[-2:-8:-1]   # 7 6 5 4 3 2


# lst1 = [2, 3, 4, 1]
#
# # Old syntax
# lst2 = []
# for i in lst1:
#     lst2.append(i *i + 1)
#
# print(lst2)     # [5, 10, 17, 2]
#
# # new syntax
# lst2 = [i*i+1   for i in lst1]
# print(lst2)     # [5, 10, 17, 2]


# new_list = [expression  for member in iterable   ]

# lst1 = [2, 3, 4, 1]
#
# lst2 = [i*i+1   for i in lst1]
# print(lst2)     # [5, 10, 17, 2]
#
# lst3 = [n+1 for n in range(5, 9)]
# print(lst3)     # [6, 7, 8, 9]
#
# lst4 = [3*char for char in 'Hey']
# print(lst4)     # ['HHH', 'eee', 'yyy']


# lst1 = [1, -2, 6, -3, 2, -6]
#
# # Old syntax
# lst2 = []
# for n in lst1:
#     if n > 0:
#         lst2.append(n)
#
# print(lst2)     # [1, 6, 2]
#
# # New syntax
# lst3 = [n for n in lst1   if n > 0]
# print(lst3)     # [1, 6, 2]


"""Homework 1: Minimum of a type!
● Write a function that takes a list and a type
○ It returns the minimum value among this data type or None if not present
○ E.g. In below list: [10, 20, 5] are of type int. Their minimum is 5"""

# def find_smallest(lst, target_type):
#     new_lst = [item for item in lst if type(item) is target_type]
#
#     if len(new_lst) == 0:
#         return None
#
#     return min(new_lst)
#
#
# if __name__ == '__main__':
#     lst = [10, -2.5, 20, 5, 'mostafa', 5.2, 'Ziad']
#
#     print(find_smallest(lst, type(0)))      # 5
#     print(find_smallest(lst, type(0.0)))    # -2.5
#     print(find_smallest(lst, type('')))     # Ziad


"""Homework 3: Is sublist
● Read a line of N integers. Let’s call it list1
● Then Read a line of M integers. Let’s call it list2
● Print YES if list2 is a sublist of list1. Otherwise print NO
○ Sublist is like substring. All of it as it is should appear in list1
● Input ⇒ Output
○ [1 2 3 4]   [1 4]          
○ [1 2 3 4]   [2 3]          
⇒ False
⇒ True
○ [10 -10 20 25 2 7 2 3]   [20 25 25]    ⇒ True
○ [10 -10 20 25 2 7 2 3]   [20 25 7]    ⇒ False"""

"""Background: Fixed Sliding Window
● Indicate a group of consecutive number. Fixed and variable size
○ You slide to next window 
Img src
Background: Fixed Sliding Window
● Assume a list: 1 0 3 -4 2  -6 9
● Sliding window (sublist): 3
● Let’s print all windows of length 3 and their sum
○ 1 0 3       
○   0 3 -4      
⇒ sum = 4
⇒ sum = -1                 [observe 0 3 are common]
○      3 -4 2      
○         -4 2 -6     
⇒ sum = 1
⇒ sum = -8
○             2 -6 9      
⇒ sum = 5
● Observe the relation between 2 consecutive windows:
○ They share all the elements except a change in the first / last element
● Variable sliding window: its size grows and shrinks"""

# def is_subslist(lst_main, lst_check):
#     if len(lst_check) == 0:
#         return True  # special case
#
#     if len(lst_check) > len(lst_main):
#         return False
#
#     # For each index: generate a sublist and check
#     for idx in range(len(lst_main) - len(lst_check) + 1):
#         if lst_check == lst_main[idx: idx + len(lst_check)]:
#             return True
#
#     return False
#
#     # as slice is not memory efficient, this is not the most efficient code
#     # Another wat: internal loop to check the list step by step and stop early
#
#     # in practice: if list will be small: you should code it in a nice way
#     # if the efficient way is more effort to write by you / read by others
#     # code clarity is an important factor in industry
#     # not just efficiency that is not really added value
#     # I am just training you to be a better problem solver :)
#
#
# if __name__ == '__main__':
#     lst1 = list(map(int, input().split()))
#     lst2 = list(map(int, input().split()))
#
#     status = is_subslist(lst1, lst2)
#
#     if status:
#         print('YES')
#     else:
#         print('NO')


"""Homework 3: Fixed sliding window
● Read a line of N integers. Then Read integer K (on next line). K <= N
● Find the first sublist of K elements that has maximum sum. 
● Input  
○ 1 0 3 -4 2  -6 9
○ 3
○ Output: Starts at 4 with Sum 5
○ 30 -6 -8 10 2
○ 4
○ Output: Starts at 0 with Sum 26
● Medium to Hard: Can you do it without nested loops? There are 2 ways."""

# def maxium_sum_fixed_window(lst, k):
#     start_idx, max_sum = None, None
#     # For each index: generate a sublist and check
#     for idx in range(len(lst) - k + 1):
#         sublist_sum = sum(lst[idx : idx + k])
#
#         if max_sum is None or max_sum < sublist_sum:
#             max_sum, start_idx = sublist_sum, idx
#
#     return start_idx, max_sum
#
# # Nest loop sol: O(N^2)
# # Observe: the slice needs to iterate O(N) steps.
# # The sum needs to iterate O(N)
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#     k = int(input())
#
#     start_idx, max_sum = maxium_sum_fixed_window(lst, k)
#
#     print(start_idx, max_sum)


"""Homework 4: Count increasing sublists
● Read a line of N integers. Count how many sublist are increasing
● E.g. If input  is 1 2 3 4
○ We can find all sublists of length 1 ⇒ [1], [2], [3], [4]
○ All sublists of length 2 ⇒ [1, 2], [2, 3], [3, 4]
○ All sublists of length 3 ⇒ [1, 2, 3], [2, 3, 4]
○ All sublists of length 4 ⇒ [1, 2, 3, 4]
● Inputs ⇒ Outputs
○ 1 2 3 4  ⇒ 10    [10 sublists from previous example, all are increasing]
○ 4 3 2 1 ⇒ 4       [only sublists of length 1 can be considered]
○ 10 20 1 5 ⇒ 6
● Easy using 3 nested loops. Medium using 2 loops. Hard using 1 loop
○ Do your best"""

# caution: this is hard. Try and comeback later

# 1 loop
# Even the last idea has duplicate of computations
# If we know our best increasing lst is [1, 2, 3, 4]
# why trying from 2 to reach 4, then from 3 to reach?
# We already know we have 4*5/2 valid sequences (all start and end)

# idea
# Get your max increasing sequence. Now this adds n*(n+1)/2
    # for simplicity, just add the current sequence length
# Move to the next start. And so on


# def count_increasing(lst):
#     total = len(lst)    # initally for sequence of length 1
#     cur_len = 1
#
#     for idx in range(1, len(lst)):
#         # Keep expand the current valid sequence if possible
#         if lst[idx-1] <= lst[idx]:
#             total += cur_len    # At each step: we have cur_len ending at this position
#             cur_len += 1    # add another element
#         else:
#             cur_len = 1     # start a new sequence
#
#     return total
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     print(count_increasing(lst))

"""Homework 5: Josephus problem
● Read 2 integers N (<= 200) and K (<= 1000000). Code for small K first
○ Find the game winner for following game:
● We have a group of N people in Circle. They are numbered 1, 2, …. N
○ Someone is the master of the game.
○ He starts from Person #1. Count K. Then remove this person from the circle.
○ He keeps doing so till only 1 person remains. This is the winner.
● Input 4 2
○ Means we have people: 1, 2, 3, 4. Master starts at 1
○ Count 2 persons (2 removed), start from 3
○ Count 2 persons (4 removed), start from 1
○ Count 2 persons (3 removed), 1 is winner
● Output
○ People removed in order: 2 4 3 1      [same answer for 10 2 why?]
Homework 5: Josephus problem
● Input ⇒ Output
○ 7 1 ⇒ 1 2 3 4 5 6 7 
○ 7 2 ⇒ 2 4 6 1 5 3 7 
○ 7 3 ⇒ 3 6 2 7 5 1 4
○ 7 4 ⇒ 4 1 6 5 7 3 2 
○ 7 5 ⇒ 5 3 2 4 7 1 6 
○ 7 6 ⇒ 6 5 7 2 1 4 3 
○ 7 7 ⇒ 7 1 3 6 2 4 5 
○ 7 14 ⇒ 7 2 6 3 5 4 1 
○ 7 1000 ⇒ 6 3 2 1 4 7 5 
○ 7 99999 ⇒ 4 7 5 2 1 3 6 """


# Direct Simulation!

# def josephus(n, k):
#     lst = [0] * n
#
#     for idx in range(n):
#         lst[idx] = idx + 1  # assign 1 2 3 4 5 ... n
#
#     # Note creating length at once is MORE efficient than N appends
#
#     last_pos = 0
#     ret = []
#
#     while len(lst) > 1:
#         # first guy is counted. Iterate k-1 steps
#         for step in range(k-1):
#             last_pos += 1
#             if last_pos == n:   # let's cycle
#                 last_pos = 0    # go back to begin
#
#         ret.append(lst[last_pos])
#         lst.pop(last_pos)
#         n = len(lst)  # list is shrinking
#         if last_pos == n:
#             last_pos = 0
#
#     ret.append(lst[0])
#
#     return ret
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#
#     print(josephus(n, m))


"""Homework 6: longest sublist
● Read a line of N integers. Each is just 0 or 1
● Find the longest sublist with number of zeros == numbers of ones
○ Easy: 3 loops
○ Medium: 2 loops (even with no extra arrays)
○ (very) hard: Single loop
● Inputs ⇒ outputs
○ 1 0 0 0 1 1 1  ⇒ 6                                                (e.g. 100011 or 000111)
○ 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 0 0  0 1   ⇒ 8          (e.g. 00101101)
○ 1 1 1 1 ⇒ 0
○ 1 1 1 0 0 ⇒ 4
○ 0 ⇒ 0
● Reduction
○ How may this problem be reduced to another problem: longest sublist of zero sum?"""

# HARD
# 1 loop

"""
Assume input

index 0 1 2 3 4
value 1 1 1 0 0

How many ones and zeros at position 0: (1, 0)
How many ones and zeros at position 4: (3, 2)   => cancel 1s with 0s ==> (1, 0)

What does it mean to have 2 positions with same value of: total ones - total zeros?
    It means the values in between the 2 positions must have ones = zeros
        Specifically from pos 1 to pos 4


Algorithm:
- Keep accumulating current value to compute total ones - total zeros
- use 2 arrays one for postivie value and one for -ve  (or use one list with a shifted value)
- If first time to see such value: mark it
- if you met it before: we have a new valid range"""


# def longest_subarray(lst):
#     best_len = None
#
#     postives = [-1] * (len(lst) + 1)
#     negatives = [-1] * (len(lst) + 1)
#
#     accumulation = 0
#
#     for idx, item in enumerate(lst):
#         first_idx = None
#
#         if item == 0:
#             accumulation -= 1
#         else:
#             accumulation += 1
#
#         if accumulation == 0:
#             best_len = idx + 1
#         elif accumulation > 0:
#             if postives[accumulation] == -1:  # such accumulation never appeared
#                 postives[accumulation] = idx  # mark the first idx for that
#             else:
#                 first_idx = postives[accumulation]
#         else:
#             if negatives[-accumulation] == -1:
#                 negatives[-accumulation] = idx
#             else:
#                 first_idx = negatives[-accumulation]
#
#         if first_idx is not None:
#             cur_len = idx - first_idx
#
#             if best_len is None or best_len < cur_len:
#                 best_len = cur_len
#
#     return best_len if best_len is not None else 0
#
# # later with dict: the code can be simplified
#
# # By replacing 0 as -1, each group of equal ones and zeros is actually sublist of zero sum
#
# if __name__ == '__main__':
#     lst = list(map(int, input().split()))
#
#     print(longest_subarray(lst))


























































