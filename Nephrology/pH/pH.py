import numpy as np

def Calculate_pH(HCO3,PCO2):
    pH = 6.1 + np.log((HCO3/0.03)*PCO2)
    return pH