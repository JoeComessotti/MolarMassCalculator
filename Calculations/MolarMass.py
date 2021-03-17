from AtomicMass import *

def split(string):
        return [char for char in string]

def listToString(s):
    str1 = ""
    for c in s:
        str1 += " " + c
    return str1

def calculateMolarMass(formula):
        compound = formula
        comp = split(compound)
        for index, elem in enumerate(comp):
            if index != len(comp) - 1:
                if comp[index].isupper() and not comp[index + 1].isnumeric() and not comp[index + 1].isupper() and comp[index + 1] != "(" and comp[index + 1] != ")":
                    comp[index] += comp[index + 1]
                    comp.remove(comp[index+1])
                if comp[index].isnumeric() and comp[index + 1].isnumeric():
                    comp[index] += comp[index + 1]
                    comp.remove(comp[index + 1])

        for i, e in enumerate(comp):
            if i != len(comp) - 1:
                if not comp[i + 1].isnumeric() and comp[i + 1] != ")" and comp[i] != "(":
                    comp[i] += " +"
                if comp[i + 1].isnumeric() or comp[i] == ")":
                        comp[i] += " *"
        
        fcomp = listToString(comp)
        molarMass = eval(fcomp)

        return molarMass

