from Calculations.MolarMass import calculateMolarMass

def calculateMols(formula, mass):
    mm = calculateMolarMass(formula)
    mols = float(mass) / float(mm)
    return mols