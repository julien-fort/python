def findMultiples(n):
    a = 3 # garder les multiples de 3
    b = 5 # garder les multiples de 5
    for i in range(0,100+1):
        s = ""
 
        # Trouver les multiples de 3
        if (i == a):
            a = a + 3 # Mettre à jour ensuite multiple de 3
            s = s + "Fizz"
         
        # trouver les multiples de 5
        if (i == b):
            b = b + 5 # Mettre à jour ensuite multiple de 5
            s = s + "Buzz"
        if (s == ""):
            print(i)
        else:
            print(s) 
 
# code conducteur
if __name__ == '__main__':
    findMultiples(20)