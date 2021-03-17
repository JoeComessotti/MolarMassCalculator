from Calculations.MolarMass import calculateMolarMass

#This function takes the formula of the substance, as well as the mass and multiplies them
#to return the number of mols.
def calculateMols(formula, mass):
    mm = calculateMolarMass(formula)
    mols = float(mass) / float(mm)
    return mols