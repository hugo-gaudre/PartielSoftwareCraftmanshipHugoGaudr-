class Exploration:
    def __init__(self, survivant, carte):
        self.survivant = survivant
        self.carte = carte

    def explorer(self, commande):
        if commande == 'avancer':
            self.survivant.avancer()
        elif commande == 'tournerGauche':
            self.survivant.tourner_a_gauche()
        elif commande == 'tournerDroite':
            self.survivant.tourner_a_droite()
        else:
            raise Exception("Commande inconnue")

        if self.carte.est_hors_limites(self.survivant.x, self.survivant.y):
            raise Exception("Le survivant est hors des limites de la carte. Il est dieee.")

        self.rencontrer_zombie()

    def rencontrer_zombie(self):
        for zombie in self.carte.zombies:
            if self.survivant.x == zombie.x and self.survivant.y == zombie.y:
                self.survivant.perdre_sante(10)  
