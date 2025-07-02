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


