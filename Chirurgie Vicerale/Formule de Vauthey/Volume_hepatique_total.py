import numpy as np




def VautheyFormula(taille,poids):
    surface_corporelle = np.sqrt(taille*poids/3.6)
    volume_hepatique = (surface_corporelle*1267.28) -794.41
    return volume_hepatique