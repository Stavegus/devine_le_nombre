# On importe le module random
import random
"""
On créer trois variable :
    nombre => on génere un nombre aléatoire entre 1 et 100
    chiffre_un => on génere un nombre aleatoire entre 0 et 50
    chiffre_deux => on fait pareil pour le deuxieme chiffre
"""
nombre = random.randint(0, 100)
chiffre_un = random.randint(0, 50)
chiffre_deux = random.randint(51, 100)
"""
On créer une variable essai et on l'initialise à zéro
On créer une variable point_de_vie et on l'initialise à 3 pour limiter le nombre de point de vie
"""
essai = ""
point_de_vie = 3

# On créer une boucle infini
while True:
    """
    On additionne chiffre_un et chiffre_deux et on divise par deux pour obtenir
    le résultat, puis on converti en int
    On récupére la saisie utilisateur et on la formate pour afficher le message
    suivant
    """
    nombre = int((chiffre_un + chiffre_deux) / 2)
    essai = input(f"Choissisez un nombre {chiffre_un} et {chiffre_deux} : ")

    """
    On force la conversion si il y a rien un message d'erreur apparaitra
    """
    try:
        essai = int(essai)
    except ValueError:
        print("ERREUR: Entrez un nombre correct")
    else:
        """
        La première condition vérifie si le résultat n'est pas égal si vrai:
            On retire un point de vie 
            On affiche les points de vie restant
            La deuxième condition vérifie si point de vie est égale à 0 si vrai:
                On affiche un message de game over
                On sort du programme 
        """
        if essai != nombre:
            point_de_vie -= 1
            print(point_de_vie, " point de vie restant")
            if point_de_vie == 0:
                print("Vous avez perdue")
                break

        """
        On vérifie si le chiffre deviné par l'utilisateur est égal à la réponse si vrai:
            On affiche un message de victoire
        Sinon si c'est trop grand
            On affiche c'est trop grand
        Sinon si c'est trop petit
            On affiche c'est trop petit
        """
        if essai == nombre:
            print("Vous avez gagné")
            break
        elif essai > nombre:
            print("C'est trop grand")
        else:
            print("C'est trop petit")
