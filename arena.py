import random
from player import Player


class Arena: 
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
    
    def fight(self):
        winners = [self.character1, self.character2]
        winner = random.choice(winners)
        print(f"And the winner is {winner}")




# sam = Player("Sam", "hi")
# rafa = Player("Rafa", "ji")
# test = Arena(sam, rafa)

# test.fight()