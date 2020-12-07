import random

class Player: 
    def __init__(self, name, origin, ratio, motto):
        motto = ["omae", "wa", "mou", "shinderiu"]
        self.name = name
        self.origin = origin 
        self.ratio = ratio 
        self.motto = random.choice(motto)
    
    def 
