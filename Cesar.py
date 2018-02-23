import math

def cesar(d, text):
    text = list(text)
    for i in range(len(text)):
        
        temp = ord(text[i])+d
        if (temp > 122):
            temp = temp - 122 + 96
        if (temp < 97):
            temp = temp + 26   
        text[i] = chr(temp)

    return("".join(text))



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
    



def resoudreCesar(Input):
    Liste = []
    for i in range(25):
        Liste.append(str(cesar(i, Input)))
    (OUT,clef) =  chooseBest(Liste)

    print()
    print("La clef est :",clef)
    print()
    return OUT
    

print()
print()

Input = "vcfgrwqwfsbhfsntowbsobgfsbhfsnqvsnjcigsghqsoixcifrviwtshseicwbsgojsnjcigdogeisjcigoihfsgofhwgobgjcigbsrsjsnqwfqizsfrobgzsgfisgzsgxcifgcijfopzsgeiojsqzsggwubsgrsjchfsdfctsggwcbdofzseiszsghhcbashwsf"
print("Premier Message")
print(Input)
print(resoudreCesar(Input))

print()
print()

print("Second Message")
print(Input)
Input2 = "hcihszouoizssghrwjwgsssbhfcwgdofhwsgrcbhzibssghvopwhssdofzsgpszusgzoihfsdofzsgoeiwhowbgzohfcwgwsasdofqsileiwrobgzsifzobuisgsbcaasbhqszhsgshrobgzobchfsuoizcwg"
print(resoudreCesar(Input2))

print()
print()