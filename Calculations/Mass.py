from Calculations.MolarMass import calculateMolarMass

def calculateMass(formula, mols):
    mm = calculateMolarMass(formula)
    mass = float(mols) * float(mm)
    return mass