hauteur = int(input("veuillez entrer la hauteur :" ))
largeur = int(input("veuillez entrez la largeur :" ))

separateur = "-"
side = "|"

for i in range (hauteur):
    if i == 0 :
        print(side + separateur * largeur + side)
    elif i == hauteur-1:
        print(side + separateur * largeur + side)
    else:
        print (side + " " * largeur + side)