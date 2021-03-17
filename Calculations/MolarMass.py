#AtomicMass.py is a collection of variables containing
# the molar mass for every element.
#
#The name for each of these variables is the symbol of the element it represents.
# this makes evaluating the math string at the end of the function simple, because 
# ideally, the computer will recognize the chemical formulas that the user inputs as variables.
from AtomicMass import *

#returns a list of each character in the string
def split(string):
        return [char for char in string]

#converts a list of characters to a string
def listToString(s):
    str1 = ""
    for c in s:
        str1 += " " + c
    return str1

# Calculates the molar mass of the chemical formula parameter. 
#
#  parameter needs to be a string, which is ideal for user input.
def calculateMolarMass(formula):
        formula = split(formula) 
        # for each element in the list of characters, it checks whether the 
        # next character in the list is a part of that element. 
        # 
        # for example, if the current character is an upper case letter and the next character 
        # is a lower case letter, it groups them together.
        for index, elem in enumerate(formula):
            if index != len(formula) - 1:
                if formula[index].isupper() and not formula[index + 1].isnumeric() and not formula[index + 1].isupper() and formula[index + 1] != "(" and formula[index + 1] != ")":
                    formula[index] += formula[index + 1]
                    formula.remove(formula[index+1])
                if formula[index].isnumeric() and formula[index + 1].isnumeric():
                    formula[index] += formula[index + 1]
                    formula.remove(formula[index + 1])
        #After all of the characters are organized into the correct groups, 
        # this loop checks whether or not to add a math operator, and if so then which one.
        for i, e in enumerate(formula):
            if i != len(formula) - 1:
                if not formula[i + 1].isnumeric() and formula[i + 1] != ")" and formula[i] != "(":
                    formula[i] += " +"
                if formula[i + 1].isnumeric() or formula[i] == ")":
                        formula[i] += " *"
        
        #converts the list of characters and math operators to a string,
        #  and then evaluates the math equation to find the molar mass
        fformula = listToString(formula)
        molarMass = eval(fformula)

        return molarMass
