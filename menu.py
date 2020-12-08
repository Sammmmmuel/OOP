from arena import Arena
from player import Player


class Menu: 
    def __init__(self):
        self.arena = None
        # self.startup = "startup"
    def popUp(self):
        print("Welcome to the Naruto Fighting Game !")

    def questions(self):
        players = ["Itachi", "Naruto", "Sasuke", "Madara", "Obito", "Minato", "Jiraiya", "Pain"]
        player1_name = input("Choose A charater from Nartuo! /n")
        for player in players:
            if player1_name == player:
                player2_name = input("Choose Another Character")
                break
            else:
                print("Not Yet Implemented, Try Again!")
                break
        
        player1 = Player(player1_name, "hi")
        player2 = Player(player2_name, "ji")
        self.arena = Arena(player1, player2)
        self.arena.fight()






test = Menu()

test.popUp()
test.questions()