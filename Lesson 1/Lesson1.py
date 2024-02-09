"""
From the course by Jovian's CEO Aakash
---------------------------------------
Lesson 1 covers:
    1.Binary Search.
    2.Linked Lists.
    3.Complexity Analysis.

    * Linear and Binary Search.
    * Complexity and Big O Notation.
    * Linked Lists using Python Classes.
------------------------------------------
Problem:
    Question1:
        Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays
        them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given 
        number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""

"""
Solution to Question1:
    To represent the list of cards, we initialize a variable called cardsList that holds Alice's cards in the order 
    she has laid them out. Let us assume that she lays seven cards out each with a number showing the order in 
    which it decreases.
"""


cardsList = [13, 11, 10, 7, 4, 3, 1, 0]

"""
Alice knows what the card is and at what position it is placed. But because all the cards are faced downward we have
no idea where the card is positioned but we know the card we are looking for as well.
To find our card position in Alice's card list we must have another variable that has the card we are looking for stored so we 
can find the card's position in cardList. Let us call this variable 'card'.

So our inputs to find the card that Alice has challenged Bob to find are:
    cardList: Bob gives us this information on how the cards are arranged.
    card: Bob gives us the card we are looking for.

    With this two inputs, we can write a function that accepts the inputs as parameters and helps Bob find the card.
"""

def find_card(cardsList, card):
    #position is initialized as a way to determine the card's position
    position = 0

    #repeat as long as the value of position is less than the total length of the card list
    while position < len((cardsList)):
        #check if the position in cardList corresponds to the card we are looking for. 
        if cardsList[position] == card:
            #if they are the same, the card has been found, tell us the position and stop.
            return position

        position += 1
    return -1

"""
TEST CASES
---------------------------------------------------------------------------------------------------------------------------
We will implement test cases using a dictionary that has two keys; 'input' and 'output'. The input key's value will be 
a dictionary that has two keys as well; 'cardList' and 'card'. The output key value will be the position of the card.

Some possible test cases are:
    1. The card is somewhere in the middle of the card list
    2. The card is the first element in the card list
    3. The card is the last element in the card list
    4. The card is the only element in the card list
    5. The card is not in the card list (an edge case)
    6. The card list is empty (an edge case)
    7. The cardlist contains repeating numbers
    8. The card itself is repeated in card list
    -------------------------------------------------------------------------------------------------------------------------

    In situations where the problem does not specify what should be done with edge cases;
    1. Read the problem again carefully
    2. Look through examples provided with the problem
    3. Ask for clarification from the interviewer
    4. Make a reasonable assumption, state it and move forward
"""
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

"""
To evaluate a single test case, we could write a function that helps to do this. Let us call the function evaluateTestCase.
This function will take the function find_card and a single test case and print out the result to see if the function is robust.
If it is not, we debug and make it robust as well as functional and efficient.
"""

#Function to test a single test case
def evaluateTestCase(find_card, testCase):
    """
    The first parametre in this function takes the function 'find_card()'
    The second parametre takes a single test case.
    """

    #result stores the value from the operation carried out by the function find_card
    result = find_card(testCase['input']['cardList'], testCase['input']['card'])
    
    #Here we make a comparison with our test case output and print it out as our expected output
    if testCase['output'] == testCase['output']:
        print("The expected output is: ", result)
        print("\n")

    #Here we print the actual output we get which is stored in the result variable
    print("The actual output is ", result)
    print("\n")

    #Here we compare our result to the expected output to determine if the test has passed or failed
    if result == testCase['output']:
        print("Test Result: PASSED!")
        print("\n")
    else:
        print("Test Result: FAILED!")
        print("\n")


"""
We could also write a function that tests all test cases at once. This will make it a lot easier to verify our find_card function
withouth manually imputing all of our test cases. Let us call this function checkTestCases.
"""

#Function to test multiple test cases
def checkTestCases(find_card, testCases):
    """
    The first parametre in this function takes the function 'find_card()'
    The second parametre takes a list of test cases.
    """

    #Counter here is used as an iterative device
    counter = 1

    #Here we loop through our test cases and test them one after the other
    for case in testCases:

        #result stores the value from the operation carried out by the function find_card
        result = find_card(case['input']['cardList'], case['input']['card'])

        #Here we see the use of the counter as it details which test case we are currently testing
        print("TEST CASE #", counter)
        print("\n")

        #Here we make a comparison with our test case output and print it out as our expected output
        if case['output'] == case['output']:
            print("The expected output is: ", case['output'])
            print("\n")

        #Here we print the actual output we get which is stored in the result variable
        print("The actual output is ", result)
        print("\n")

        #Here we compare our result to the expected output to determine if the test has passed or failed
        if result == case['output']:
            print("Test Result: PASSED!")
            print("\n")
        else:
            print("Test Result: FAILED!")
            print("\n")

        #Here we increment the counter 
        counter += 1

 
"""
To figure out the execution time of the program we could do something like this:
start = time.time() -> This stores the time the program starts running.
end = time.time() -> This stores the time the program ends

The execution time is the difference between the start and end.
This prints the execution time:
    print("The execution time is ", (end - start)*10**3, "ms")
        # print("\n")
"""

"""
The function find_card is a simplistic function that searches the entire list until the card position is located.
This could result could be immediate if the card position is close to the search start position or the result
could be very late in coming if the card position is far away from the search start position. The solution we have
implemented here is a brute force solution because it checks for all possible answers until the right one is found.
However, from our problem statement, Bob needs to turnover as few cards as possible to access the cards. So we need
an optimal or better way to help Bob in doing this.

A BETTER WAY?
------------------------------------------------------------------------------------------------------------------------------
A good way may be to guess the right card at the first attempt. But if Bob could do this, he would not need our help to 
check for his hidden card. He could just guess it's position and be done with it. So guessing the right card may not be 
our solution. How about if instead of a right card, we guessed a random card? If we guess a random card, by virtue of
the card list being sorted we can focus on a certain part while disregarding another part of the list. So if we picked
a card in the middle and it shows 9 and the card we are looking for is a 7, it means that we can disregard all cards to
the left of the card we randomly selected and focus on the right side of the card. This seems a better way as it removes
needless searching through the entire list. So we want to guess which card to pick, it would not be a good idea to pick 
card close to the ends of the list as this might not give us enough information to work with. But if we pick a card from
the middle, we can quickly eliminate half of the cards we would need to search through. From the half that remains for 
us to search through, we can again pick the middle card and eliminate another half. This is what is known as binary search.
------------------------------------------------------------------------------------------------------------------------------

THE BINARY SEARCH 'for sorted list'
------------------------------------------------------------------------------------------------------------------------------
Steps:
    1. Locate the middle element of the list 
    2. If middle element is equal to our number return the position of the number
    3. If it is less than the number then search the greater half of the list
    4. If it is greater than the number then search the lesser half of the list
    5. If no elements remain, return -1
------------------------------------------------------------------------------------------------------------------------------
"""

#Function to perform a binary search
def bin_search(cardsList, card):

    """
    Above like the previous find card function, the bin_search function takes similar parametres

    Below is a varaible allocation of pointers high and low and as the name suggests, they point to the highest and lowest 
    elements in the list. Low is set to the start index and high is set to the end index.
    """
    low, high = 0, len(cardsList) - 1

    #This loop keeps track of every disregarded part of our list by constantly reassigning the high and low values
    while low <= high:

        #This prints our current values with every iteration.
        print("low: ", low, ", high: ", high)

        #The mid is the middle of our list, it is the index value of the midnumber. This line ensures we get an integer as our value.
        mid = (low + high) // 2

        #The result is to help us satisfy the test where we must return the first occurrence of our card
        result = test_location(cardsList, card, mid)

        

        #This checks if our result is the same as the string found, if it is we return the mid index
        if result == 'found':
            return mid
        
        #This checks if our result is the same as the string left, if it is we go left
        elif result == 'left':
            high = mid - 1

        #This checks if our result is the same as the string right, if it is we go right
        elif result == 'right':
            low = mid + 1
    return -1


"""
For the bin_search function above we require a helper function that would help us passing certain test conditions
This condition is the need for us to return the first occurrence of the card in the list. The functionis given below:
"""

def test_location(cardList, card, mid):
    mid_number = cardList[mid]
    print("mid: ", mid, ", mid_number: ", mid_number)

    if mid_number == card:
        if mid - 1 >= 0 and cardList[mid-1] == card:
            return 'left'
        else:
            return 'found'
    elif mid_number < card:
        return 'left'
    else:
        return 'right'