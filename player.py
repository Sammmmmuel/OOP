import random


class Player: 
    def __init__(self, name, motto):
        mottos = ["omae", "wa", "mou", "shinderiu"]
        self.name = name
        self.motto = random.choice(mottos)
    
    def sayMotto(self):
        print(f"As {self.name} enters he says {self.motto}\n")

    def intro(self):
        print(f"Welcome {self.name}\n")

    def __str__(self):
        return self.name










# test = Player("itachi", "naruto")
# test2 = Player("naruto", "k")

# test.sayMotto()
# test.intro()
# test2.intro()