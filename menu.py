from arena import Arena
from player import Player
from easterEgg import EasterEgg


class Menu(EasterEgg): 
    def __init__(self):
        self.arena = None
    def popUp(self):
        print("Welcome to the Naruto Fighting Game !")

    def questions(self):
        choices = ["Itachi", "Naruto", "Sasuke", "Madara", "Obito", "Minato", "Jiraiya", "Pain"]
        # for player in range(len(players)): 
        #     players[player] = players[player].lower()
        print("Choose A charater from Naruto!")
        character1 = None
        character2 = None
        while character1 is None or character2 is None:
            name = input()
            if name == "lol":
                EasterEgg().trick()
            elif name == "twitch":
                EasterEgg().promo()
                
            elif character1 is None:
                for choice in choices:
                    if name == choice:
                        character1 = Player(name, "")
                        character1.intro()
                        print("Choose Another Character")
                        # break
                
            elif character2 is None:
                for choice in choices:
                    if name == choice:
                        character2 = Player(name, "")
                        character2.intro()
                        # break
                # if userCharacter1 == choices:
                #     character1 = Player(userCharacter1, "")
                #     character1.intro()
                #     userCharacter2 = input("Choose Another Character\n")
                # elif userCharacter1 == "lol":
                #     self.call = EasterEgg("1")
                #     self.call.trick()
                #     break
                # elif userCharacter1 == "twitch":
                #     self.call = EasterEgg("1")
                #     self.call.promo()
                #     break
                # else:
                #     print("Not Yet Implemented, Try Again!")
                #     break
        self.arena = Arena(character1, character2)
        self.arena.fight()


test2 = EasterEgg()
test2.trick()
test = Menu()

test.popUp()
test.questions()