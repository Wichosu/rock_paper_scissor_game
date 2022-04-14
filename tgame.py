from player import player
from ai import ai
import computing
p1 = player()
ai = ai()
print("Welcome to Rock Paper Scissor!!")
#print("Choose your move")
#print("1. Rock")
#print("2. Paper")
#print("3. Scissor")
while(True):
    p1.move_selection()
    ai.ai_selection()
    computing.compute(p1.get_move(), ai.get_move())
    print(f"ai choose {ai.get_move()}")