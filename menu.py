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
        userCharacter1 = input("Choose A charater from Naruto!\n")
        character1 = None
        for player in choices:
                if userCharacter1 == player:
                    character1 = Player(userCharacter1, "")
                    character1.intro()
                    userCharacter2 = input("Choose Another Character\n")
                    
                elif userCharacter1 == "lol":
                    self.call = EasterEgg("1")
                    self.call.trick()
                    break
                elif userCharacter1 == "twitch":
                    self.call = EasterEgg("1")
                    self.call.promo()
                    break
                else:
                    print("Not Yet Implemented, Try Again!")
                    break
            
                character2 = Player(userCharacter2, "")
                character2.intro()
                self.arena = Arena(character1, character2)
                self.arena.fight()


test2 = EasterEgg("")
test2.trick()
test = Menu()

test.popUp()
test.questions()