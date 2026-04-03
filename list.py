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



























