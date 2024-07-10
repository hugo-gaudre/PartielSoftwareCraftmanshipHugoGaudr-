class Carte:
    def __init__(self, taille):
        self.taille = taille
        self.ressources = []
        self.zombies = []

    def ajouter_ressource(self, ressource):
        self.ressources.append(ressource)

    def ajouter_zombie(self, zombie):
        self.zombies.append(zombie)

    def est_hors_limites(self, x, y):
        return x < 0 or y < 0 or x >= self.taille or y >= self.taille
