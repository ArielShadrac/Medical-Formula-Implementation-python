# Posm = [Na+× 2] + Glycémie (mmol/L) = 285 mOsm/kg d’eau
# Source Néphrologie 9e édition, R2C 2020

def Posm(Na, Gly):
    return (Na*2 + Gly)