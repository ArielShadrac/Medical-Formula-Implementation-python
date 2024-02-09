# Paediatic Glalgow Coma scale
# Source : Wikipedia

def Score(Eye=1, Voice=1, Motor=1):
    score =  Eye + Voice + Motor
    if Eye <1 or Eye >4:
        raise Exception("l'ouverture des yeux est comprise entre 1 et 4")
    if Voice <1 or Voice >5:
        raise Exception("la reponse verbale est comprise entre 1 et 5")
    if Motor <1 or Motor >6:
        raise Exception("la reponse motrice est comprise entre 1 et 6")
    if 14<=score<=15:
        print("Conscience Normal")
    elif 10<=score<=14:
        print("Somnolence ou coma leger")
    elif 7<=score<=9:
        print("Coma Lourd")
    else:
        print("Coma profond ou mort clinique")
