from decimal import ROUND_HALF_DOWN
import random
from player import player
class ai(player):

    def aiSelection(self):
        self.setMove(random.randint(1, 3))
