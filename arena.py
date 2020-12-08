import random
from player import Player

class Arena: 
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def fight(self):
        winners = [self.player1, self.player2]
        winner = random.choice(winners)
        print(f"And the winner is {winner}")




sam = Player("Sam", "hi")
rafa = Player("Rafa", "ji")
test = Arena(sam, rafa)

# test.fight()