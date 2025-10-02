# Exemple avec un seul exercice
def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")
    prenom = input("entrée prenom utilisateur:")
    print(prenom)

def exercice2():
    print(yayayaya)

def main():
# Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    else:
        print("Exercice non reconnu.")

if __name__ == "__main__":
    main()
