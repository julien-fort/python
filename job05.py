#boucle for
v1 = input('entrez une valeur : ')
v2 = input('entrez une valeur : ')
n1=int(v1)
n2=int(v2)
for i in range (n1+1, n2) : 
      print (i)
for i in range (n1-1, n2, -1) :
      print (i)
if  n1 == n2:
    print ("vi et v2 sont de la même valeur")      
