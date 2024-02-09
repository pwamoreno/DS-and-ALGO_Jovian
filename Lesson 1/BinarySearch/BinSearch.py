from TestLocation import test_location


"""
THE BINARY SEARCH 'for sorted list'
------------------------------------------------------------------------------------------------------------------------------
Steps:
    1. Locate the middle element of the list 
    2. If middle element is equal to our number return the position of the number
    3. If middle element is less than the number then search the greater half of the list
    4. If middle element is greater than the number then search the lesser half of the list
    5. If no elements remain, return -1
------------------------------------------------------------------------------------------------------------------------------
"""

# test = {#The card itself is repeated in card list. Here we expect the first occurence to be returned
#         'input': {
#             'cardList': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#             'card': 6
#         },
#         'output': 2
# }

def bin_search(cardsList, card):
    low, high = 0, len(cardsList) - 1

    while low <= high:
        print("low: ", low, ", high: ", high)
        mid = (low + high) // 2
        result = test_location(cardsList, card, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1
