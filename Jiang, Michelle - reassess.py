"""
title: Kitchen Converter
author: Michelle Jiang 
date-created: 2023-01-17
"""

### FUNCTIONS ### 

def checkInt(NUMBER, MINVALUE=0, MAXVALUE=5000) -> int:
    """
    checks if a string contains a valid integer
    :return: int
    """
    try:
        NUMBER = int(NUMBER)
        if NUMBER > MAXVALUE or NUMBER < MINVALUE:
            print(f"Please input an integer less than or equal to {MAXVALUE} and greater than or equal to {MINVALUE}! ")
            NEWNUMBER = input("> ")
            return checkInt(NEWNUMBER, MINVALUE, MAXVALUE)
        else:
            return NUMBER
    except ValueError:
        print("Please input an integer! ")
        NEWNUMBER = input("> ")
        return checkInt(NEWNUMBER, MINVALUE, MAXVALUE)

def checkFloat(NUMBER, MINVALUE=-5000, MAXVALUE=5000) -> float: # in case they want to freeze something 
    """
    checks if a string contains a valid float
    :return: float
    """
    try:
        NUMBER = float(NUMBER)
        if NUMBER > MAXVALUE or NUMBER < MINVALUE:
            print(f"Please input a float less than or equal to {MAXVALUE} and greater than or equal to {MINVALUE}! ")
            NEWNUMBER = input("> ")
            return checkInt(NEWNUMBER, MINVALUE, MAXVALUE)
        else:
            return NUMBER
    except ValueError:
        print("Please input a float! ")
        NEWNUMBER = input("> ")
        return checkFloat(NEWNUMBER, MINVALUE, MAXVALUE)

# INPUTS # 

def startScreen() -> None:
    """
    displays starting text
    """
    print("Welcome to the Kitchen Converter! ")
    return

def menu() -> int:
    """
    displays a menu for user to choose options from
    :return: int
    """
    print("""
Please choose one of the following: 
1. Celsius to Fahrenheit 
2. Fahrenheit to Celsius
3. Pounds to Grams
4. Exit
    """)
    CHOICE = input("> ")
    CHOICE = checkInt(CHOICE, 1, 4)
    return CHOICE

def valueToBeConverted() -> float:
    """
    user inputs the value to be converted 
    :return: float 
    """
    print("Please input the value you would like to be converted: ")
    VALUE = input("> ")
    VALUE = checkFloat(VALUE)
    return VALUE

# PROCESSING # 

def celsiusToFahrenheit(VALUE) -> float:
    """
    converts the value from celsius to fahrenheit
    :param VALUE: float
    :return: float 
    """
    VALUE = VALUE * 1.8 + 32 
    VALUE = round(VALUE, 2)
    return VALUE

def fahrenheitToCelsius(VALUE) -> float:
    """
    converts the value from fahrenheit to celsius 
    :param VALUE: float
    :return: float 
    """
    VALUE = (VALUE - 32) / 1.8 
    VALUE = round(VALUE, 2)
    return VALUE

def poundsToGrams(VALUE) -> float:
    """
    converts the value from pounds to grams
    :param VALUE: float 
    :return: float
    """
    VALUE = VALUE * 453.592
    VALUE = round(VALUE, 2)
    return VALUE

# OUTPUTS # 

def displayResult(VALUE) -> None:
    """
    displays the converted value
    :param VALUE: float
    :return: None
    """
    print(f"The result of your conversion is {VALUE}. ")
    return

### MAIN PROGRAM CODE ### 

if __name__ == "__main__":
    # INPUTS # 
    startScreen()
    while True:
        CHOICE = menu()
        # PROCESSING # 
        if CHOICE == 1:
            # INPUTS # 
            VALUE = valueToBeConverted()
            # PROCESSING # 
            VALUE = celsiusToFahrenheit(VALUE)
            # OUTPUTS # 
            displayResult(VALUE)
        elif CHOICE == 2:
            # INPUTS # 
            VALUE = valueToBeConverted()
            # PROCESSING #
            VALUE = fahrenheitToCelsius(VALUE)
            # OUTPUTS #
            displayResult(VALUE)
        elif CHOICE == 3: 
            # INPUTS #
            VALUE = valueToBeConverted()
            # PROCESSING #
            VALUE = poundsToGrams(VALUE)
            # OUTPUTS #
            displayResult(VALUE)
        # OUTPUTS # 
        elif CHOICE == 4:
            exit()