# coding: utf-8
import math
from collections import OrderedDict

def check(phrase, contenu):
    compt = 0
    for mot in contenu:
        if (phrase.find(mot[:-1])>-1):
            compt = compt +1
    return compt

def chooseBest(Liste):
    mon_fichier = open("liste_francais.txt", "r")
    contenu = mon_fichier.readlines()
    best = 0
    besti = 0
    for i in range(len(Liste)):
        temp = check(str(Liste[i]), contenu)
        if temp>best:
            best = temp
            besti=i
    print("Nous avons trouvé une solution plausible avec", best, "occurences de mots de la langue française :\n")        
    return (Liste[besti], besti)


def completeString(Input, T, l):
    k = T - len(Input)
    L = list(Input)
    for r in range(k):
        L.insert(T-(r)*l, "*")

    Output = "".join(L)
    return Output


def permutationScytale(Input, l):
    
    M = len(Input)
    c = math.ceil(len(Input)/l)
    T = c*l    
    Input = completeString(Input, T,l)
    Output = ""
    for i in range(M):
        Output = Output + Input[(i*c)%(T) + int(i*c/T)]
    return(Output)   

def loss(Input):
    Liste = list(Input)
    Lenght = len(Input)
    Output = []
    occ = {}
    true_freq = {'a': 0.07880126313182391, 'b': 0.009298053703741926, 'c': 0.03364223648634703, 'd': 0.037862995603805905, 'e': 0.15185445088852656, 'f': 0.011000804936946607, 'g': 0.008936864048213658, 'h': 0.0076056221749809085, 'i': 0.07769705475635177, 'j': 0.00562423892179728, 'k': 0.0005056655177395719, 'l': 0.05630430744463479, 'm': 0.030628882788796927, 'n': 0.07321830302780129, 'o': 0.05549937049802894, 'p': 0.031175827124311162, 'q': 0.014055437452271367, 'r': 0.067625023219335, 's': 0.08202101091824732, 't': 0.07475593898990733, 'u': 0.06512765474396813, 'v': 0.016800478834286186, 'w': 0.0011764463065777795, 'x': 0.003993725619698252, 'y': 0.003178468968648738, 'z': 0.0014034798043384038}

    loss = 0
    for elem in Liste:
        if elem in occ:
            occ[elem]+=1
        else:
            occ[elem]=1
            
    for elem in occ:
        if elem in true_freq:
            loss += (occ[elem]- (true_freq[elem] * Lenght))**2
        else :
            loss += 1000
    return(loss)             
            

# On peut ameliorer enormement le temps de de calcul en faisant un pretraitement de Liste 
# par comparaison des distributinons des lettres avant de chercher des mots du dictionnaire
def resoudreScytale(Input):

    # Ce parametre permet de reduire l'ensemble des possibles à SIMPLIFICATION avant de
    # l'envoyer à chooseBest qui regarde les occurences des mots du dictionnaires afin de
    # choisir le meilleur.
    # La fonction chooseBest etant très efficace mais très couteuse en temps de calcul
    # On peut reduire les elements qu'elle a a traiter en diminuant SIMPLIFICATION
    # Cette reduction se faire en calculant une loss entre la distribution des lettres
    # dans l'entrée et selon la distribution attendue.
    # 10 semble être une valeur être une valeur raisonnable qui renvoie les bons résultats
    # sur nos tests et permet de resoudre le problème en quelques centaines de milisecondes.
    # Il est imperatif de changer cette valeur si le programme renvoie des resultats incoherents
    SIMPLIFICATION = 10


    Input = Input.lower()
    Liste = []
    for i in range(1, len(Input)-1):
        Liste.append(permutationScytale(Input,i))

    Losses = {}
    for elem in Liste:
        Losses[elem] = loss(elem[0])
    Losses = sorted(Losses.items(), key=lambda t: t[1])
    Output = []
    for i in range(SIMPLIFICATION):
        if(len(Losses)>i):
            Output.append(Losses[i][0])
    (Out,Taille) = chooseBest(Output)

    print("La taille du Scytale est :", Taille)
    return Out
        
print()        
print("TESTS")

Input="BOOOUMNRJT"
print(resoudreScytale(Input))

Input="BOOUNRJT"
print(resoudreScytale(Input))

print()
print()


Input = "lelnracsrunanatuvllerrmcnjeeaeseiaetanctsagsgeemftqdnnentraraueneciliianeredofaesntdneenignpcdaishdcaoaeenede"
print("Example TP")
print(Input)
print(resoudreScytale(Input))