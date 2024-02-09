# test = {#The card itself is repeated in card list. Here we expect the first occurence to be returned
#         'input': {
#             'cardList': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
#             'card': 6
#         },
#         'output': 2
# }

def test_location(cardList, card, mid):
    mid_number = cardList[mid]
    print("mid: ", mid, ", mid_number: ", mid_number)

    if mid_number == card:
        if mid - 1 >= 0 and cardList[mid - 1] == card:
            return 'left'
        else:
            return 'found'
    elif mid_number < card:
        return 'left'
    else:
        return 'right'

# test_location(test['input']['cardList'], test['input']['card'], 2)    