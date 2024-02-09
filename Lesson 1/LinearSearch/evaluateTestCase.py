from find_card import find_card

test = {#The card is somewhere in the middle of the card list
        'input': {
            'cardList': [3, -1, -9, -127],
            'card': -127
        },
        'output': 3
}


def evaluateTestCase(find_card, testCase):
    result = find_card(testCase['input']['cardList'], testCase['input']['card'])

    print("Input:")
    print(testCase['input'])
    print("\n")
    
    if testCase['output']:
        print("The expected output is: " + str(testCase['output']))
        print("\n")

    print("The actual output is " + str(result))
    print("\n")

    if result == testCase['output']:
        print("Test Result: PASSED!")
        print("\n")
    else:
        print("Test Result: FAILED!")
        print("\n")
    # findCard = find_card(testCase['input']['cardList'], testCase['input']['card'])
    # return findCard

evaluateTestCase(find_card, test)