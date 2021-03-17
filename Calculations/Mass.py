from Calculations.MolarMass import calculateMolarMass

#This function takes the formula of the substance as well as the number of moles and multiplies 
#them to return the mass of the substance.
def calculateMass(formula, mols):
    mm = calculateMolarMass(formula)
    mass = float(mols) * float(mm)
    return mass