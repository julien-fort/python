hauteur = int(input("veuillez entrer la hauteur :" ))
for i in range(0, hauteur):
    print ((hauteur-i) * " " + "/" + (i*2) * " " + "\\") # multiplication et + signifie la concaténation (, sous python)
print (((hauteur +1)*2)*"-")