
# coding: utf-8

import math
from collections import OrderedDict

Input = "v ubcfb osu ymoqsuu n cxqfj dqmfnu ub vjcfqu juz amqjmruz zmsscfusb bquflu auoquz hfszbms zwfba ju wusbms qusbqu ncsz ju vmo z uddmqvcfb n uxfbuq ju xusb wcoxcfz fj eczzc qcefnuwusb jc emqbu xfbquu no ijmv nuz wcfzmsz nu jc xfvbmfqu ecz czzul qcefnuwusb vueusncsb emoq uweuvauq kou zusrmoddqu us wuwu buwez kou jof os bmoqifjjms nu emozzfuqu ub nu zcijuju acjj zusbcfb ju vamo vofb ub ju xfuog bcefz c j osu nu zuz ugbquwfbuz osu cddfvau nu vmojuoqbqme xczbu emoq vu nuejmfuwusb fsbuqfuoq ubcfb vjmouu co woq ujju quequzusbcfb zfwejuwusb osusmqwu xfzcru jcqru nu ejoz n os wubqu ju xfzcru n os amwwu n usxfqms kocqcsbu vfsk csz c juecfzzu wmozbcvau smfqu cog bqcfbz cvvusbouz ub iucoghfszbms zu nfqfruc xuqz j uzvcjfuq fj ubcfb fsobfju n uzzcpuq nu equsnqu j czvuszuoq wuwu coxwufjjuoquz uemkouz fj dmsvbfmsscfb qcquwusb cvboujjuwusb n cfjjuoqz ju vmoqcsb ujuvbqfkou ubcfbvmoeu ncsz jc ymoqsuu v ubcfb osu nuz wuzoquz n uvmsmwfu eqfzuz us xou nu jc zuwcfsu nu jc acfsuzms ceecqbuwusb ubcfb co zuebfuwu hfszbms kof cxcfb bqusbu suod csz ub zmoddqcfb n os ojvuquxcqfkouog co nuzzoz nu jc vauxfjju nqmfbu wmsbcfb jusbuwusb fj z cqqubc ejozfuoqz dmfz us vauwfsemoq zu quemzuq c vackou ecjfuq zoq osu cddfvau vmjjuu co woq dcvu c jc vcru nu j czvuszuoq jusmqwu xfzcru xmoz dfgcfb no qurcqn v ubcfb os nu vuz emqbqcfbz cqqcsruz nu bujju zmqbu kou juzpuog zuwijusb zofxqu vujof kof eczzu osu jurusnu zmoz ju emqbqcfb nfzcfb ifr iqmbauq xmoz qurcqnuc j fsbuqfuoq nu j ceecqbuwusb nu hfszbms osu xmfg zovquu dcfzcfb usbusnqu osu zuqfu nu smwiquzkof cxcfusb bqcfb c jc eqmnovbfms nu jc dmsbu jc xmfg eqmxuscfb n osu ejckou nu wubcj mijmsrouwfqmfq buqsu usvczbqu ncsz ju woq nu nqmfbu hfszbms bmoqsc os imobms ub jc xmfg nfwfsoc nu xmjowuwcfz juz wmbz ubcfusb usvmqu nfzbfsvbz ju zms nu j ceecqufj no bujuvqcs vmwwu ms nfzcfb emoxcfbubqu czzmoqnf wcfz fj s p cxcfb covos wmpus nu j ubufsnqu vmwejubuwusb hfszbms zu nfqfruc xuqz jcdusubqu fj ubcfb nu zbcboqu dquju ejobmb eubfbu ub zc wcfrquoq ubcfb zmojfrsuu ecq jc vmwifscfzms ijuou osfdmqwu no ecqbf fj cxcfb juz vauxuog bquz ijmsnz ju xfzcru scboqujjuwusb zcsrofs jc euco noqvfu ecq ju zcxms rqmzzfuq juz jcwuz nu qczmfq uwmozzuuz ub ju dqmfn nu j afxuq kof xuscfb nu equsnqu dfs"


# In[260]:


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
    compteur = 0
    fin = len(Liste)
    for i in range(len(Liste)):
        print(compteur,"/",fin)
        compteur+=1
        temp = check(str(Liste[i]), contenu)
        if temp>best:
            best = temp
            besti=i
    print("Nous avons trouvé une solution plausible avec", best, "occurences de mots de la langue française :\n")        
    return (besti)


# In[261]:


def combinatoire(Input, mot):
    if len(Input) == 0 :
        if possible(mot):
            return [mot]
        else : 
            return ['']
    Liste = []
    for elem in Input[0]:
        if elem not in mot:
            Liste = Liste + combinatoire(Input[1:], mot+elem)
    return Liste

def Combinatoire(Input):
    return combinatoire(Input, "")


# In[262]:


def Match(a,b):
    m = min(a,b)/max(a,b)
    if m > 0.30:
        return True
    return False


# In[263]:


def possible(chaine):
    for i in range(len(chaine)-1):
        for e in range(i+1, len(chaine)):
            if chaine[i] == chaine[e]:
                return False
    return True


def Possibles(Liste):
    return [x for x in Liste if possible(x)]


# In[264]:


def Decode(Input, possibility):
    Freq = getFreq(Input)    
    dico={}
    for i in range(len(possibility)):
        dico[Freq[i][0]] = possibility[i]
    Liste = list(Input)
    for i in range(len(Liste)):
        if Liste[i] in dico:
            Liste[i] = dico[Liste[i]]
    return("".join(Liste))


# In[265]:


def ListofPossibles(Distribution1, Distribution2, Input):
    
    mon_fichier = open("liste_francais.txt", "r")
    contenu = mon_fichier.readlines()
    Liste = []
    i = 0
    for elem1 in Distribution1:
        Liste.append([])
        for elem2 in Distribution2:
            if Match(elem1[1], elem2[1]):
                Liste[i].append(elem2[0])
        if Distribution2[i][0] not in Liste[i]:    
            Liste[i].append(Distribution2[i][0])
        if Distribution1[i][0] == '':
            Liste[i]=[]
        i += 1

    Liste[25] = ['e']
    Liste[24] = ['a']
    Liste[23] = ['i']
    Liste[22] = ['t']
    Liste[21] = ['r']
    Liste[20] = ['n']
    Liste[19] = ['s']
    Liste[18] = ['u']
    Liste[17] = ['l']
    Liste[16] = ['o']
    Liste[15] = ['d']
    Liste[12] = ['p']    
    Liste[11] = ['v']
    Liste[10] = ['f']
    Liste[9] = ['g']
    Liste[8] = ['h']
    Liste[3] = ['y']
    Liste[1] = ['j']
   
    for i in range(len(Liste)-1):
   		print(Distribution1[i+1], Liste[i])

    toRemove = []
    #On supprime les allocations impossible dès maintenant
    for clas in Liste:
        if len(clas) == 1:
            toRemove.append(clas[0])
    
    for rm in toRemove:
        for elem in Liste:
            if len(elem) > 1 and rm in elem:
                elem.remove(rm)
    toRemove = []
    


    #On supprime les allocations impossible dès maintenant
    for clas in Liste:
        if len(clas) == 1:
            toRemove.append(clas[0])
        if len(clas) == 0:
            Liste.remove(clas)
    
    for rm in toRemove:
        for elem in Liste:
            if len(elem) > 1 and rm in elem:
                elem.remove(rm)

    # On enleve les possibilités qui n'ajoute pas de mots du dictionnaire
    Essai = []
    for elem in Liste:
        if len(elem)>0:
            Essai.append(elem[0])

    for i in range(len(Liste)):
        #print(Distribution1[i][0], Liste[i])
        dictionette = {}
        if len(Liste[i]) > 50 :
            for elem in Liste[i]:
                Essai[i] = elem
                dictionette[elem] = (check(Decode(Input, Essai),contenu))
            dictionette = sorted(dictionette.items(), key=lambda t: t[1])
            #print(dictionette)
            Liste[i]= []
            Liste[i].append(dictionette[len(dictionette)-1][0])
            Liste[i].append(dictionette[len(dictionette)-2][0])
            Liste[i].append(dictionette[len(dictionette)-3][0])
            Liste[i].append(dictionette[len(dictionette)-4][0])
            Liste[i].append(dictionette[len(dictionette)-5][0])

            Essai[i] = dictionette[len(dictionette)-1][0]
            
    toRemove = []
    #On supprime les allocations impossible dès maintenant
    for clas in Liste:
        if len(clas) == 1:
            toRemove.append(clas[0])
    
    for rm in toRemove:
        for elem in Liste:
            if len(elem) > 1 and rm in elem:
                elem.remove(rm)
    toRemove = []
    
    #On supprime les allocations impossible dès maintenant
    for clas in Liste:
        if len(clas) == 1:
            toRemove.append(clas[0])
        if len(clas) == 0:
            Liste.remove(clas)
    
    for rm in toRemove:
        for elem in Liste:
            if len(elem) > 1 and rm in elem:
                elem.remove(rm)
    
    for i in range(len(Liste)):
    	print(i, Distribution1[i+1], Liste[i])    
    
    return Possibles(Combinatoire(Liste))


# In[266]:


def getDistributions(Input):
    Length = 0
    for elem in Input:
        if elem != ' ':
            Length += 1
    Liste = []
    dico = {}
    true_freq = {'a': 0.07880126313182391, 'b': 0.009298053703741926, 'c': 0.03364223648634703, 'd': 0.037862995603805905, 'e': 0.15185445088852656, 'f': 0.011000804936946607, 'g': 0.008936864048213658, 'h': 0.0076056221749809085, 'i': 0.07769705475635177, 'j': 0.00562423892179728, 'k': 0.0005056655177395719, 'l': 0.05630430744463479, 'm': 0.030628882788796927, 'n': 0.07321830302780129, 'o': 0.05549937049802894, 'p': 0.031175827124311162, 'q': 0.014055437452271367, 'r': 0.067625023219335, 's': 0.08202101091824732, 't': 0.07475593898990733, 'u': 0.06512765474396813, 'v': 0.016800478834286186, 'w': 0.0011764463065777795, 'x': 0.003993725619698252, 'y': 0.003178468968648738, 'z': 0.0014034798043384038}    
    for elem in true_freq:
        true_freq[elem] = true_freq[elem]*Length

    for elem in Input:
        if elem != ' ':
            if not elem in dico:
                dico[elem] = 1
            else:
                dico[elem] += 1
    dico = sorted(dico.items(), key=lambda t: t[1])
    true_freq = sorted(true_freq.items(), key=lambda t: t[1])

    #for i in range(1, len(dico)+1):
    #    print(dico[len(dico)-i], true_freq[len(true_freq)-i])
        
    for i in range(len(true_freq)-len(dico)):
        dico.insert(0,('',0))
        
    return ListofPossibles(dico, true_freq, Input)    


# In[267]:


def getFreq(Input):
    dico = {}
    for elem in Input:
        if elem != ' ':
            if not elem in dico:
                dico[elem] = 1
            else:
                dico[elem] += 1
    dico = sorted(dico.items(), key=lambda t: t[1])
    return dico


# In[268]:


def resoudreTexte(Input):

    print("Computing ... ")
    Possibilities = getDistributions(Input)
    ListeOut = []        
    Freq = getFreq(Input)
    print("Il y a",len(Possibilities), "possibilités")
    print("Etape 1")
    print()
    compteur = 0
    fin = len(Possibilities)
    for possibility in Possibilities:
        print(compteur,"/", fin)
        compteur += 1
        possibility = list(possibility)
        dico = {}
        for i in range(len(possibility)):
            dico[Freq[i][0]] = possibility[i]
        # On a un dictionnaire representant l'assignation des transpositions
        Liste = list(Input)
        for i in range(len(Liste)):
            if Liste[i] in dico:
                Liste[i] = dico[Liste[i]]
        ListeOut.append("".join(Liste))
    print("Etape 2")
    print()
    res = chooseBest(ListeOut)

#print(Input)
    for i in range(len(Possibilities[res])):
        dico[Freq[i][0]] = Possibilities[res][i]
    for elem in dico:
    	print(elem, "-->", dico[elem])

    print(list(Possibilities[res]))

    return ListeOut[res]


print(resoudreTexte(Input))


# In[132]:


#Bigrammes
#dico2 = {}
#for i in range(len(Input)-1):
#    if Input[i] == Input[i+1]:
#        if Input[i:i+2] not in dico2:
#            dico2[Input[i:i+2]] = 0
#        dico2[Input[i:i+2]] += 1
#dico2 = sorted(dico2.items(), key=lambda t: t[1])
#true_bi = [('ff',8),('pp',10),('rr',16),('mm',17),('nn',20),('tt',24),('ll',29),('ee',66),('ss',73)]
#sum_true_bi = 0
#for i in range(len(true_bi)):
#    sum_true_bi+=true_bi[i][1]
#sum_bi = 0
#for i in range(len(dico2)):
#    sum_bi+=dico2[i][1]
#            
#for i in range(len(dico2)):
#    print(dico2[i][0], dico2[i][1]/sum_bi, "    Expected    ", true_bi[i][0], true_bi[i][1]/sum_true_bi)


