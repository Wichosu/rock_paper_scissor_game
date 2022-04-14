from decimal import ROUND_HALF_DOWN
import random
from player import player
class ai(player):

    def ai_selection(self):
        self.set_move(random.randint(1, 3))
