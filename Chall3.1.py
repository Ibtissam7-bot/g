#########CHALLENGE1
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]
notes_1=[]
somme=0
for note in notes:
    somme= note+somme
moyenne=somme/len(notes)
#print(moyenne)
for note in notes:
    if note>moyenne:
        notes_1.append(note)
        print(f"{note} est supérieure à la moyenne {moyenne}")
    else :
        continue
print("La liste qui stocke les nombres supérieur à la moyenne est:")
print(notes_1)


############CHALLENGE 2
Ch1 = "Le langage Python est très populaire"
Ch2 = "Python est un langage puissant"
Ch11=Ch1.split()
Ch22=Ch2.split()
Ch3=[]
for i in Ch11:
    for j in Ch22:
        if i==j:
            Ch3.append(i)
print(f"Les mots communs entre deux chaînes de caractères Ch1 et Ch2 sont:{Ch3}")
print(Ch3)

########CHALLENGE 3
stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]
print(stock)
chaine=[]
num=[]
for s in stock:
    if type(s)== str:
        chaine.append(s)
    elif type(s)== int:
        num.append(s)
print(chaine,num)
TR1= sorted(chaine)
TR2 = sorted(num, reverse=True)
print(TR1)
print(TR2)

##########Challenge4
def rechercheElement(elem,liste):
    for i in range(len(liste)):
        if liste[i]== elem:
            return i
    return False
print(rechercheElement("ana",["Nom","moi",1,4]))
print(rechercheElement("moi",["Nom","moi",1,4]))

##########Challenge 5
L = [7 , 23 , 5 , 23 , 7 , 19 , 23 , 12 , 29]
a= 23
count=0
for i in L:
    if i==a:
        count+=1
print(f"Le nombre {a} apparaît {count} fois.")



