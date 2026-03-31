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


def argmax(lst):
    # Given a list: return the idx of the maximum value
    # Return None for an empty list
    if len(lst) == 0:
        return None
    return lst.index(max(lst))


def top2_argmax_v1(lst):
    # Given a list: return the indices of the first and second maximum
    if len(lst) < 2:
        return None, None

    # get top max position and value
    max1_pos = argmax(lst)
    max1_val = lst[max1_pos]

    # replace it with a very small value
    mn_value = min(lst)
    lst[max1_pos] = mn_value - 1

    max2_pos = argmax(lst)

    # undo the change to the list
    lst[max1_pos] = max1_val

    return max1_pos, max2_pos

def main():
    lst = list(map(int, input().split()))

    max1_pos, max2_pos = top2_argmax_v1(lst)

    if max1_pos is not None:
        print('idx1', max1_pos, 'value', lst[max1_pos])
        print('idx2', max2_pos, 'value', lst[max2_pos])



main()



