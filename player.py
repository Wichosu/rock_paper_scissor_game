class player:
    def __init__(self):
        self.__move = 0
    
    def setMove(self, move):
        self.__move = move
    
    def getMove(self):
        return self.__move

    def moveSelection(self):
        print("Choose your move")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissor")
        option = int(input())
        self.setMove(option)