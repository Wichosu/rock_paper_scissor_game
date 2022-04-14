class player:
    def __init__(self):
        self.move = 0
    
    def set_move(self, move):
        self.move = move
    
    def get_move(self):
        return self.move

    def move_selection(self):
        print("Choose your move")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        option = int(input())
        self.set_move(option)