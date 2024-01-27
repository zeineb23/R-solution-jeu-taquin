#Initialisation du taquin
def Initialisation():
    ch1= '___________________';
    ch2= '|     |     |     |';
    ch3= '|  8  |  2  |  3  |';
    ch4= "|_____|_____|_____|";
    ch5= "|     |     |     |";
    ch6= "|  1  |  6  |     |";
    ch7= "|_____|_____|_____|";
    ch8= "|     |     |     |";
    ch9= "|  7  |  5  |  4  |";
    ch10="|_____|_____|_____|";
    global T;
    T=[ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9,ch10];


#Trouve la position du zéro
def zero(tab) :
        for i in range(0,len(tab)) :
            if (tab[i]==0) :
                return i;
        return -1;

#Affichage du taquin
def affiche(tab) :
    global T;
    pos=0;
    for ch in T :
        if(ch==T[2]) :
            T[2]="|  "+str(tab[pos])+"  |  "+str(tab[pos+1])+"  |  "+str(tab[pos+2])+"  |";
            pos=pos+3;
            print(T[2]);

        elif (ch==T[5]):
                T[5]="|  "+str(tab[pos])+"  |  "+str(tab[pos+1])+"  |  "+str(tab[pos+2])+"  |";
                pos=pos+3;
                print(T[5]);

        elif(ch==T[8]):
                T[8]="|  "+str(tab[pos])+"  |  "+str(tab[pos+1])+"  |  "+str(tab[pos+2])+"  |";
                pos=pos+2;
                print(T[8]);

        else :
                print(ch);
                

#Déplacement de deux cases
def TestDeplacement(tab,i,j) :
    c=tab[i];
    d=tab[j];
    tab[i]=d;
    tab[j]=c;
    pos=0;
    print("Les valeurs deplacées : ",tab[i]," et ",tab[j]);
    return tab;

#Trouver les déplacements possibles
#pos1 : position du zero
def PossibiliteDeplacement(T1,pos1,pos2) :
    if (pos1 in [2,5] and pos2==pos1+1) :
        
        return False;
    elif (pos1 in [3,6] and pos2==pos1-1) :
       
        return False;
    elif (pos2 >8 or pos2<0) :
        
        return False;
    else :
        
        return True;


#Ajouter les déplacment possibles
#pos1 position du zero
def DeplacementsPossibles(T1,pos1) :
    b1=PossibiliteDeplacement(T1,pos1,pos1+1);
    b2=PossibiliteDeplacement(T1,pos1,pos1-1);
    b3=PossibiliteDeplacement(T1,pos1,pos1-3);
    b4=PossibiliteDeplacement(T1,pos1,pos1+3);
    T3=[];
    if(b1) :
        T3.append(pos1+1);
    if(b2) :
        T3.append(pos1-1);
    if(b3):
        T3.append(pos1-3);
    if(b4) :
        T3.append(pos1+3);
    return T3;



#Fonction test but
def isGoal(Etat) :
    if (Etat==[1,2,3,8,0,4,7,6,5]):
        return True;
    else :
        return False;



#Mise a jour du taquin après déplacement
def update1() :
    def ajoutDansOPEN(TD,pos) :

        def parcouru(tab) :
            for d in CLOSED :
                if(d==tab) :
                    return True;
            return False;
        
        global OPEN;
        OP=[];
        for i in range(0,len(OPEN[0])) :
            OP.append(OPEN[0][i]);
            
        del OPEN[0];
        affiche(OP)
        for j in TD :   
            tab1=[];
            for x in range(0,len(OP)):
                tab1.append(OP[x]);
            T=[];
            tab=TestDeplacement(tab1,pos,j);
            if(not(parcouru(tab))) :
                T.append(tab);
            for i in OPEN :
                T.append(i);
            OPEN=T;

            
    global OPEN;
    global CLOSED;
    pos1=zero(OPEN[0]);
    TD = DeplacementsPossibles(OPEN[0],pos1);
    CLOSED.append(OPEN[0]);
    ajoutDansOPEN(TD,pos1);
    

def RechercheProfondeur(T1) :
    global OPEN;
    global CLOSED;
    while(len(OPEN)!=0) :
        if(isGoal(OPEN[0])) :
           affiche(OPEN[0]);
           print("Noeuds parcourus = ",len(OPEN)+len(CLOSED));
           return OPEN[0];
        else :
            update1();
    return [];
     
       
T1=[];
T=[];
Initialisation();
OPEN=[[8,1,3,7,2,4,0,6,5]];
affiche(OPEN[0]);
CLOSED=[];
print("Le resultat final en recherche en profondeur est : ", RechercheProfondeur(T1));
n=input("Est-ce que le résultat est correct? [O/N]");
