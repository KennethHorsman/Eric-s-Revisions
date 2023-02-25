def is_valid_number_alternate(num: str) ->  bool:
    """ A way of determining whether a string represents a number which I prefer """
    try:
        float(num)
        return True
    except ValueError:
        return False

def is_valid_number(num: str) -> bool:
    """ (Quick and dirty) way to determine if a string represents a number. Right now it only handles negatives and decimals."""
    if num.replace(".", "").replace("-", "").isnumeric():
        return True
    return False

def input_numbers():
    numbers = [] # Creates empty list to add valid input to
    while True:
        userInput = input("Please provide a number and press ENTER. When you are finished, press ENTER again: ")
        if userInput == '':
            break # Forces user to enter inputs one line at a time, then submit by entering nothing.
        # test = userInput.replace(".","").replace("-","") # Allows decimals and negatives to pass the test by pretending to remove them
        if not is_valid_number(userInput):
        # invalidInput = [x for x in test if not x.isnumeric()] # Loops through value(s) in test to see if its numeric. is there a different approach when only  one value?
        # if len(invalidInput) > 0: # If anything is not numeric, invalidInput would obtain that value, increasing its length
            print(f"Invalid characters detected: {userInput}") # No idea how this went from printing entire input to just invalid character
        else:
            """ Now that you are entering a single value at a time, you don't need to extend """
            numbers.append(float(userInput))
            # A Adds userinput to numbers list if it passes tests above. I don't know why the split is needed to add negative values
    return numbers

""" I changed this so that it takes in the list of values to find the sum and mean for. Also, changed the name to better reflect what it does"""
def print_sum_and_mean(numbers):
    print(f"{numbers=}")
    summed = sum(numbers) if len(numbers) > 0 else "0" # Prints sum as equal to 0 if the len(numbers) is not at least 1
    """ It's not really correct to say zero here... """
    mean = summed / len(numbers) if len(numbers) > 0 else "0"
    print(f"For the numbers {[int(number) if number.is_integer() else number for number in numbers]}:\nSum = {summed}\nMean = {mean}") # F-string makes the entire thing a string when other data types within {} brackets
    return

numbers = input_numbers() # Originally I put this inside the sumAndMean but that seems like it might be a bad idea
print_sum_and_mean(numbers)
input('')


""" 
QUESTION:
Is it possible to make my numbers list into a combination of integers and floats?
I think it would look a lttle nicer to not have .0's in my print statement.
Example numbers: 1.5, 5, -10 , 4.25
Instead of: 1.5, 5.0, -10.0, 4.25
"""
""" Yes - see above :D """
