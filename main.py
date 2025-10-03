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
        
def exercice52(L1,L2,L3):
    s1 = 0
    for i in range(3):
          s1 = s1 + L1[i]
    s2 = 0
    for i in range(3):
        s2 = s2 + L2[i]
    s3 = 0
    for i in range(3):
        s3 = s3 + L3[i]

    if not(s1 == s2 and s2 == s3):
         print("non")
    
    somme = s1

    c1= L1[0] + L2[1] + L3[2]
    c2= L1[1] + L2[1] + L3[1]
    c3=L1 [2] + L2[2] + L3[2]

    if not(c1 == somme and c2 == somme and c3 == somme):
         print("non")

    d1 = L1[0] + L2[1] + L3[2]
    d2 = L1[2] + L2[1] + L3[0]

    if d1==somme and d2==somme :
        print("oui")
    else:
         print("non")


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
    for i in range(len(L)):
        min_index = i
        for j in range(i+1,len(L)):
            if L[j] < L[min_index] :
                 min_index = j
            
        L[i], L[min_index] = L[min_index], L[i]
    return L
     
def exercice62(mot):
    L = list(mot)
    n = len(L)
    if n % 2 == 0:
        L1 = L[:n//2]
        L2 = L[n//2:]
    else :
         L1 = L[:n//2]
         L2 = L[(n//2+1):]

    L2 = L2[::-1]
    if L1 == L2 :
        print("Palindrome")
    else :
        print("non")

def exercice63(mot1,mot2):
    L1 = list(mot1)
    L2 = list(mot2)
    if len(L2) == len(L1):
        L3 =[x in L1 for x in L2]
        if len(L3) == len(L1):
             print("anagrame")
        else :
             print("pas anagrame")
    else :
         print("pas anagrame")
    
def exercice64(mots):
    L = list(mots)
    compteur = 1
    L1 = []
    for i in range(1,len(L)):
        if L[i] == L[i-1] :
            compteur += 1
        else :
             L1.append(L[i-1])
             L1.append(compteur)
             compteur = 1
    L1.append(L[-1])
    L1.append(compteur)
    
    print(L1)

def exercice65():
             
            
    
        
                  
          



def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "64":
        exercice64("aaabbc")
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()