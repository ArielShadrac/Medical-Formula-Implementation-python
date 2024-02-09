import numpy as np
from rich.console import Console

console = Console()

def Teab(ph):
    if ph<7.38:
        print('Acidose')
    elif ph>7.42:
        print('Alcalose')
    else:
        print('Normal')

def metabolic_acidose(ph, HCO3, PCO2):
    if ph<7.38 and HCO3<22 and PCO2<35:
        console.print('Urgence Vitale', style='red')
    elif ph<7.10 or HCO3<8:
        print('Acidose metabolique')
    else:
        print('Normal')



# print(Trou_ionique(10,5,35))