# test = {#The card list is empty (an edge case) here we also assume our output is -1
#         'input': {
#             'cardList': [],
#             'card': 7
#         },
#         'output': -1
# }

#This performs a linear search for the card.
def find_card(cardsList, card):
    #position is initialized as a way to determine the card's position
    position = 0

    #repeat as long as the value of position is true
    while position < len(cardsList):
        #check if the position in cardList corresponds to the card we are looking for. 
        if cardsList[position] == card:
            #if they are the same, the card has been found, tell us the position and stop.
            return position
    
        position += 1
    return -1
        