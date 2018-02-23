# coding: utf-8
import math
from collections import OrderedDict
from functools import reduce

def f(a,b,x):
    return (a*x+b) %26

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
        temp = check(str(Liste[i][0]), contenu)
        if temp>best:
            best = temp
            besti=i
    print("Nous avons trouvé une solution plausible avec", best, "occurences de mots de la langue française.\n")        
    mon_fichier.close()
    return (Liste[besti])
    

def CodeVigenere(Input, clef):
    Output = ""
    for i in range(len(Input)):
        Output+= chr( ((ord(Input[i])-96) + (ord(clef[i%len(clef)])-96)) %26 +96)
    Output = Output.replace("`","z")
    return Output


def DecodeVigenere(Input, clef):
    Output = ""
    for i in range(len(Input)):
        Output+= chr( ((ord(Input[i])-96) - (ord(clef[i%len(clef)])-96)) %26 +96)
    Output = Output.replace("`","z")
    return Output


def div(a):
    for i in range(1,a):
        if a%(a-i) == 0:
            return a-i
    return 1


def distances(Input):
    poly = {}
    dist = []
    for i in range(len(Input)-3):
        if Input[i:i+2] in poly :
            if not Input[i+1:i+3] in poly:
                dist.append(i-poly[Input[i:i+2]])
            else :
                if not (poly[Input[i+1:i+3]] - poly[Input[i:i+2]] == 1):
                    dist.append(i-poly[Input[i:i+2]])
        poly[Input[i:i+2]] = i
    redo = []
    for i in range(len(dist)-1):
        if div(dist[i]) > 1:
            redo.append(dist[i])
            
    redo = list(set(redo))
    return(redo)



def GCD(a,b):
    """ The Euclidean Algorithm """
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b
        
        
def pgcd(list):
    if len(list) == 0:
        return 1
    return reduce(GCD, list)



def facteurs(x):
    Out = []
    for i in range(2,x+1):
        if x%i == 0:
            Out.append(i)
    return Out


def transpose(M,w):
    M=list(M)
    Output = ""
    for elem in M:
        Output+= chr(f(1,-w,ord(elem)-97)+97)
    return Output


# In[297]:


def loss(Input):
    Liste = list(Input)
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
        loss += (occ[elem]- true_freq[elem]*len(Input))**2
        #print(elem," : ", occ[elem], true_freq[elem]*len(Input))
    return(loss)


def resoudreMonoAlpha(Input, patho):
    Seuil = 3
    if patho:
        Seuil = 10
    Losses= {}
    for w in range(26):
        temp = transpose(Input,w)
        w = chr(w+96).replace("`","z")
        Losses[w] = loss(temp)
        #print(w, loss(temp), temp)
    Losses = sorted(Losses.items(), key=lambda t: t[1])
    Output = []
    for i in range(Seuil):
        Output.append(Losses[i][0])
    return Output


def combinatoire(Input, mot):
    if len(Input) == 0 :
        return [mot]
    Liste = []
    for elem in Input[0]:
        Liste = Liste + combinatoire(Input[1:], mot+elem)
    return Liste


def Combinatoire(Input):
    return combinatoire(Input, "")


def resoudrePolyAlpha2(Input, n):
    Mots = []
    Out = []
    Input = list(Input)
    for i in range(n):
        Mots.append("")
        Out.append([])
    for i in range(len(Input)):
        Mots[i%n]+=Input[i]    
    for i in range(len(Mots)):
        Out[i] = resoudreMonoAlpha(Mots[i], i == 1)
    Comb = Combinatoire(Out)
    Liste = []
    for word in Comb:
        temp = DecodeVigenere(Input, word)
        Liste.append((temp, word))
    Losses = {}
    for elem in Liste:
        Losses[elem] = loss(elem[0])
    Losses = sorted(Losses.items(), key=lambda t: t[1])
    Output = []
    for i in range(10):
        if(len(Losses)>i):
            Output.append(Losses[i][0])
    return chooseBest(Output)

def epurer2(Liste):
    dic = {}
    Liste.sort()
    for a in Liste:
        dic[a]=0
        for b in Liste:
            if b%a ==0:
                dic[a]+=1
    dic = sorted(dic.items(), key=lambda t: t[1])
    k = len(dic)-1
    #while k>0 and (dic[k-1][0] % dic[k][0]) == 0:
    #    k = k -1
    
    Output = []
    for elem in dic:
        if elem[1] > 1:
            Output.append(elem[0])
    return Output


# In[425]:


def bestFacteur(Liste):
    dico = {}
    
    Liste = epurer2(Liste)
    for elem in Liste:
        for fact in facteurs(elem):
            if fact in dico:
                dico[fact]+=1
            else:
                dico[fact] = 1
                
    dico = sorted(dico.items(), key=lambda t: t[1])
    
    i = len(dico)-1
    while i > 0:
        if dico[i][0] * dico[i -1][0] == dico[i -2][0]:
            dico.remove(dico[i])
            dico.remove(dico[i-1])
            i = i -1
        elif dico[i][0] == 2 or dico[i][0] == 3:
            dico.remove(dico[i])
        elif dico[i][0] * 2 == dico[i -1][0]:
            dico.remove(dico[i])

            
        i = i -1
    return dico[-1][0]


# In[438]:


def resoudrePolyAlpha(Input):
    mon_fichier = open("liste_francais.txt", "r")
    contenu = mon_fichier.readlines() 
    Liste = []
    dist = distances(Input)
    mult = pgcd(dist)
    if mult == 1:
        mult = bestFacteur(dist)
    print("Analyse terminée,",mult, "est un multiple de la taille de la clef.")
    for n in facteurs(mult):
        Liste.append((resoudrePolyAlpha2(Input, n)))
    print("Les solutions possibles ont été enumérées.")
    (Out,clef) = chooseBest(Liste) 
    while check(str(Out), contenu)/len(Input)<0.4 and mult < len(Input)/4:
        Liste = []
        mult = mult*2
        print("Resultat peu concluant, nous essayons avec ", mult, "comme facteur.")
        for n in facteurs(mult):
            if n not in facteurs(int(mult/2)):
                Liste.append((resoudrePolyAlpha2(Input, n)))
        print("Les solutions possibles ont été enumérées.")
        (Out,clef) = chooseBest(Liste)      

    print("La clef est :", clef)
    return Out


# In[439]:


clef = "abcdefghd"
Code = (CodeVigenere("ilfaudraitquejetrouveuntextepourfairedestestsafindevoirsimonalgomarchevramentpsksurdespetitestaillesilyatoujoursdescaspathologiquesetvoirsionpeutpasseralechellenetermedetempsdecalculilnefaudraitpasquecaprennedescentainesdanneesquandmeme", clef))
print(Code)
print(resoudrePolyAlpha(Code))


# In[440]:


Input = "iefomntuohenwfwsjbsfftpgsnmhzsbbizaomosiuxycqaelrwsklqzekjvwsivijmhuvasmvwjewlzgubzlavclhgmuhwhakookakkgmrelgeefvwjelksedtyhsgghbamiyweeljcemxsohlnzujagkshakawwdxzcmvkhuwswlqwtmlshojbsguelgsumlijsmlbsixuhsdbysdaolfatxzofstszwryhwjenuhgukwzmshbagigzzgnzhzsbtzhalelosmlasjdttqzeswwwrklfguzl"
print(resoudrePolyAlpha(Input))


# In[442]:


Input = "zbpuevpuqsdlzgllksousvpasfpddggaqwptdgptzweemqzrdjtddefekeferdprrcyndgluaowcnbptzzzrbvpssfpashpncotemhaeqrferdlrlwwertlussfikgoeuswotfdgqsyasrlnrzppdhtticfrciwurhcezrpmhtpuwiyenamrdbzyzwelzucamrptzqseqcfgdrfrhrpatsepzgfnaffisbpvblisrplzgnemswaqoxp!dseehbeeksdptdttqsdddgxurwnidbdddplncsd"
print(resoudrePolyAlpha(Input))
