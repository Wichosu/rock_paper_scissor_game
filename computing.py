move_set = ["Rock", "Paper", "Scissors"]

def compute(p1move, p2move):
    if p1move == p2move:
        print("DRAW")
    elif p1move == 1 and p2move == 2:
        print(f"P2 WINS with {move_set[p2move-1]}")
    elif p1move == 1 and p2move == 3:
        print(f"P1 WINS with {move_set[p1move-1]}")
    elif p1move == 2 and p2move == 1:
        print(f"P1 WINS with {move_set[p1move-1]}")
    elif p1move == 2 and p2move == 3:
        print(f"P2 WINS with {move_set[p2move-1]}")
    elif p1move == 3 and p2move == 1:
        print(f"P2 WINS with {move_set[p2move-1]}")
    elif p1move == 3 and p2move ==2:
        print(f"P1 WINS with {move_set[p1move-1]}")