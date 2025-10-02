# Exemple avec un seul exercice
import random
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2(nom):
    prenom = input("entrée prenom utilisateur :")
    print("bonjour",prenom)
def exercice3():   
    print("premiereligne \ndeuxieme ligne \ntroisième ligne")

def exercice4(année):
    age = 2025 - année
    return age

def exercice5(a,b):
        return a+b 

def exercice6(a,b):
        return a-b 

def exercice7(a,b):
        return a*b 

def exercice8(a,b):
        return a / b 

def exercice9(a):
        return a**2

def exercice10(a):
        return a*a

def exercice11(a):
        return a / 2 

def exercice12():
        a = print("hello"*5)
        return   

def exercice13():
      for i in range(1,6):
            print(i)
def exercice14():
      for i in range(1,6):
            print(2*i)
def exercice15(coté):
      return coté*4

def exercice16(coté):
      return coté*coté

def exercice17(euro):
      dollard = euro * 1.1
      return euro

def exercice18(minutes):
      seconde = minutes * 60
      return seconde

def exercice19(prixHT):
      prixTTC = prixHT * 1.2
      return prixTTC

def exercice20(age):
      print( "paul a ", age, "ans")

def exercice21(a):
    if a > 0 :
        print("positif")
    if a < 0 :
        print("negatif")
    else :
        print("nul")

def exercice12(age):
    if age < 18 :
        print("mineur")
    else :
          print("majeur")
    
def exercice23(notes):
    if notes < 10 :
        print("non validé")
    else : 
          print("validé")

def exercice24(a,b):
    if a > b :
        print(a , "est plus grand")
    if a < b :
         print(b , "est plus grand")
    else :
         print("meme nombre")

def exercice25(a,b):
    if a > b :
        print("non")
    if a < b :
         print("oui")
    else :
         print("meme nombre")

def exercice26(a):
    if a % 5 == 0 :
         print("divisible par 5")
    else :
         print("non divisible par 5")

def exercice27(a):
    if a < 12 :
        print("enfant")
    if a < 17 :
         print("adolescent")
    else :
         print("adulte")

def exercice28(a):
    if a < 0 :
        print("glace")
    if a < 100 :
         print("eau liquide")
    else :
         print("vapeur")

def exercice29(a):
    if a < 9 :
        print("recalé")
    if a < 12 :
         print("passable")
    if a < 15 :
         print("bien")
    else :
         print("trés bien")

def exercice30(N):
     for i in range(N+1):
          print(i)

def exercice31(N):
    for i in range(0, N+1):
        print(N-i)

def exercice32(N):
    a = 0
    for i in range(N+1):
        a += i
    print(a)
    
def exercice33(N):
    for i in range(10):
        print(i*N)

def exercice34(N):
     for i in range (0,N+1):
        if i == 0 :
             print(0)
        if i % 2 == 0 :
             print(i)

def exercice35(N):
    for i in range(1, int(N ** 0.5) + 1):
        print(i**2)

def exercice36(N):
    print("salut"*N)

def exercice37(h):
     print("*", "*"*2,"*"*3)

def exercice38(a,b):
    operation = input("1 for + ,2 for - , 3 for * , 4 for / ")
    if operation == "1" :
         print(a+b)
    if operation == "2" :
         print(a-b)
    if operation == "3" :
         print(a*b)
    if operation == "4" :
         print(a/b)

def exercice39():
    secret = random(1,10)
    a = int(input("pair ou impair :"))
    if a == "paire" and secret % 2 == 0 :
         print("gagnée")
    if a == "inpaire" and secret % 2 != 0 :
         print("gagnée")
    else :
         print("Perdu")

def exercice40():
    mdp = input("mdp:")
    if len(mdp) < 6 :
         print("trop court")
    else :
        print("Valide")

def exercice41():
    Notes = [10,12,14,8,16]
    a = 0 
    for i in range(0,len(Notes)):
        a += Notes[i]
    print(a/5)
    
def exercice42():
    L = [i for i in range(5)]
    max = 0
    min = 0
    for i in range(len(L)):
        if max > i :
             max = i
        if min < i :
             min = i
    print(min,max)

def exercice43(mot):
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for lettre in mot:
        if lettre in voyelles:
            compteur += 1
    return compteur

def exercice44(mot):
    return mot[::-1]

def exercice45(L):
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

def exercice46(L,a):
    for i in range(len(L)):
        if a == L[i]:
            print("trouvée")

def exercice47(L,a):
    compteur = 0
    for i in range(len(L)):
        if a == L[i]:
            compteur += 1
    return compteur

def exercice48(a):
    L=[]
    for i in range(1,a+1):
        if a % i == 0 :
            L.append(i)
    return L

def exercice49(a):
    for i in range(2,a):
        compteur = 0
        if a % i == 0:
            print("non premier")
            compteur += 1
    if compteur == 0 :
        print("premier")

def exercice50(N):
    L = [0, 1]
    for i in range(2,N):
         L.append(L[-1]+L[-2])
    print(L)

def exercice51(N):
      for i in range(1,N+1):
        pa=[1]
        for j in range(i):
            na = pa + [1]
            for e in range(0,len(pa) - 1):
                 na[e+1] = pa[e] + pa[e+1]
            pa = na
        print(pa)
        
def exercice52(n):
     print((n*((n**2) + 1))/2)

def exercice53(n):
    if n == 0 :
         print(0)
    L = []
    while n > 0:
        L.insert(0, n % 2)  
        n = n // 2           
    return L    

def exercice54():
    a = random(0,6)
    b = random(0,6)
    print(a+b)

def exercice55(n):
    a = 1
    for i in range(2,n+1):
        a = a*i
    print(a)
    
def exercice56(n):
    L=[]
    for i in range(n):
        L.append(3 * i + 2)
    print(L)

def exercice57(n):
    mots = n.split()
    print(mots)
    motlong = ""
    taillemax = 0
    for mot in mots :
        compteur = 0
        for lettre in mot:
            compteur += 1
        if compteur > taillemax:
             taillemax=compteur
             motlong=mot
    print(mot,compteur)

def exercice58(n):
    chiff = [int(c) for c in str(n)]
    a = 0
    for i in range(len(chiff)):
        a += chiff[i]**3
    if n == a :
        print("chiffre amstrong")
    else :
         print("ca ne l'est pas")

def exercice59(a,b):
    La = exercice48(a)
    Lb = exercice48(b)
    Lc = [x for x in La if x in Lb]
    if not Lc: 
        print("Pas d'éléments communs")
        return
    max = Lc[0] 
    for i in range(1,len(Lc)):
        if Lc[i] > max:
            max = Lc[i]
    print(max)

def exercice60(l,L):
    print(l*"*")
    for i in range(L):
        print("*",""*(l-2),"*")
    print(l*"*")

def exercice61(L):
    L0 = L[0]
    for i in range(len(L)):
         for j in range(len(L)-i):
              if L[i] < L[i + 1]
     

               

    
          
     
          

    
     

    
        
                  
          



def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "60":
        exercice60(4,3)
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()