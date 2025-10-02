# Exemple avec un seul exercice

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
      
      



def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()