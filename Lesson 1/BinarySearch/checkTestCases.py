from BinSearch import bin_search
import time

testCases = [
    {#The card is somewhere in the middle of the card list
        'input':{
            'cardList': [13, 11, 10, 7, 4, 3, 1, 0],
            'card': 1
        },
        'output': 6
    },
    {#The card is the first element in the card list 
        'input': {
            'cardList': [7, 6, 5, 4, 3, 2, 1],
            'card': 7
        },
        'output': 0
    },
    {#The card is the last element in the card list
        'input': {
            'cardList': [3, -1, -9, -127],
            'card': -127
        },
        'output': 3
    },
    {#The card is the only element in the card list
        'input': {
            'cardList': [6],
            'card': 6
        },
        'output': 0
    },
    {#The card is not in the card list (an edge case) so we assume the function returns -1
        'input': {
            'cardList': [9, 7, 5, 2, -9],
            'card': 4
        },
        'output': -1
    },
    {#The card list is empty (an edge case) here we also assume our output is -1
    #The program breaks for this test case
        'input': {
            'cardList': [],
            'card': 7
        },
        'output': -1
    },
    {#The cardlist contains repeating numbers
    #The program breaks for this test case
        'input': {
            'cardList': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'card': 3
        },
        'output': 7
    },
    {#The card itself is repeated in card list. Here we expect the first occurence to be returned
    #The program breaks for this test case
        'input': {
            'cardList': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'card': 6
        },
        'output': 2
    }
]
# firstTestCase = testCases[0]['input']['cardList']
# print(firstTestCase)

def checkTestCases(bin_search, testCases):
    
    counter = 0
    passed = 0
    failed = 0
    # start = time.time()
    for case in testCases:
        result = bin_search(case['input']['cardList'], case['input']['card'])
        # end = time.time()
        
        print("TEST CASE #", counter + 1)
        
        print("Input:")
        print(testCases[counter]['input'])
        print("\n")

        if case['output']:
            print("The expected output is: ", case['output'])
            print("\n")

        print("The actual output is ", result)
        print("\n")

        # print("The execution time is ", (end - start)*10**3, "ms")
        # print("\n")
        
        if result == case['output']:
            passed += 1
            print("Test Result: PASSED!")
            print("\n")
        else:
            failed += 1
            print("Test Result: FAILED!")
            print("\n")
        counter += 1
    print("Summary: ")
    print("Total: " + str(counter), "Passed: " + str(passed), "Failed: " + str(failed), "\n")
       


checkTestCases(bin_search, testCases)