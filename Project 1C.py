# Project 1C
# Collects input as number(s) from the user, then displays the sum and mean of those numbers.
# Horsman, Kenneth
# Course: CSC1019-FBN

""" General note: using the 'global' keyword is not a great pattern. It has its uses, but generally you want to be very careful about it. In this case, it probably makes more sense to just have the function return the numbers variable and then assign it in the main program. After all, you don't even need it until the last line anyway. """
def inputNumbers():
    global numbers
    while True:
        userInput = input("Please enter numbers separated by a comma. Press ENTER when done: ")
        if userInput == "":
            noInput()
            break
        inputList = userInput.split(",") # Splits userInput into a list divided by a comma
        inputTest = [] # Empty test list
        for x in inputList: # For every value in the inputList:
            inputTest += x.replace("-", "") # Remove spaces, negatives, and add the resulting value to inputTest
        if all(x.isnumeric() for x in inputTest): # If all values in inputTest are numeric
            numbers = list(map(int, inputList)) # Then assign 'numbers' as a each value in inputList converted (mapped) into an integer
            break
        else:
            inputInvalid()
            break
    return numbers

def noInput():
    global numbers
    while True:
        userInput = input("No input given. Please try again: ")
        if userInput == "":
            noInput() # I don't know why it won't loop without me forcing it to
            break        
        inputList = userInput.split(",")
        inputTest = []
        for x in inputList:
            inputTest += x.replace("-", "")
        if all(x.isnumeric() for x in inputTest):
            """ Generally you would do this kind of thing using a list / tuple comprehension. """
            numbers = list(map(int, inputList))
            break        
        else:
            inputInvalid()
            break
    return numbers

def inputInvalid():
    global numbers 
    while True:
        userInput = input("Incorrect format. Please try again: ")
        if userInput == "":
            noInput()
            break
        inputList = userInput.split(",")
        inputTest = []
        for x in inputList:
            inputTest += x.replace("-", "")
        if all(x.isnumeric() for x in inputTest):
            numbers = list(map(int, inputList))
            break  
        else:
            inputInvalid() # Same issue here as on line 30
            break            
    return numbers 
    
def inputSumAndMean():
    inputSum = sum(numbers)
    inputMean = inputSum / len(numbers)
    """ This is actually ok - it's really len(numbers) that you don't want to be zero. """
    if inputSum == 0: # If the input is "2 -2" or "0 0" for example it will no longer return with a float division error.
        """ For all of the string concatenations you're doing here, it is probably more readable to use f-strings """
        print("The sum of " + str(numbers) + " is 0 and the average is 0.")
        return # Prevents function from trying to perform the operation to check if the mean is a whole number.   
    if inputMean > -1 and inputMean < 1: # Prevents float division error for decimal numbers starting with 0.
        print("The sum of " + str(numbers) + " is " + str(inputSum) + " and the average is " + str(inputMean) + ".")
        return
    if inputMean / int(inputMean) == 1: #Checks if the mean is a whole number
        print("The sum of " + str(numbers) + " is " + str(inputSum) + " and the average is " + str(int(inputMean)) + ".") # Converts the mean to an integer.
    else:
        print("The sum of " + str(numbers) + " is " + str(inputSum) + " and the average is " + str(inputMean) + ".")
    return

inputNumbers()
inputSumAndMean()
input("") # When the script is run in CMD, for example, this prevents the program from immediately closing once the above functions have finished running.
