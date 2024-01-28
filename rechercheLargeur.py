#Initialisation
def initialiser_taquin():
    global T
    T=[
        '___________________',
        '|     |     |     |',
        '|  8  |  2  |  3  |',
        "|_____|_____|_____|",
        "|     |     |     |",
        "|  1  |  6  |     |",
        "|_____|_____|_____|",
        "|     |     |     |",
        "|  7  |  5  |  4  |",
        "|_____|_____|_____|"
    ]

#Trouver la position du zéro
def position_zero(tab):
    for i in range(len(tab)):
        if tab[i] == 0:
            return i
    return -1

#Affichage du taquin
def afficher_taquin(tab):
    global T
    pos = 0
    for ch in T:
        if ch == T[2]:
            T[2] = "|  "+str(tab[pos])+"  |  "+str(tab[pos + 1])+"  |  "+str(tab[pos + 2])+"  |"
            pos += 3
            print(T[2])
        elif ch == T[5]:
            T[5] = "|  "+str(tab[pos])+"  |  "+str(tab[pos + 1])+"  |  "+str(tab[pos + 2])+"  |"
            pos += 3
            print(T[5])
        elif ch == T[8]:
            T[8] = "|  "+str(tab[pos])+"  |  "+str(tab[pos + 1])+"  |  "+str(tab[pos + 2])+"  |"
            pos += 2
            print(T[8])
        else:
            print(ch)

#Permutation deux cases
def deplacer_cases(tab, i, j):
    c = tab[i]
    d = tab[j]
    tab[i] = d
    tab[j] = c
    pos = 0
    print("Les valeurs déplacées : ", tab[i], " et ", tab[j])
    return tab

#Trouver les deplacements possibles
def deplacements_possibles(T1, pos1, pos2):
    if pos1 in [2, 5] and pos2 == pos1 + 1:
        return False
    elif pos1 in [3, 6] and pos2 == pos1 - 1:
        return False
    elif pos2 > 8 or pos2 < 0:
        return False
    else:
        return True

#Modification de la liste les deplacements possibles
def ajouter_deplacements_possibles(T1, pos1):
    b1 = deplacements_possibles(T1, pos1, pos1 + 1)
    b2 = deplacements_possibles(T1, pos1, pos1 - 1)
    b3 = deplacements_possibles(T1, pos1, pos1 - 3)
    b4 = deplacements_possibles(T1, pos1, pos1 + 3)
    T3 = []
    if b1:
        T3.append(pos1 + 1)
    if b2:
        T3.append(pos1 - 1)
    if b3:
        T3.append(pos1 - 3)
    if b4:
        T3.append(pos1 + 3)
    return T3

#Test but
def est_objectif(etat):
    if etat == [1, 2, 3, 8, 0, 4, 7, 6, 5]:
        return True
    else:
        return False

#MAJ taquin après deplacement
def mettre_a_jour_taquin(i):
    def ajouter_aux_deplacements_possibles(deplacements_possibles, position):
        def est_visite(tab):
            for d in FERMÉ:
                if d == tab:
                    return True
            return False

        global OUVERT
        for j in deplacements_possibles:
            tab1 = list(OUVERT[i])
            tab = deplacer_cases(tab1, position, j)
            if not est_visite(tab):
                OUVERT.append(tab)
                afficher_taquin(tab)

    global OUVERT
    global FERME
    position_zero = position_zero(OUVERT[i])
    deplacements_possibles = ajouter_deplacements_possibles(OUVERT[i], position_zero)
    FERME.append(OUVERT[i])
    ajouter_aux_deplacements_possibles(deplacements_possibles, position_zero)
    del OUVERT[0]

#Recherche en largeur
def recherche_en_largeur():
    global FERME
    global OUVERT
    while len(OUVERT) != 0:
        if est_objectif(OUVERT[0]):
            afficher_taquin(OUVERT[0])
            print("Noeuds parcourus = ", len(OUVERT) + len(FERMÉ))
return OUVERT[0]
else:
mettre_a_jour_taquin(0)
return []

T1 = []
T = []
initialiser_taquin()
OUVERT = [[8, 1, 3, 7, 2, 4, 0, 6, 5]]
afficher_taquin(OUVERT[0])
FERME = []
print("Le résultat final en recherche en largeur est : ", recherche_en_largeur())
n = input("Est-ce que le résultat est correct? [O/N]: ")
