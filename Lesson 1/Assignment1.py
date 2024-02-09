"""
The Problem:
    You are given a list of numbers, obtained by rotating a sorted list an unknown 
    number of times. Write a function to determine the minimum number of times the
    the original sorted list was rotated to obtain the given list. Your function
    should have the worst-case complexity of O(logN), where N is the length of the
    list. You can assume that all the numbers in the list are unique.

    Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted 
    list [0, 2, 3, 4, 5, 6, 9] 3 times.

    We define 'rotating a list' as removing the last element of the list and adding
    it before the first element. E.g. rotating the list [3, 2, 4, 1] produces this
    list [1, 3, 2, 4]

    'Sorted list' refers to a list where the elements are arranged in increasing
    order e.g. [1, 3, 5, 7].


    Test Cases:
        1. A list of size 10 rotated 3 times.
        2. A list of size 8 rotated 5 times.
        3. A list that was not rotated at all.
        4. A list that was just rotated once.
        5. A list that was rotated n-1 times, where n is the size of the list.
        6. A list that was rotated n times (do we get back the original list).
        7. An empty list.
        8. A list containing just one element.
"""
test = [ 
    {
        'input': [10, 13, 14, 0, 2, 3, 4, 5, 6, 9],
        'output': 3
    },
    {
        'input': [4, 5, 6, 9, 10, 0, 2, 3],
        'output': 5
    },
    {
        'input': [0, 2, 3, 4, 5, 6, 9, 10],
        'output': 0
    },
    {
        'input': [10, 0, 2, 3, 4, 5, 6, 9],
        'output': 1
    },
    {
        'input': [2, 3, 4, 5, 6, 9, 0],
        'output': 6
    },
    {
        'input': [0, 2, 3, 4, 5, 6, 9],
        'output': 0
    },
    {
        'input': [],
        'output': 0
    },
    {
        'input': [2],
        'output': 0
    },
]


# def rotatedList(items):
#     counter = 0

#     while counter < len(items):
#         if counter > 0 and items[counter] < items[counter - 1]:
#             print("The number of rotations is: ", counter)
#         counter += 1
#     print("0")

# rotatedList([])


def binaryRotatedList(items):
    low, high = 0, len(items) - 1

    while len(items) > 1 and low <= high:
        mid = (low + high) // 2
        mid_number = items[mid]

        if mid > 0 and mid_number < items[mid - 1]:
            print(mid)
        elif mid_number < items[len(items) - 1]:
            high = mid - 1
        elif mid_number > items[len(items) -1]:
            low = mid + 1
    return 0

hey = binaryRotatedList([0, 2, 3, 4, 5, 6, 9, 10])
print(hey)


# [1, 2, 3, 4, 5, -1, 0] -> Input to check on the right
# [7, 8, 1, 3, 4, 5, 6] -> Input to check on the left

