
#Recherche profondeur
def recherche_profondeur():
    global OUVERT
    global FERMÉ
    while len(OUVERT) != 0:
        if est_objectif(OUVERT[0]):
            afficher_taquin(OUVERT[0])
            print("Noeuds parcourus = ", len(OUVERT) + len(FERMÉ))
            return OUVERT[0]
        else:
            mise_a_jour_taquin()
    return []


T1 = []
T = []
initialiser_taquin()
OUVERT = [[8, 1, 3, 7, 2, 4, 0, 6, 5]]
afficher_taquin(OUVERT[0])
FERMÉ = []
print("Le résultat final en recherche en profondeur est : ", recherche_profondeur())
n = input("Est-ce que le résultat est correct? [O/N]: ")
