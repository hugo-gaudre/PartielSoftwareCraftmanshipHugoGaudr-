from Survivant import Survivant
from Carte import Carte
from Ressource import Ressource
from Zombie import Zombie
from Exploration import Exploration

def main():
   
    survivant = Survivant(5, 5, "nord", 100)  
    carte = Carte(10)


    carte.ajouter_ressource(Ressource(6, 5, "nourriture"))
    carte.ajouter_ressource(Ressource(4, 5, "eau"))
    carte.ajouter_ressource(Ressource(5, 6, "arme"))
    zombie = Zombie(0, 1)
    carte.ajouter_zombie(zombie)
    carte.ajouter_zombie(Zombie(9, 9))
    carte.ajouter_zombie(Zombie(1, 1))

   
    exploration = Exploration(survivant, carte)

    try:
        exploration.explorer("avancer")
        exploration.explorer("tournerDroite")
        exploration.explorer("avancer")
        exploration.explorer("tournerGauche")
        exploration.explorer("avancer")
        exploration.explorer("avancer")
    except Exception as e:
        print(e)

 
    print(f"Position du survivant : ({survivant.x}, {survivant.y})")
    print(f"Santé du survivant : {survivant.sante}")

 
    zombie.perdre_sante(20)
    print(f"Santé du zombie après l'attaque : {zombie.sante}")

if __name__ == "__main__":
    main()
