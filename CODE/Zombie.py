import random

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer_aleatoirement(self, carte):
        direction = random.choice(['nord', 'sud', 'est', 'ouest'])
        if direction == 'nord' and not carte.est_hors_limites(self.x, self.y - 1):
            self.y -= 1
        elif direction == 'sud' and not carte.est_hors_limites(self.x, self.y + 1):
            self.y += 1
        elif direction == 'est' and not carte.est_hors_limites(self.x + 1, self.y):
            self.x += 1
        elif direction == 'ouest' and not carte.est_hors_limites(self.x - 1, self.y):
            self.x -= 1
